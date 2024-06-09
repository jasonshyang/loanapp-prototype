from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account, BorrowerInfo, LenderInfo

class AccountCreationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = (
            'username', 
            'password1', 
            'password2',
            'email', 
            'account_type', 
        )

class BorrowerInfoForm(forms.ModelForm):
    class Meta:
        model = BorrowerInfo
        fields = (
            'income', 
            'occupation', 
        )

class LenderInfoForm(forms.ModelForm):
    class Meta:
        model = LenderInfo
        fields = (
            'risk_appetite', 
        )