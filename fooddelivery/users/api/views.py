from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import generics

from users.models import User
from users.api.serializers import (
    UserCreateSerializer,
    UserUpdateSerializer,
    UserDetailSerializer,
    UserListSerializer,
    PasswordResetRequestSerializer,
    CodeVerificationSerializer,
    PasswordChangeSerializer)

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAdminUser]

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()    
    permission_classes = [IsAdminUser]

#Paso1: Enviar el código al correo
class PasswordResetView(generics.GenericAPIView):
    serializer_class = PasswordResetRequestSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": "Se ha enviado un código de verificación a tu correo electrónico."})

#Paso2: Verificar el código y devolver un token temporal
class CodeVerificationView(generics.GenericAPIView):
    serializer_class = CodeVerificationSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.save()
        return Response({"token":token, "detail":"Código verificado correctamente."})

#Paso3: Cambiar la contraseña con el token temporal
class PasswordChangeView(generics.GenericAPIView):
    serializer_class = PasswordChangeSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": "La contraseña ha sido actualizada correctamente."})
