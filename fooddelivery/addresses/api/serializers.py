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

    class Meta:
        model = Address
        fields = '__all__'
    
    def get_user(self, obj):
        from users.api.serializers import UserDetailSerializer
        return UserDetailSerializer(obj.user).data

class AddressListSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Address
        fields = '__all__'

    def get_user(self, obj):
        from users.api.serializers import UserListSerializer
        return UserListSerializer(obj.user).data