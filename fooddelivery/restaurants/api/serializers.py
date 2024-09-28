from rest_framework import serializers
from restaurants.models import Restaurant
from orders.api.serializers import (
    OrderListSerializer,
    OrderDetailSerializer
)
from ratings.api.serializers import(
    RatingListSerializer,
    RatingDetailSerializer
)

from addresses.api.serializers import (
    AddressListSerializer,
    AddressDetailSerializer
)

from menus.api.serializers import(
    MenuListSerializer,
    MenuDetailSerializer
)

class RestaurantCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = '__all__'

class RestaurantUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = '__all__'

class RestaurantDetailSerializer(serializers.ModelSerializer):
    orders = OrderDetailSerializer(many=True, read_only=True)
    ratings = RatingDetailSerializer(many=True, read_only=True)
    addresses = AddressDetailSerializer(many=True, read_only=True)
    menu = MenuDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = ['id','name','address','phone_number','orders','ratings','addresses','menu']

class RestaurantListSerializer(serializers.ModelSerializer):
    orders = OrderListSerializer(many=True, read_only=True)
    ratings = RatingListSerializer(many=True, read_only=True)
    addresses = AddressListSerializer(many=True, read_only=True)
    menu = MenuListSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = ['id','name','address','phone_number','orders','ratings','addresses','menu']