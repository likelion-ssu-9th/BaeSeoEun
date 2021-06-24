"""instagram URL Configuration

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
from posting.views import *
from account.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('<str:id>',detail,name="detail"),#str은 자료형, id= 매개변수로 지정한 이름
    # path('posting/',include('posting.urls')),
    path('account/',include('account.urls')),
    path('new/', new , name = "new" ),
    path('create/', create, name= "create"),
    path('edit/<str:id>', edit, name="edit"),
    path('update/<str:id>',update,name="update"),
    path('feed_create/',feed_create,name="feed_create"),
    path('feed/<str:id>',feed,name="feed"),
    path('profile/',profile, name="profile"),
    path('delete/<str:id>', delete , name="delete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
