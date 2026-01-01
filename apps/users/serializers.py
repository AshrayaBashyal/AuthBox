from rest_framework import serializers
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ("email", "username", "password")

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data["email"],
            username=validated_data["username"],
            password=validated_data["password"],
            is_active=True,
            is_verified=False
        )
        return user


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("No user with this email exists!")
        return value


class ResetPasswordSerializer(serializers.Serializer):
    uid = serializers.IntegerField(write_only=True)
    token = serializers.CharField(write_only=True)
    new_password = serializers.CharField(min_length=8, write_only=True)

    def validate(self, data):
        from apps.auth.tokens import password_reset_token
        from .models import User

        try:
            user = User.objects.get(id=data["uid"])
        except User.DoesNotExist:
            raise serializers.ValidationError("No user with this ID exists!")

        if not password_reset_token.check_token(user, data["token"]):
            raise serializers.ValidationError("Invalid or expired token")

        data["user"] = user

        return data

    def save(self):
        user = self.validated_data["user"]
        password = user.set_password(self.validated_data["new_password"])
        user.save()