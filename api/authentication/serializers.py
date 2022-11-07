from rest_framework import serializers
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User

from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(max_length=100, min_length=4)
    first_name = serializers.CharField(max_length=50, min_length=2)
    last_name = serializers.CharField(max_length=50, min_length=2)

    class Meta:
        model = User
        fields = ['id','username', 'first_name', 'last_name', 'email', 'password']
       
   

    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': ('Email is already in use')})
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)

     
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password','first_name', 'last_name')
        extra_kwargs = {
            'password':{'write_only': True},
        }

    def create(self, validated_data):
        user = User(
        email=validated_data['email'],
        username=validated_data['username'],
        password=make_password(validated_data['password'])
             )
        # user.set_password(make_password(validated_data['password']))
        user.save()
        return user






# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

#     @classmethod
#     def get_token(cls, user):
#         token = super(MyTokenObtainPairSerializer, cls).get_token(user)

#         # Add custom claims
#         token['username'] = user.username
#         return token