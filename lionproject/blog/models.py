from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date= models.DateTimeField()
    body= models.TextField()
    image = models.ImageField(upload_to = "blog/", blank = True, null = True)
    #upload_to는 업로드할 폴더를 지정하는것
    #settings.py에 MEDIA_URL로 지정해둔 media폴더안에 blog폴더를 만들어서 관리하겠다는 설정.


    def __str__(self):  #?뭐지찾아보기
        return self.title
    def summary(self): #글자제한
        return self.body[1:100]
