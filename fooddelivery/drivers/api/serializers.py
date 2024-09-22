from rest_framework import serializers
from drivers.models import Driver
from orders.api.serializers import (
    OrderListSerializer,
    OrderDetailSerializer
)

class DriverCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Driver
        fields = '__all__'

class DriverUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Driver
        fields = '__all__'

class DriverDetailSerializer(serializers.ModelSerializer):
    orders = OrderDetailSerializer(many=True, read_only=True, source='order_set')

    class Meta:
        model = Driver
        fields = ['name','phone_number','email','location','vehicle_model','vehicle_plate','vehicle_color','orders']
  
class DriverListSerializer(serializers.ModelSerializer):
    orders = OrderListSerializer(many=True, read_only=True, source='order_set')

    class Meta:
        model = Driver
        fields = ['name','phone_number','email','location','vehicle_model','vehicle_plate','vehicle_color','orders']