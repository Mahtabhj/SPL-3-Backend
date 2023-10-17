from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from wafrauth import urls as auth_urls
from wafrcloudaccount import urls as cloud_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(auth_urls)),
    path('api/', include(cloud_urls)),
]
