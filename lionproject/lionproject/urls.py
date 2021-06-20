"""lionproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from blog.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home , name = "home"),#path이름은 home
    path('blog/',include('blog.urls')),#blog.urls로이동
    path('account/',include('account.urls')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)#개발할때마다 복붙하기#이게뭔지는 공식문서가서확인


#url 1번,부모url