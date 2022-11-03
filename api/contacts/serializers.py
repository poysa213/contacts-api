from django.contrib.auth.models import User

from rest_framework import serializers


from .models import Contact

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']
        
class ContactSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer()
    class Meta:
        model = Contact
        fields = ['id', 'owner', 'name', 'email', 'phone_number', 'added_at', 'is_favorite']