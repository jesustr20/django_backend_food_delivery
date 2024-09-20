from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from addresses.models import Address
from addresses.api.serializers import (
    AddressCreateSerializer,
    AddressDetailSerializer,
    AddressUpdateSerializer,
    AddressListSerializer
)

class AddressCreateView(generics.CreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressCreateSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class AddressListView(generics.ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressListSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

class AddressDetailView(generics.RetrieveAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressDetailSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class AddressUpdateView(generics.UpdateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressUpdateSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class AddressDeleteView(generics.DestroyAPIView):
    queryset = Address.objects.all()
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]