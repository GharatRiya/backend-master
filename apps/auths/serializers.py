from rest_framework import serializers
from apps.users.models import Users


class AuthsSerializer(serializers.ModelSerializer):

    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        model = Users
        fields = ["email", "password"]

    def validate(self, attrs):
        password = attrs.get("password")
        email = attrs.get("email")

        user = Users.objects.filter(email=email).first()

        if not user:
            raise serializers.ValidationError({"error": "Invalid credentials"})
        if not user.check_password(password):
            raise serializers.ValidationError({"error": "Invalid credentials"})
        attrs["user_id"] = user.id
        attrs["first_name"] = user.first_name
        attrs["last_name"] = user.last_name
        attrs["email"] = user.email
        return attrs
