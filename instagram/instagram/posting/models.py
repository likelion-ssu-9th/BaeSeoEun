from django.db import models

# Create your models here.
class Posting(models.Model):
    
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="posting/",blank=True, null=True)
    
    def __str__(self) : #class 호출될떄 나오는 이름표같은 녀석
        return self.title
    def summary(self):
        return self.body[:50]
