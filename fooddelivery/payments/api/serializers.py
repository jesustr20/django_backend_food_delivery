from rest_framework import serializers
from payments.models import Payment

class PaymentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'

class PaymentUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'

class PaymentDetailSerializer(serializers.ModelSerializer):
    order = serializers.StringRelatedField()

    class Meta:
        model = Payment
        fields = '__all__'
    
    def get_order(self, obj):
        from orders.api.serializers import OrderDetailSerializer
        return OrderDetailSerializer(obj.order).data

class PaymentListSerializer(serializers.ModelSerializer):
    order = serializers.StringRelatedField()

    class Meta:
        model = Payment
        fields = '__all__'
    
    def get_order(self, obj):
        from orders.api.serializers import OrderDetailSerializer
        return OrderDetailSerializer(obj.order).data