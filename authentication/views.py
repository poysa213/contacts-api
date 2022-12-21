from django.contrib.auth.models import User
from rest_framework import generics, permissions, mixins, status
from .serializers import  RegisterSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


#Register API
class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)
    queryset = User.objects.all()

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({
                "user": UserSerializer(user,context=self.get_serializer_context()).data,
                "message": "User Created Successfully.  Now perform Login to get your token",
            })
        return Response(serializer.data, status=status.HTTP_401_BAD_REQUEST)
