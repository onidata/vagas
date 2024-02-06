from loans.models import Loans
from rest_framework import serializers


class LoansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loans
        fields = [
            "id",
            "amount",
            "interest_rate",
            "ip_address",
            "date",
            "bank",
            "customer",
            "installments",
            "cet_amount",
            "iof_interest_rate",
            "insurance",
        ]


class LoanCreateSerializer(serializers.Serializer):
    amount = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=True,
    )
    interest_rate = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=True,
    )
    ip_address = serializers.CharField(
        max_length=15,
        required=True,
    )
    bank = serializers.CharField(
        max_length=128,
        required=True,
    )
    installments = serializers.IntegerField()
    insurance = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=True,
    )
