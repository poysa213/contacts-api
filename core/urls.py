from django.contrib import admin
from django.urls import path, include
from rest_framework.exceptions import server_error


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/contacts/', include('contacts.urls')),
    path('api/auth/', include('authentication.urls')),
]


handler404 = 'contacts.views.handler404'
handler500 = 'contacts.views.handler500'
