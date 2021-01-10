import jwt
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from core.permissions import IsMe
from rest_framework.exceptions import NotFound, AuthenticationFailed
from django.contrib.auth import authenticate
from django.conf import settings
from .serializer import UserSerializer, LoginSerializer, LoginResultSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ["create", "list", "retrieve"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsMe]
        return [permission() for permission in permission_classes]


class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        # (instance, data) -> 순서
        username = request.data.get("username")
        password = request.data.get("password")
        try:
            user = User.objects.get(username=username)
            if not authenticate(username=username, password=password):
                raise AuthenticationFailed()
            token = jwt.encode({"pk": user.pk}, settings.SECRET_KEY, algorithm="HS256")
            result = LoginResultSerializer({"token": token, "user": user})
            return Response(data=result.data)
        except User.DoesNotExist:
            raise NotFound()
