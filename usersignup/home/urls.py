
from django.urls import path
from . import views
from django.urls import include, path
from . import views
from django.contrib import admin

urlpatterns = [
    path('signup/',views.signup_view,name = "signup_view"),
    path('login/',views.login_view ,name = "login_view"),

]