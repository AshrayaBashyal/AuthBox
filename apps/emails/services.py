from apps.auth.tokens import email_verification_token
from django.core.mail import EmailMessage
from django.conf import settings


def build_verification_link(user):
    token = email_verification_token.make_token(user)
    return f"http://localhost:8000/api/auth/verify-email/?uid={user.id}&token={token}"

def send_verification_email(user):
    link = build_verification_link(user)

    email = EmailMessage(
        subject="Verify Your Email",
        body=f"Click here to verify your email:\n\n{link}",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[user.email],
    )

    email.send()