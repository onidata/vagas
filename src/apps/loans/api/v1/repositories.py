from django.contrib.auth.models import User
from django.db.utils import IntegrityError, OperationalError
from loans.models import Loans
from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.validators import ValidationError


class LoansBaseRepository:
    def __init__(self, model=Loans):
        self.model = model


class ListAllLoansRepository(LoansBaseRepository):
    def handle(self, user_id):
        loans = self.model.objects.filter(customer=user_id)
        return loans


class GetCustomerFromUserModelRepository:
    @classmethod
    def handle(cls, user_id, user=User):
        return user.objects.get(id=user_id)


class CreateLoanRepository(LoansBaseRepository):
    def handle(self, user_id, validated_data, iof_interest_rate, cet_amount):
        user = GetCustomerFromUserModelRepository.handle(user_id)
        import ipdb

        ipdb.set_trace()
        try:
            loan = self.model.objects.create(
                amount=validated_data["amount"],
                interest_rate=validated_data["interest_rate"],
                ip_address=validated_data["ip_address"],
                bank=validated_data["bank"],
                customer=user,
                installments=validated_data["installments"],
                cet_amount=cet_amount,
                iof_interest_rate=iof_interest_rate,
                insurance=validated_data["insurance"],
            )
            loan.full_clean()
            loan.save()

        except (IntegrityError, OperationalError) as error:
            raise ValidationError(
                detail={"error": error},
                code=HTTP_500_INTERNAL_SERVER_ERROR,
            )
