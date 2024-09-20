from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from ratings.models import Rating
from ratings.api.serializers import (
    RatingCreateSerializer,
    RatingListSerializer,
    RatingDetailSerializer,
    RatingUpdateSerializer
)

class RatingCreateView(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingCreateSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class RatingListView(generics.ListAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingListSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

class RatingDetailView(generics.RetrieveAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingDetailSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class RatingUpdateView(generics.UpdateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingUpdateSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class RatingDeleteView(generics.DestroyAPIView):
    queryset = Rating.objects.all()    
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]