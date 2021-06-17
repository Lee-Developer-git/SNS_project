from django.shortcuts import redirect, render, get_object_or_404
from .models import Post
from django.utils import timezone

def showmain(request):
    return render(request, 'main/show_main.html')

def showinfo(request):
    return render(request, 'main/show_info.html')

# get post
def showpost(request):
    posts = Post.objects.all()
    return render(request, 'main/show_post.html', {'posts': posts})

def postdetail(request, id):
    posts = Post.objects.all()
    post = get_object_or_404(Post, pk = id)
    return render(request, 'main/postDetail.html', {'post':post, 'posts': posts})

# create post
def postCreate(request):
    return render(request, 'main/postCreate.html')

def create(request):
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.writer = request.POST['writer']
    new_post.pub_date = timezone.now()
    new_post.body = request.POST['body']
    new_post.image = request.FILES['image']
    new_post.save()
    return redirect('main:postDetail', new_post.id)

# update post
def postEdit(request, id):
    edit_post = Post.objects.get(id = id) # 포스트 id 값대로 불러옴
    return render(request, 'main/postEdit.html', {'post': edit_post})

def update(request, id):
    update_post = Post.objects.get(id = id)
    update_post.title = request.POST['title']
    update_post.writer = request.POST['writer']
    update_post.pub_date = timezone.now()
    update_post.body = request.POST['body']
    update_post.save()
    return redirect('main:postDetail', update_post.id)

def delete(request, id):
    delete_post = Post.objects.get(id = id)
    delete_post.delete()
    return redirect('main:post')