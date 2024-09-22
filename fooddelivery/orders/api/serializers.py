from rest_framework import serializers
from orders.models import Order

class OrderCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'

class OrderUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'

class OrderDetailSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    driver = serializers.StringRelatedField()

    class Meta:
        model = Order
        fields = '__all__'

    def get_user(self, obj):
        from users.api.serializers import UserDetailSerializer
        return UserDetailSerializer(obj.user).data
    
    def get_driver(self, obj):
        from drivers.api.serializers import DriverDetailSerializer
        return DriverDetailSerializer(obj.driver).data

class OrderListSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    driver = serializers.StringRelatedField()

    class Meta:
        model = Order
        fields = '__all__'
    
    def get_user(self, obj):
        from users.api.serializers import UserListSerializer
        return UserListSerializer(obj.user).data
    
    def get_driver(self, obj):
        from drivers.api.serializers import DriverListSerializer
        return DriverListSerializer(obj.driver).data