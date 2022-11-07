from rest_framework import serializers
from .models import User



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(max_length=100, min_length=4),
    first_name = serializers.CharField(max_length=50, min_length=2)
    last_name = serializers.CharField(max_length=50, min_length=2)
    phone_number = serializers.CharField(max_length=50, min_length=6)

    class Meta:
        model = User
        fields = ['id', 'phone_number', 'first_name', 'last_name', 'email', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': ('Email is already in use')})
        phone_number = attrs.get('phone_number', '')
        if User.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError(
                {'email': ('phone_number is already in use')})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','phone_number','password','first_name', 'last_name')
        extra_kwargs = {
            'password':{'write_only': True},
        }