from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import include, path
from .views import index
from RestAPI.api import api

# RLs for the browsable API.




urlpatterns = [
    path("api/", api.urls),
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),
    path("",index) #project view
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]