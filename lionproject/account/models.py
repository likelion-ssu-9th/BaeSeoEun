from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
#기존에 제공되는 모델을 사용할것이기 떄문에 여기는 건들지않는다.
class CustomUser(AbstractUser):#AbstractUser를 상속받는다. (setting.py에 이 모델을 사용하겠다는 설정해줘야함!)
    nickname = models.CharField(max_length=100)
    university = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
