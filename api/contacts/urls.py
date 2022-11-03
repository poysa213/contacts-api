from django.urls import path, include

from rest_framework import routers

from knox import views as knox_views

from .views import ContactViewset

router = routers.DefaultRouter()

router.register('contacts', ContactViewset, basename='carts-items')


urlpatterns = [
    path(r'auth/', include('knox.urls'))

]


urlpatterns += router.urls