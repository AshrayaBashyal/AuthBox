from django.urls import path
from .views import LoginView, VerifyEmailView
from rest_framework_simplejwt.views import TokenRefreshView
from ..users.views import ForgotPasswordView, ResetPasswordView

app_name = "auth"

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path("refresh/", TokenRefreshView.as_view(), name='token_refresh'),
    path("verify-email/", VerifyEmailView.as_view()),
    path("forgot-password/", ForgotPasswordView.as_view()),
    path("reset-password/", ResetPasswordView.as_view()),
]