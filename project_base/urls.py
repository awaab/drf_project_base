from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('user_api.urls')),
    path('auth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
