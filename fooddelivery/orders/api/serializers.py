from rest_framework import serializers
from orders.models import Order
from payments.api.serializers import(
    PaymentListSerializer,
    PaymentDetailSerializer
)

class OrderCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'

class OrderUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'

class OrderDetailSerializer(serializers.ModelSerializer):
    payment = PaymentDetailSerializer(many=True, read_only=True)

    user = serializers.StringRelatedField()
    driver = serializers.StringRelatedField()
    restaurant = serializers.StringRelatedField()

    class Meta:
        model = Order
        fields = ['id','status','order_total','delivery_status','created_at','updated_at','user','driver','payment','restaurant']

    def get_user(self, obj):
        from users.api.serializers import UserDetailSerializer
        return UserDetailSerializer(obj.user).data
    
    def get_driver(self, obj):
        from drivers.api.serializers import DriverDetailSerializer
        return DriverDetailSerializer(obj.driver).data
    
    def get_restaurant(self, obj):
        from restaurants.api.serializers import RestaurantDetailSerializer
        return RestaurantDetailSerializer(obj.restaurant).data

class OrderListSerializer(serializers.ModelSerializer):
    payment = PaymentListSerializer(many=True, read_only=True)

    user = serializers.StringRelatedField()
    driver = serializers.StringRelatedField()
    restaurant = serializers.StringRelatedField()

    class Meta:
        model = Order
        fields = ['id','status','order_total','delivery_status','created_at','updated_at','user','driver','payment','restaurant']
    
    def get_user(self, obj):
        from users.api.serializers import UserListSerializer
        return UserListSerializer(obj.user).data
    
    def get_driver(self, obj):
        from drivers.api.serializers import DriverListSerializer
        return DriverListSerializer(obj.driver).data
    
    def get_restaurant(self, obj):
        from restaurants.api.serializers import RestaurantListSerializer
        return RestaurantListSerializer(obj.restaurant).data