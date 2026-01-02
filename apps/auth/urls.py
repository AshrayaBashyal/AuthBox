from django.urls import path
from .views import LoginView, VerifyEmailView, LogoutView
from rest_framework_simplejwt.views import TokenRefreshView
from ..users.views import ForgotPasswordView, ResetPasswordView

app_name = "auth"

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path("refresh/", TokenRefreshView.as_view(), name='token_refresh'),
    path("verify-email/", VerifyEmailView.as_view(), name='verify_email'),
    path("forgot-password/", ForgotPasswordView.as_view(), name='forgot_password'),
    path("reset-password/", ResetPasswordView.as_view(), name='password_reset'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]