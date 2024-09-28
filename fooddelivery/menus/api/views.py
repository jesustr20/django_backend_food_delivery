from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from menus.models import Menu

class MenuCreateView(generics.CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = ...
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class MenuListView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = ...
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class MenuDetailView(generics.RetrieveAPIView):
    queryset = Menu.objects.all()
    serializer_class = ...
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class MenuUpdateView(generics.UpdateAPIView):
    queryset = Menu.objects.all()
    serializer_class = ...
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class MenuDeleteView(generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = ...
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]