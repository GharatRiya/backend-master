from rest_framework import status  # <-- Add this missing import
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from .models import Users
from .serializers import UserSerializer


class UserViewset(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Users.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # status is now properly imported and will work as expected
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        data = self.queryset
        serializer = self.get_serializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    

    def update(self, request, *args, **kwargs):

        id = kwargs["pk"]
        data = self.queryset.filter(id=id)
        print(data)

        if not data:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )
        else:
            serializer = self.get_serializer(data, data=request.data, partial=True)
            if serializer.is_valid():
                self.perform_create(serializer)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(
                {"error": "Data not valid"}, status=status.HTTP_400_BAD_REQUEST
            )
