from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer
from apps.emails.services import send_verification_email


class RegisterView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        send_verification_email(user)

        return Response(
            {"message": "Account created. Please verify your email."},
            status=status.HTTP_201_CREATED
        )
