from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from core.constants import ACCOUNT_TYPE, OCCUPATION, RISK_LEVEL, ACCOUNT_STATE
# Create your models here.


class Account(AbstractUser):
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE)
    account_state = models.CharField(max_length=20, choices=ACCOUNT_STATE)
    risk_score = models.IntegerField(null=True, blank=True)
    risk_level = models.CharField(max_length=10, choices=RISK_LEVEL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username