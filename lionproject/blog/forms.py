from django import forms #장고가 제공해주는 폼사용
from .models import Blog #Blog의 models.py사용

class BlogForm(forms.ModelForm):#둘다 내장된거,폼이름정의
    class Meta:#폼클래스안에 메타클래스정의 
        model = Blog #모델을 블로그라고 하고
        fields=['title','writer','body','image']#pub_date는 폼을 받으면안된다(자동으로생성해야함)./ 생성한폼을 제공하는기능
        #https://wayhome25.github.io/django/2017/05/06/django-form/
        