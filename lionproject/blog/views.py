from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
from .forms import BlogForm


#model을 import를 받아오기
# Create your views here.

def home(request):
    blogs = Blog.objects.all()#객체를 만든다.
    return render(request,'home.html',{'blogs':blogs}) #reuqest받아서 home.html에 접근하겠다.,만든객체blogs을 불러와라

def detail(request,id):
    blog = get_object_or_404(Blog, pk = id ) #객체생성=blog의 model을 가져온다,pk를 id로 가져온다.
    return render(request,'detail.html', {'blog':blog})

def new(request):
    form = BlogForm() #입력받는공간(BlogForm)선언
    return render(request, 'new.html', {'form':form})

#redirect=>render대신쓴다. 누르면 넘어가게/redirectvsrender

def create(request):#유효성검사이후에 데베에 저장하는 과정!form이 다해줌
    form = BlogForm(request.POST, request.FILES)#form이라는 객체에 저장할때 POST랑FILES를 같이저장
    if form.is_valid():#form이 유효한지
        new_blog = form.save(commit=False)#유효하면 (완전저장x,commit=false) 임시저장 왜냐면 pub_date같이저장해줘야함
        new_blog.pub_date = timezone.now()#timezone.now()를 통해 현재시간을 저장
        new_blog.save()#완전저장
        return redirect('detail', new_blog.id)#detail로 보내는 redirect
    return redirect('home')#form이 유효하지않으면, 실패한 경우

def edit(request, id): #수정할글의  id 정보필요
    edit_blog = Blog.objects.get(id=id)#model안의 객체들의 id값
    return render(request, 'edit.html', {'edit_blog': edit_blog})

def update(request,id):
    update_blog = Blog()
    update_blog.title = request.POST['title']
    update_blog.writer = request.POST['writer']
    update_blog.body = request.POST['body']
    update_blog.pub_date = timezone.now()
    update_blog.save() #updateblog객체저장
    return redirect('detail',update_blog.id) 

def delete(request, id):
    delete_blog = Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('home')

