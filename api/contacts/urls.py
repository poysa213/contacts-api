from rest_framework import routers

from .views import ContactViewset

router = routers.DefaultRouter()

router.register('contacts', ContactViewset, basename='carts-items')

urlpatterns = router.urls