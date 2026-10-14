from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from apps.users.models import Users
from .serializers import AuthsSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status


class AuthsViewset(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = AuthsSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=["post"], basename="login")
    def login(self, request):
        data = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            user = Users.objects.get(email=data["email"])
            refresh_token = RefreshToken.for_user(user)
            access_token = refresh_token.access_token
            return Response(
                {
                    "user": serializer.validated_data,
                    "refresh_token": str(refresh_token),
                    "access_token": str(access_token),
                },
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
