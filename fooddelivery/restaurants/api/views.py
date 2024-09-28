from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from restaurants.models import Restaurant
from restaurants.api.serializers import(
    RestaurantCreateSerializer,
    RestaurantListSerializer,
    RestaurantDetailSerializer,
    RestaurantUpdateSerializer
)

class RestaurantCreateView(generics.CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantCreateSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class RestaurantListView(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class RestaurantDetailView(generics.RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantDetailSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class RestaurantUpdateView(generics.UpdateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantUpdateSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class RestaurantDeleteView(generics.DestroyAPIView):
    queryset = Restaurant.objects.all()    
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]