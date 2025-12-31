from apps.auth.jwt import CustomTokenObtainPairSerializer
from rest_framework.exceptions import AuthenticationFailed


class LoginSerializer(CustomTokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        if not self.user.is_verified:
            raise AuthenticationFailed("Email not verified")

        return data
