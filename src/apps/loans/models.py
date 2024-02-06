from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class Loans(models.Model):
    id = models.UUIDField(
        verbose_name="Identificador",
        primary_key=True,
        default=uuid4,
    )
    amount = models.DecimalField(
        verbose_name="Valor do Empréstimo",
        max_digits=10,
        decimal_places=2,
    )
    interest_rate = models.DecimalField(
        verbose_name="Taxa de Juros Mensal",
        max_digits=10,
        decimal_places=2,
    )
    ip_address = models.CharField(
        verbose_name="Endereço IPv4 do Solicitante",
        max_length=15,
        blank=False,
        null=False,
    )
    date = models.DateTimeField(
        verbose_name="Data de Solicitação do Empréstimo",
        db_index=True,
        default=now,
    )
    bank = models.CharField(
        verbose_name="Instituição Financeira",
        max_length=128,
        blank=False,
        null=False,
    )
    customer = models.ForeignKey(
        User,
        models.CASCADE,
        verbose_name="Solicitante do Empréstimo",
        blank=False,
        null=False,
    )
    installments = models.IntegerField(
        verbose_name="Quantidade de Parcelas",
        blank=False,
        null=False,
    )
    cet_amount = models.DecimalField(
        verbose_name="Custo Efetivo Total",
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )
    iof_interest_rate = models.DecimalField(
        verbose_name="Imposto sobre operações financeiras",
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )
    insurance = models.DecimalField(
        verbose_name="Porcentagem do Seguro Prestamista",
        max_digits=10,
        decimal_places=2,
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = "Empréstimo"
        verbose_name_plural = "Empréstimos"

    def __str__(self) -> str:
        return f"ID: {self.id} - Amount: {self.amount}"
