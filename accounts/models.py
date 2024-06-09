from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from core.constants import ACCOUNT_TYPE, OCCUPATION, RISK_LEVEL, ACCOUNT_STATE
# Create your models here.


class Account(AbstractUser):
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE)
    account_state = models.CharField(max_length=20, choices=ACCOUNT_STATE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="account_set",
        related_query_name="account",
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="account_set",
        related_query_name="account",
    )

    def __str__(self):
        return self.username
    
class BorrowerInfo(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    income = models.DecimalField(max_digits=10, decimal_places=2)
    occupation = models.CharField(max_length=2, choices=OCCUPATION)
    risk_score = models.IntegerField(null=True, blank=True)
    risk_level = models.CharField(max_length=10, choices=RISK_LEVEL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.account.account_type != 'BORROWER':
            raise ValueError('INVALID ACCOUNT TYPE - Account must be a Borrower to have BorrowerInfo')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.account.username
    
class LenderInfo(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    risk_appetite = models.CharField(max_length=10, choices=RISK_LEVEL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.account.account_type != 'LENDER':
            raise ValueError('INVALID ACCOUNT TYPE - Account must be a Lender to have LenderInfo')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.account.username