from rest_framework import serializers
from ratings.models import Rating
from django.contrib.contenttypes.models import ContentType

class RatingCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = '__all__'

class RatingUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = '__all__'

class RatingDetailSerializer(serializers.ModelSerializer):
    
    content_object = serializers.SerializerMethodField()

    class Meta:
        model = Rating
        fields = '__all__'
    
    def get_content_object(self, obj):
        content_object = obj.content_object

        if isinstance(content_object, Restaurant):
            from restaurants.models import Restaurant
            from restaurants.api.serializers import RestaurantDetailSerializer
            return RestaurantDetailSerializer(content_object).data
        elif isinstance(content_object, User):
            from users.models import User
            from users.api.serializers import UserDetailSerializer
            return UserDetailSerializer(content_object).data
        else:
            return None

class RatingListSerializer(serializers.ModelSerializer):
    
    content_object = serializers.SerializerMethodField()

    class Meta:
        model = Rating
        fields = '__all__'
    
    def get_content_object(self, obj):
        content_object = obj.content_object

        if isinstance(content_object, Restaurant):
            from restaurants.models import Restaurant
            from restaurants.api.serializers import RestaurantDetailSerializer
            return RestaurantDetailSerializer(content_object).data
        elif isinstance(content_object, User):
            from users.models import User
            from users.api.serializers import UserDetailSerializer
            return UserDetailSerializer(content_object).data
        else:
            return None