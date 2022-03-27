from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView

from .views import *

urlpatterns = [
    path("", homepage, name="homepage"),
    path("sign-up/", signUp, name="sign-up"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("login/", LoginView.as_view(template_name="core/login.html"), name="login"),
]