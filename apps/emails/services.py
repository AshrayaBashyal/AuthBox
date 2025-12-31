from apps.auth.tokens import email_verification_token
from django.conf import settings
from django.core.mail import send_mail


def build_verification_link(user):
    token = email_verification_token.make_token(user)
    return f"http://localhost:8000/api/auth/verify-email/?uid={user.id}&token={token}"

def send_verification_email(user):
    link = build_verification_link(user)
    send_mail(
        "Verify Your Email",
        f"Click here to verify your email: {link}",
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False
    )