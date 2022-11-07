from django.contrib.auth import get_user_model



from rest_framework import serializers


from .models import Contact

User = get_user_model()

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']

class ContactSerializer(serializers.ModelSerializer):
#     owner = OwnerSerializer()
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'phone_number', 'location', 'added_at', 'is_favorite']