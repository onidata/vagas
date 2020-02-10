from rest_framework import serializers
from payments.models import Payment
# forms.py
class PaymentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = ('id','date','amount','contract_id')
