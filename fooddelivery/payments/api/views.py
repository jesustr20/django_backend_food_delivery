from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from payments.models import Payment
from payments.api.serializers import(
    PaymentCreateSerializer,
    PaymentListSerializer,
    PaymentDetailSerializer,
    PaymentUpdateSerializer
)

class PaymentCreateView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentCreateSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class PaymentListView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentListSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class PaymentDetailView(generics.RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentDetailSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class PaymentUpdateView(generics.UpdateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentUpdateSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class PaymentDeleteView(generics.DestroyAPIView):
    queryset = Payment.objects.all()    
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]