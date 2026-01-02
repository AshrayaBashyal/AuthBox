# =========================================
# ISSUE NOTE:
# Email verification link generates ValueError: Field 'id' expected a number but got '3D…'.
# Printed Raw email shows: uid=3D16&token=3D1p3le… due to quoted-printable encoding. (= <--> =3D)
# Django fails at User.objects.get(id=uid).
# # Is there a reliable way to prevent =3D in the URL from breaking user verification?
# Tried URL encoding, base64, EmailMessage vs EmailMultiAlternatives, HTML email, charset tweaks — nothing prevents corruption.
# Nothing works. The 3D appears in the raw email source and corrupts the UID, causing the ValueError.
# =========================================
from django.utils.http import urlencode
from apps.auth.tokens import email_verification_token, password_reset_token
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


def build_password_reset_link(user):
    token = password_reset_token.make_token(user)
    params = urlencode({"uid": user.id, "token": token})
    return f"http://localhost:8000/api/auth/reset-password/?{params}"


def send_password_reset_email(user):
    link = build_password_reset_link(user)
    email = EmailMessage(
        subject="Reset Your Password",
        body=f"Click here to reset your password:\n\n{link}",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[user.email],
    )
    email.content_subtype = "plain"
    print(" Password reset email (console):")
    print(email.body)       # prints email to console
    email.send()       # with console backend, this prints to terminal