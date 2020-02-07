from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from core.models import BaseModel

# Create your models here.


class User(AbstractUser, BaseModel):
    email = models.EmailField(_('email address'), unique=True, help_text='User Email')
    cpf = models.CharField(help_text='CPF', unique=True, max_length=14)

    class Meta:
        ordering = ['id']

    @property
    def owner(self):
        return self
