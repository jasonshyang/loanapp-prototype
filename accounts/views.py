from django.forms import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

# Create your views here.
from .models import Account
from .forms import AccountCreationForm, BorrowerInfoForm, LenderInfoForm
from django.views import generic
from .utils import get_risk_score, get_risk_level

class IndexView(generic.ListView):
    template_name = "accounts/index.html"
    context_object_name = "account_list"

    def get_queryset(self):
        return Account.objects.order_by("-updated_at")


class CreateView(generic.CreateView):
    template_name = "accounts/register.html"
    form_class = AccountCreationForm
    success_url = "/accounts/"

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

class BorrowerView(generic.CreateView):
    template_name = "accounts/register.html"
    form_class = BorrowerInfoForm
    success_url = "/accounts/"

    @method_decorator(csrf_protect)
    def dispatch(self, request, *args, **kwargs):
        if 'account_type' not in request.session:
            return HttpResponseRedirect(reverse('accounts:register'))
        account = Account.objects.get(id=request.session['id'])
        if request.session['account_type'] != account.account_type:
            return HttpResponseRedirect(reverse('accounts:register'))
        return super().dispatch(request, *args, **kwargs)
    
    
    def form_valid(self, form):
        if form.is_valid():
            borrower = form.save(commit=False)
            borrower.account = Account.objects.get(id=self.request.session['id'])
            borrower.risk_score = get_risk_score()
            borrower.risk_level = get_risk_level(borrower.risk_score)
            borrower.save()
        return super().form_valid(form)


class LenderView(generic.CreateView):
    template_name = "accounts/register.html"
    form_class = LenderInfoForm
    success_url = "/accounts/"

    @method_decorator(csrf_protect)
    def dispatch(self, request, *args, **kwargs):
        if 'account_type' not in request.session:
            return HttpResponseRedirect(reverse('accounts:register'))
        account = Account.objects.get(id=request.session['id'])
        if request.session['account_type'] != account.account_type:
            return HttpResponseRedirect(reverse('accounts:register'))
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        if form.is_valid():
            lender = form.save(commit=False)
            lender.account = Account.objects.get(id=self.request.session['id'])
            lender.save()
        return super().form_valid(form)


class DetailView(generic.DetailView):
    model = Account
    template_name = "accounts/detail.html"

# TODO: Add views for login and continuing the registration process