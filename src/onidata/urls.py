from apps.loans.api.v1.views import LoansListAndCreateView
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views

loans_patterns = [
    path("", LoansListAndCreateView.as_view(), name="list_and_create"),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-token-auth/", views.obtain_auth_token),
    path("v1/loans/", include((loans_patterns, "loans"))),
]
