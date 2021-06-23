from django.shortcuts import render, get_object_or_404, redirect #
from .models import Posting
from django.utils import timezone
# Create your views here.
def home(request):
    postings = Posting.objects.all()
    return render(request,'home.html',{'postings':postings})

def detail(request,id):
    posting = get_object_or_404( Posting , pk=id)#pk값이 id인 posting의 값을 가져오거나 에러를 띄워라, object하나만을 가져옴
    return render(request, 'detail.html',{'posting':posting} )

def new(request):
    return render(request,'new.html')#새로운 파일 생성하는 양식나오기

def create(request):
    new_posting = Posting() 
    new_posting.title = request.POST['title']
    new_posting.body = request.POST['body']
    new_posting.pub_date = timezone.now()
    new_posting.save()
    return redirect('detail', new_posting.id)

def edit(request,id):
    edit_posting = Posting.objects.get(id= id)
    return render(request, 'edit.html',{'posting':edit_posting})

def update(request, id):
    update_posting = Posting.objects.get(id=id)
    update_posting.title=request.POST['title']
    update_posting.body=request.POST['body']
    update_posting.pub_date = timezone.now()
    update_posting.save()
    return redirect('detail',update_posting.id)

def feed_create(request):
    new_feed = Posting() 
    new_feed.title = request.POST['title']
    new_feed.body = request.POST['body']
    new_feed.pub_date = timezone.now()
    new_feed.save()
    return redirect('detail', new_feed.id)

def feed(request,id):
    feed = Posting.objects.get(id=id)
    return render(request, 'feed.html',{'feed':feed})

def profile(request):
    profiles = Posting.objects.all()
    return render(request, 'profile.html',{'profiles': profiles})

def delete(request, id): #안써도 request매개변수로 필요함
    delete_posting = Posting.objects.get(id=id)
    delete_posting.delete()
    return redirect('home')