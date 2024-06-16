from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from accounts.models import Account
from core.constants import MONEY_REQUEST_STATUS, MONEY_REQUEST_TYPE
# Create your models here.


class MoneyRequest(models.Model):
    borrower = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='borrower')
    lender = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='lender')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=10, choices=MONEY_REQUEST_TYPE)
    status = models.CharField(max_length=10, choices=MONEY_REQUEST_STATUS, default='OPEN')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.borrower.account_type != 'BORROWER':
            raise ValueError('INVALID ACCOUNT TYPE - Borrower must be a Borrower to have MoneyRequest')
        if self.lender is not None and self.lender.account_type != 'LENDER':
            raise ValueError('INVALID ACCOUNT TYPE - Lender must be a Lender to have MoneyRequest')
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.type} - Loan Amount: {self.amount}"