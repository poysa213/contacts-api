from rest_framework import generics, permissions, mixins
from .serializers import RegisterSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


# from .serializers import MyTokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView


# class MyObtainTokenPairView(TokenObtainPairView):
#     permission_classes = (AllowAny,)
#     serializer_class = MyTokenObtainPairSerializer


#Register API
class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classess = [AllowAny]
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,    context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })