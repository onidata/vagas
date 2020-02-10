from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden, HttpResponseRedirect, Http404
from django.core.serializers import serialize
from payments.serializer import PaymentSerializers
from django.db.models import Prefetch
from payments.models import Payment
from contracts.models import Contract
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from rest_framework.views import APIView
from django.forms.models import model_to_dict
import json, uuid


# Create your views here.

class PaymentsView(APIView):
    '''
    '''
    def post(self, request):
        try:
            serialized = PaymentSerializers(data=request.data)
            if serialized.is_valid():
                serialized.save()
                data = {
                'status': 'success',
                'payment': serialized.data
                }
                response = Response(data, status=HTTP_200_OK)
            else:
                data = {
                'status': 'error',
                'errors': serialized.errors
                }
                response = Response(data)
        except Exception as e:
            data = {
            'status': 'error',
            'errors': str(e)
            }
            response = Response(data)
        return response

    def get(self,request):
        try:
            payment_query = Payment.objects.prefetch_related(
                Prefetch('contract_id', queryset=Contract.objects.filter(
                    owner_id=request.user.id
                    )))
            serialized = PaymentSerializers(payment_query,many=True)
            data = {
            'status':'success',
            'all_payments': serialized.data
            }
            response = Response(data, status=HTTP_200_OK)
        except Exception as e:
            data = {'status': 'error', 'reason': str(e)}
            response = Response(data)
        return response

class PaymentView(APIView):
    '''
    '''
    def get(self,request,id):
        try:
            payment = get_object_or_404(Payment, id=id)
            contract = get_object_or_404(Contract, id=payment.contract_id.id)
            # check if user is owner
            if request.user != contract.owner_id:
                raise Http404
            serialized = PaymentSerializers(payment)
            data = {
            'status':'success',
            'payment': serialized.data
            }
            response = Response(data, status=HTTP_200_OK)
        except Exception as e:
            data = {'status': 'error', 'reason': str(e) or 'User Not Allowed'}
            response = Response(data)
        return response
