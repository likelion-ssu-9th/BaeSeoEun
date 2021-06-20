from django.contrib import admin
from django.urls import path, include
from account.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('register/',register_view, name="signup"),
]
