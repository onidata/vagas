from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LoanCreateSerializer, LoansSerializer
from .services import CreateLoanService, ListAllLoansService


class LoansListAndCreateView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_id = request.user.id
        service = ListAllLoansService()
        loans_queryset = service.handle(user_id)
        validated_data = LoansSerializer(loans_queryset, many=True).data
        return Response({"data": validated_data})

    def post(self, request):
        user_id = request.user.id
        payload = request.data
        service = CreateLoanService()
        validated_data = LoanCreateSerializer(payload).data
        data = service.handle(user_id, validated_data)
        return Response({"data": data})
