from django.forms import ValidationError
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import views as auth_views
from django.views import generic

# Create your views here.
from .models import Account
from .forms import AccountCreationForm
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
            account = form.save(commit=False)
            if account.account_type == 'BORROWER':
                account.risk_score = get_risk_score()
                account.risk_level = get_risk_level(account.risk_score)                
            elif account.account_type == 'LENDER':
                pass
            else:
                raise ValidationError("Invalid account type. Account must be either a borrower or a lender.")
            account.save()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class DetailView(generic.DetailView):
    model = Account
    template_name = "accounts/detail.html"


class AuthView(auth_views.LoginView):
    template_name = "accounts/login.html"
    next_page = "/accounts/"
    

'''
def user_login(request):
    username = request.POST("username")
    password = request.POST("password")
    account = authenticate(request, username=username, password=password)
    if account is not None:
        login(request, account)
        return HttpResponseRedirect(reverse('accounts:detail', args=(account.id,))) # type: ignore
    else:
        return HttpResponseNotFound('Invalid login credentials. Please try again.')
'''
# TODO: Add views for login and continuing the registration process, Add views for updating account information, Add views for deleting accounts