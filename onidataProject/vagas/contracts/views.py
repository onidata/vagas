from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden, HttpResponseRedirect, Http404
from contracts.serializer import ContractSerializers
from django.core.serializers import serialize
from contracts.models import Contract
from payments.models import Payment
from django.core.serializers.json import DjangoJSONEncoder
from datetime import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from rest_framework.views import APIView
from django.forms.models import model_to_dict
import json,sys

# Create your views here.

class ContractsView(APIView):
    '''
    '''
    def post(self, request):
        try:
            serialized = ContractSerializers(data = request.data)
            if serialized.is_valid():
                serialized.save(owner_id=request.user)
                data = {
                'status': 'success',
                'contract': serialized.data
                }
                response = Response(data, status=HTTP_200_OK)
            else:
                data = {
                'status': 'error',
                'error': serialized.errors
                }
                response = Response(data)
        except Exception as e:
            data = {
            'status':'error',
            'contract': str(e)
            }
            response = Response(data)
        return response

    def get(self, request):
        try:
            contract_query = Contract.objects.filter(owner_id=request.user.id)
            serialized = ContractSerializers(contract_query,many=True)
            data = {
            'status':'success',
            'all_contracts': serialized.data
            }
            response = Response(data, status=HTTP_200_OK)
        except Exception as e:
            data = {
            'status':'error',
            'contract': str(e)
            }
            response = Response(data)
        return response

class ContractView(APIView):
    '''
    '''
    def get(self, request, id):
        #check if user is owner
        try:
            contract = get_object_or_404(Contract, pk=id)
            serialized = ContractSerializers(contract)
            if request.user != contract.owner_id:
                raise Http404
            data = {
            'status':'success',
            'contract': serialized.data
            }
            response = Response(data, status=HTTP_200_OK)
        except Exception as e:
            data = {
            'status':'error',
            'contract': str(e) or 'User not Allowed'
            }
            response = Response(data)
        return response

class ContractAmountDueView(APIView):
    '''
    '''
    def get(self,request, id):
        try:
            #check if user is owner
            contract = get_object_or_404(Contract, pk=id)
            if request.user != contract.owner_id:
                raise Http404

            payment_query = Payment.objects.filter(
            contract_id=id
            )
            amount = 0
            for payment in payment_query:
                amount += payment.amount
            delta = datetime.now().date() - contract.submission_date.date()
            months = int(delta.days/30)
            amount_due = contract.amount
            for i in range(1,months):
                amount_due += amount_due * contract.interest_rate
            data = {
            'status':'success',
            'contract_id': id,
            'contract': amount_due - amount
            }
            response = Response(data, status=HTTP_200_OK)
        except Exception as e:
            data = {
            'status':'error',
            'contract': str(e) or 'User not Allowed'
            }
            response = Response(data)
        return response
