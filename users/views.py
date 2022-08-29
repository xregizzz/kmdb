from rest_framework.views import APIView, Request, Response, status
from .serializers import UserSerializer, LoginSerializer
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import TokenAuthentication
from .models import User


class UserLogin(APIView):
    def post(self, request: Request) -> Response:
        serializer = LoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"],
        )

        if not user:
            return Response({"detail": "invalid username or password"})

        token, _ = Token.objects.get_or_create(user=user)

        return Response({"token": token.key})


class UserView(APIView):
    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class ProtectedUserView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request: Request) -> Response:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)


class ProtectedUserDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request: Request, user_id: int) -> Response:

        user = get_object_or_404(User, id=user_id)

        serializer = UserSerializer(user)

        return Response(serializer.data)
