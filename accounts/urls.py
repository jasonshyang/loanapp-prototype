from django.urls import path

from . import views

app_name = "accounts"
urlpatterns = [
    # ex: /accounts/
    path("", views.IndexView.as_view(), name="index"),
    # ex: /accounts/5/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # ex: /accounts/register/
    path("register/", views.CreateView.as_view(), name="register"),
    # ex: /accounts/register/borrower/
    path("register/borrower/", views.BorrowerView.as_view(), name="register/borrower"),
    # ex: /accounts/register/lender/
    path("register/lender/", views.LenderView.as_view(), name="register/lender"),
]