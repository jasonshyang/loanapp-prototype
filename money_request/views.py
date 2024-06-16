from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views import generic
from django.http import HttpResponseRedirect
from django.forms import ValidationError
from .models import MoneyRequest
from .forms import MoneyRequestForm


# Create your views here.
class CreateView(generic.CreateView):
    template_name = "money_requests/register.html"
    form_class = MoneyRequestForm
    success_url = "/money_requests/"

    @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        if form.is_valid():
            account_type = form.cleaned_data.get('account_type')
            if account_type not in ['BORROWER', 'LENDER']:
                raise ValidationError("Invalid account type. Account must be either a borrower or a lender.")
            account = form.save(commit=False)
            account.account_state = "active"
            account.save()
            self.request.session['account_type'] = account.account_type
            self.request.session['id'] = account.id

            if account.account_type == 'BORROWER':
                return HttpResponseRedirect(reverse('accounts:register/borrower'))
            elif account.account_type == 'LENDER':
                return HttpResponseRedirect(reverse('accounts:register/lender'))
            
        return super().form_valid(form)
