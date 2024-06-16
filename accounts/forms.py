from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account

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