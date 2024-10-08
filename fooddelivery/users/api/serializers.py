import random
from django.utils import timezone
from datetime import timedelta
from rest_framework import serializers
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.conf import settings
from users.models import User, PasswordResetCode
from django.utils.text import slugify
from addresses.api.serializers import (
    AddressListSerializer,
    AddressDetailSerializer
    )
from ratings.api.serializers import(
    RatingListSerializer,
    RatingDetailSerializer
)
from orders.api.serializers import (
    OrderListSerializer,
    OrderDetailSerializer
)

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    repeat_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id','first_name','last_name','email','password', 'repeat_password']

    def validate(self, data):
        if data['password'] != data['repeat_password']:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        return data

    def create(self, validated_data):
        validated_data.pop('repeat_password', None)
        validated_data['password'] = make_password(validated_data['password'])

        if not validated_data.get('username'):
            validated_data['username'] = slugify(validated_data['email'].split('@')[0])

            base_username = validated_data['username']
            counter = 1
            while User.objects.filter(username=validated_data['username']).exists():
                validated_data['username'] = f"{base_username}{counter}"
                counter += 1
        return User.objects.create(**validated_data)
    
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name','email', 'phone_number','biography','type_user']
    
class UserDetailSerializer(serializers.ModelSerializer):
    addresses = AddressDetailSerializer(many=True, read_only=True)
    ratings = RatingDetailSerializer(many=True, read_only=True)
    orders = OrderDetailSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name','email', 'phone_number','biography','type_user','is_active', 'is_staff','addresses','ratings','orders']

class UserListSerializer(serializers.ModelSerializer):
    addresses = AddressListSerializer(many=True, read_only=True)
    ratings = RatingListSerializer(many=True, read_only=True)
    orders = OrderListSerializer(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name','email', 'phone_number','biography','type_user','is_active', 'is_staff','addresses','ratings','orders']

#Serializador para solicitar el restablecimiento de contraseña
class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        try:
            User.objects.get(email=value)
        except User.DoesNotExist:
            raise serializers.ValidationError("No existe un usuario con este correo electrónico.")
        return value

    def save(self):
        email = self.validated_data['email']
        code = str(random.randint(1000,9999))        
        
        # Establece el tiempo de expiracion (ej: 10 minutos)
        expiration_time = timezone.now() + timedelta(minutes=10)
        
        # Guardar el codigo en la base de datos
        PasswordResetCode.objects.create(email=email, code=code, expires_at=expiration_time)

        # Enviar correo electrónico con el enlace de restablecimiento
        send_mail(
            'Código de Verificación FoodDelivery',
            f'El código para restablecer tu contraseña es: {code}',
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )

class CodeVerificationSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=4)

    def validate_code(self, value):

        try:
            reset_code = PasswordResetCode.objects.get(code=value)
            if not reset_code.is_valid():
                raise serializers.ValidationError("El código ha expirado.")
        except PasswordResetCode.DoesNotExist:
            raise serializers.ValidationError("Código inválido o correo incorrecto")
        return value
    
    def save(self):
        code = self.validated_data['code']
        reset_code = PasswordResetCode.objects.get(code=code)

        try:
            user = User.objects.get(email=reset_code.email)
        except User.DoesNotExist:
            raise serializers.ValidationError("Usuario no encontrado")

        #Genera un token jwt temporal
        token=AccessToken.for_user(user)
        token['email'] = reset_code.email

        return str(token)

class PasswordChangeSerializer(serializers.Serializer):
    token = serializers.CharField()
    password = serializers.CharField(write_only=True)
    repeat_password = serializers.CharField(write_only=True)

    def validate(self, data):
        if data['password'] != data['repeat_password']:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        return data

    def save(self):
        token = self.validated_data['token']
        password = self.validated_data['password']

        #Decodificar el token
        try:
            access_token = AccessToken(token)
            email = access_token['email']
        except Exception:
            raise serializers.ValidationError("Token inválido o expirado.")
        
        #Cambiar la contraseña
        try:
            user = User.objects.get(email=email)
            user.password = make_password(password)
            user.save()
        except User.DoesNotExist:
            raise serializers.ValidationError("Usuario no encontrado")