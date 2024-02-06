from typing import Any

from django.contrib import admin
from django.http.request import HttpRequest

from .models import Loans


@admin.register(Loans)
class LoansAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "date",
        "bank",
        "customer",
        "installments",
        "cet_amount",
    ]
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

    def has_change_permission(
        self, request: HttpRequest, obj: Any | None = ...
    ) -> bool:
        return False

    def has_delete_permission(
        self, request: HttpRequest, obj: Any | None = ...
    ) -> bool:
        return False
