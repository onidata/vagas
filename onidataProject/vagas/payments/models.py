import uuid
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from contracts.models import Contract

# Create your models here.

class Payment(models.Model):
    """
    Contract identifier
    Payment date
    Payment amount
    """
    #fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateTimeField(default=timezone.now, editable=False, verbose_name="Payment Date")
    amount = models.DecimalField(default=0.00, max_digits=11, decimal_places=2, verbose_name="Payment Amount")
    #foreign keys
    contract_id = models.ForeignKey(Contract, on_delete=models.PROTECT, verbose_name="Related Contract", related_name='payments')


    #Meta
    class Meta:
        verbose_name = _("Payment")
        verbose_name_plural = _("Payments")
        ordering = ['-date']

    #functions
    def __str__(self):
        return str(self.id)
