from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone

#model을 import를 받아오기
# Create your views here.

def home(request):
    blogs = Blog.objects.all()#객체를 만든다.
    return render(request,'home.html',{'blogs':blogs}) #reuqest받아서 home.html에 접근하겠다.,만든객체blogs을 불러와라
def detail(request,id):
    blog = get_object_or_404(Blog, pk = id ) #객체생성=blog의 model을 가져온다,pk를 id로 가져온다.
    return render(request,'detail.html',{'blog':blog})
def new(request):
    return render(request, 'new.html')
def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.body = request.POST['body']
    new_blog.pub_date = timezone.now()
    new_blog.image = request.FILES['image']#폼데이터로 받아온 파일=('image')을 newblog의 이미지에 저장하기
    new_blog.save() #저장
    return redirect('detail',new_blog.id)#render대신쓴다. 누르면 넘어가게/redirectvsrender

# def create(request):
#     form = BlogForm(request.POST, request.FILES)
#     if form.is_valid():
#         new_blog = form.save(commit=False)
#         new_blog.pub_date = timezone.now()
#         new_blog.save()
#         return redirect('detail', new_blog.id)
#     return redirect('home')

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

