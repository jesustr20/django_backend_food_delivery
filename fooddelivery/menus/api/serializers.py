from rest_framework import serializers
from menus.models import Menu

class MenuCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = '__all__'

class MenuUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = '__all__'

class MenuDetailSerializer(serializers.ModelSerializer):
    restaurant = serializers.StringRelatedField()
    
    class Meta:
        model = Menu
        fields = ['id','name','description','restaurant']
    
    def get_restaurant(self, obj):
        from restaurants.api.serializers import RestaurantDetailSerializer
        return RestaurantDetailSerializer(obj.restaurant).data

class MenuListSerializer(serializers.ModelSerializer):
    restaurant = serializers.StringRelatedField()

    class Meta:
        model = Menu
        fields = ['id','name','description','restaurant']
    
    def get_restaurant(self, obj):
        from restaurants.api.serializers import RestaurantListSerializer
        return RestaurantListSerializer(obj.restaurant).data