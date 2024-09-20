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

    class Meta:
        model = Rating
        fields = '__all__'
    
    def get_user(self, obj):
        from users.api.serializers import UserDetailSerializer
        return UserDetailSerializer(obj.user).data

class RatingListSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Rating
        fields = '__all__'
    
    def get_user(self, obj):
        from users.api.serializers import UserListSerializer
        return UserListSerializer(obj.user).data