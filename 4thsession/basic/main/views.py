from django.shortcuts import redirect, render, get_object_or_404 #객체가 없으면 404에러를 띄운다
from .models import Blog
from django.utils import timezone

# Create your views here.
def showmain(request):
    blogs = Blog.objects.all()
    return render(request, 'main/mainpage.html',{'blogs':blogs})

def first(request):
    return render(request, 'main/first.html')

def second(request):
    return render(request, 'main/second.html')

def detail(request, id):
    blog = get_object_or_404(Blog, pk = id)
    return render(request, 'main/detail.html', {'blog': blog})

def new(request):
    return render(request, 'main/new.html')

def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.pub_date = timezone.now()
    new_blog.body = request.POST['body']
    new_blog.save()
    return redirect('detail', new_blog.id)