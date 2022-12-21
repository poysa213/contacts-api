from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication

from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import ContactSerializer
from .models import Contact



class ContactViewset(ModelViewSet):

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)
    
    def create(self, request, *args, **kwargs):
        serializer = ContactSerializer(
            data=request.data)
        serializer.is_valid(raise_exception=True)
        contact = serializer.save(owner=self.request.user)
        serializer = ContactSerializer(contact)
        return Response(serializer.data)
    

