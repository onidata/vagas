from datetime import datetime

from dateutil.relativedelta import relativedelta

from .repositories import CreateLoanRepository, ListAllLoansRepository

TAX_TAXATION_VALUE = 0.38
DAILY_AMORTIZATION_VALUE = 0.0082
LIMIT_TAX_IOF_VALUE = 0.03


class LoanTimeInDays:
    @classmethod
    def handle(cls, installments):
        today = datetime.now()
        final_loan_date = today + relativedelta(months=installments)
        difference = final_loan_date - today
        return difference.days


class IOFInterestRateService:
    @classmethod
    def handle(cls, amount, loan_time_in_days):
        """Function to calculate IOF Tax according Brazilian Regulation

        Args:
            amount (Decimal): loan value request by customer
            loan_time_in_days (Int): time of loan

        Returns:
            iof_interest_rate (Decimal): iof final value
        """

        tax_taxation = amount * TAX_TAXATION_VALUE
        daily_amortization = (
            amount * loan_time_in_days * DAILY_AMORTIZATION_VALUE
        )  # noqa E501
        limit_value_daily_amortization = amount * LIMIT_TAX_IOF_VALUE

        condition_to_use_limit_value = (
            daily_amortization > limit_value_daily_amortization
        )

        iof_interest_rate = 0

        if condition_to_use_limit_value:
            iof_interest_rate = round(
                tax_taxation + limit_value_daily_amortization, 2
            )  # noqa E501
            return iof_interest_rate

        iof_interest_rate = round(tax_taxation + daily_amortization, 2)
        return iof_interest_rate


class CetAmountService:
    @classmethod
    def handle(
        cls,
        amount,
        interest_rate,
        installments,
        iof_interest_rate,
        insurance,
    ):
        rate = interest_rate / 100
        compound_interest = amount * (1 + rate) ** installments
        cet_amount = round(
            (compound_interest + iof_interest_rate) * (1 + (insurance / 100)),
            2,  # noqa E501
        )
        return str(cet_amount)


class ListAllLoansService:
    def __init__(self, repository=ListAllLoansRepository()):
        self.repository = repository

    def handle(self, user_id):
        return self.repository.handle(user_id)


class CreateLoanService:
    def __init__(self, repository=CreateLoanRepository()):
        self.repository = repository

    def handle(self, user_id, validated_data):
        amount = float(validated_data["amount"])
        installments = int(validated_data["installments"])
        interest_rate = float(validated_data["interest_rate"])
        insurance = float(validated_data["insurance"])

        loan_time_in_days = LoanTimeInDays.handle(installments)
        iof_interest_rate = IOFInterestRateService.handle(
            amount, loan_time_in_days
        )  # noqa E501

        cet_amount = CetAmountService.handle(
            amount,
            interest_rate,
            installments,
            iof_interest_rate,
            insurance,
        )

        return self.repository.handle(
            user_id,
            validated_data,
            iof_interest_rate,
            cet_amount,
        )
