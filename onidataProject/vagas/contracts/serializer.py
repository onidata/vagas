from rest_framework import serializers
from contracts.models import Contract
# forms.py
class ContractSerializers(serializers.ModelSerializer):
    bank = serializers.JSONField()
    customer_metadata = serializers.JSONField()
    class Meta:
        model = Contract
        fields = ('id','amount','interest_rate','ip_address','bank','customer_metadata')
