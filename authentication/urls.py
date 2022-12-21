from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView, TokenObtainPairView

from django.urls import path

from .views import RegisterView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('register/', RegisterView.as_view(), name='sign_up'),
]
