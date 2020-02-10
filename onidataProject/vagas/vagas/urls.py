"""vagas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.urls import path, include
from contracts.views import ContractView, ContractsView, ContractAmountDueView
from payments.views import PaymentView, PaymentsView
from .views import login
# Wire up our API using automatic URL routing.
# Additionally, we include login
urlpatterns = [
    path('admi', admin.site.urls),
    path('auth', login),
    # contracts
    path('contracts',ContractsView.as_view()),
    path('contracts/<uuid:id>',ContractView.as_view()),
    path('contracts/amount-due/<uuid:id>',ContractAmountDueView.as_view()),
    #payments
    path('payments',PaymentsView.as_view()),
    path('payments/<uuid:id>',PaymentView.as_view())
]
