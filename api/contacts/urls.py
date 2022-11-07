from django.urls import path, include

from rest_framework import routers


from .views import ContactViewset

router = routers.DefaultRouter()

router.register('', ContactViewset, basename='carts-items')


urlpatterns = [
    path('', include(router.urls)),
]

