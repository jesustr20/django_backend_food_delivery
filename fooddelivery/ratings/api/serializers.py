from rest_framework import serializers
from ratings.models import Rating

class RatingCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = '__all__'

class RatingUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = '__all__'

class RatingDetailSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    restaurant = serializers.StringRelatedField()

    class Meta:
        model = Rating
        fields = '__all__'
    
    def get_user(self, obj):
        from users.api.serializers import UserDetailSerializer
        return UserDetailSerializer(obj.user).data
    
    def get_restaurant(self, obj):
        from restaurants.api.serializers import RestaurantDetailSerializer
        return RestaurantDetailSerializer(obj.restaurant).data

class RatingListSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    restaurant = serializers.StringRelatedField()

    class Meta:
        model = Rating
        fields = '__all__'
    
    def get_user(self, obj):
        from users.api.serializers import UserListSerializer
        return UserListSerializer(obj.user).data
    
    def get_restaurant(self, obj):
        from restaurants.api.serializers import RestaurantListSerializer
        return RestaurantListSerializer(obj.restaurant).data