from rest_framework import serializers
from addresses.models import Address

class AddressCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Address
        fields = '__all__'

class AddressUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'

class AddressDetailSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    restaurant = serializers.StringRelatedField()

    class Meta:
        model = Address
        fields = '__all__'
    
    def get_user(self, obj):
        from users.api.serializers import UserDetailSerializer
        return UserDetailSerializer(obj.user).data
    
    def get_restaurant(self, obj):
        from restaurants.api.serializers import RestaurantDetailSerializer
        return RestaurantDetailSerializer(obj.restaurant).data

class AddressListSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    restaurant = serializers.StringRelatedField()

    class Meta:
        model = Address
        fields = '__all__'

    def get_user(self, obj):
        from users.api.serializers import UserListSerializer
        return UserListSerializer(obj.user).data

    def get_restaurant(self, obj):
        from restaurants.api.serializers import RestaurantListSerializer
        return RestaurantListSerializer(obj.restaurant).data