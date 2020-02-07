from django.db import models
from django.db import models
from django.core.validators import MinValueValidator
from core.models import BaseModel

# Create your models here.

class Payment(BaseModel):
    contract = models.ForeignKey('contracts.Contract',
                                 related_name='payments',
                                 on_delete=models.CASCADE,
                                 help_text='Contract Payment')
    value = models.FloatField(
        help_text='Payment Price',
        validators=[MinValueValidator(limit_value=1)])
    date = models.DateField(
        help_text='Payment Date'
    )

    class Meta:
        ordering = ['contract_id']

    @property
    def owner(self):
        return self.contract.owner
