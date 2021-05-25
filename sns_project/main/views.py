from django.shortcuts import redirect, render, get_object_or_404
from .models import Post
from django.utils import timezone

# Create your views here.
def showmain(request):
    return render(request, 'main/show_main.html')

def showinfo(request):
    return render(request, 'main/show_info.html')

def showpost(request):
    posts = Post.objects.all()
    return render(request, 'main/show_post.html', {'posts': posts})

def postdetail(request, id):
    posts = Post.objects.all()
    post = get_object_or_404(Post, pk = id)
    return render(request, 'main/postDetail.html', {'post':post, 'posts': posts})

def postCreate(request):
    return render(request, 'main/postCreate.html')

def create(request):
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.writer = request.POST['writer']
    new_post.pub_date = timezone.now()
    new_post.body = request.POST['body']
    new_post.save()
    return redirect('postDetail', new_post.id)