from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_str
from django.core.mail import send_mail
from django.conf import settings
from users.models import User

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    repeat_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id','first_name','last_name','email','password', 'repeat_password' ]

    def validate(self, data):
        if data['password'] != data['repeat_password']:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        return data

    def create(self, validated_data):
        validated_data.pop('repeat_password', None)
        validated_data['password'] = make_password(validated_data['password'])
        return User.objects.create(**validated_data)
    
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name','email']
    
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name','email', 'is_active', 'is_staff']

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name','email', 'is_active', 'is_staff']

#Serializador para solicitar el restablecimiento de contraseña
class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        try:
            user = User.objects.get(email=value)
        except User.DoesNotExist:
            raise serializers.ValidationError("No existe un usuario con este correo electrónico.")
        return value

    def save(self, request):
        email = self.validated_data['email']
        user = User.objects.get(email=email)
        token_generator = PasswordResetTokenGenerator()
        # Convertir user.pk a bytes manualmente usando utf-8
        uid = urlsafe_base64_encode(str(user.pk).encode('utf-8'))
        
        reset_link = f"{request.scheme}://{request.get_host()}/api/password-reset-confirm/{uid}/{token_generator}/"

        # Enviar correo electrónico con el enlace de restablecimiento
        send_mail(
            'Restablecimiento de Contraseña',
            f'Utiliza el siguiente enlace para restablecer tu contraseña: {reset_link}',
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )

class PasswordResetConfirmSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)
    repeat_password = serializers.CharField(write_only=True)
    token = serializers.CharField(write_only=True)
    uid = serializers.CharField(write_only=True)

    def validate(self, data):
        if data['password'] != data['repeat_password']:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        return data

    def save(self):
        uid = self.validated_data['uid']
        token = self.validated_data['token']
        password = self.validated_data['password']

        try:
            uid = force_str(urlsafe_base64_decode(uid))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            raise serializers.ValidationError("El enlace de restablecimiento de contraseña no es válido.")

        token_generator = PasswordResetTokenGenerator()
        if not token_generator.check_token(user, token):
            raise serializers.ValidationError("El token es inválido o ha expirado.")

        user.password = make_password(password)
        user.save()
        return user