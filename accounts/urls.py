from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

app_name = "accounts"
urlpatterns = [
    # ex: /accounts/
    path("", views.IndexView.as_view(), name="index"),
    # ex: /accounts/5/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # ex: /accounts/register/
    path("register/", views.CreateView.as_view(), name="register"),
    # ex: /accounts/view/login/
    path("login/", views.AuthView.as_view(), name="login"),
]