from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from drivers.models import Driver
from drivers.api.serializers import(
    DriverCreateSerializer,
    DriverListSerializer,
    DriverDetailSerializer,
    DriverUpdateSerializer,
)

class DriverCreateView(generics.CreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverCreateSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class DriverListView(generics.ListAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverListSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

class DriverDetailView(generics.RetrieveAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverDetailSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class DriverUpdateView(generics.UpdateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverUpdateSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class DriverDeleteView(generics.DestroyAPIView):
    queryset = Driver.objects.all()    
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]