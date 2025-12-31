from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import LoginSerializer
from apps.users.models import User
from rest_framework.response import Response
from rest_framework.views import APIView

from .tokens import email_verification_token


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

class VerifyEmailView(APIView):
    permission_classes = []

    def get(self, request):
        uid = request.GET.get('uid')
        token = request.GET.get('token')

        try:
            user = User.objects.get(id=uid)
        except User.DoesNotExist:
            return Response({"error": "Invalid user"}, status=400)

        if email_verification_token.check_token(user, token):
            user.is_verified = True
            user.save()
            return Response({"message": "Email verified"}, status=200)
        else:
            return Response({"error": "Invalid or expired token"}, status=400)