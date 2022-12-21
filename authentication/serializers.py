from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.validators import UniqueValidator
from rest_framework import serializers

# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(max_length=100, min_length=6, write_only=True)
#     email = serializers.EmailField(max_length=255, min_length=4)
#     first_name = serializers.CharField(max_length=50, min_length=2)
#     last_name = serializers.CharField(max_length=50, min_length=2)

#     class Meta:
#         model = User
#         fields = ['id','username', 'first_name', 'last_name', 'email', 'password']
       
   
#     def validate(self, attrs):
#         email = attrs.get('email', '')
#         if User.objects.filter(email=email).exists():
#             raise serializers.ValidationError(
#                 {'email': ('Email is already in use')})
#         return super().validate(attrs)

#     def create(self, validated_data):
#         return User.objects.create_user(**validated_data)
        
# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        # extra_kwargs = {'password': {'write_only': True}}


    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': ('Email is already in use')})
        return super().validate(attrs)

    def create(self, validated_data):
        password_data = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password_data)
        user.save()
        return user
    # def create(self, validated_data):
    #     user = User.objects.create(email=validated_data['email'],
    #                                    name=validated_data['name']
    #                                      )
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user