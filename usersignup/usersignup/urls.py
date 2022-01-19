
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('',include('mainapp.urls')),
    path('',include('home.urls'))

]