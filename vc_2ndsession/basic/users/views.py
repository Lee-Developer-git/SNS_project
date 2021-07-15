from django.shortcuts import redirect, render, get_object_or_404
from main.models import Blog
from .models import User

# Create your views here.


def mypage(request, id):
    user = get_object_or_404(User, pk=id)
    context = {
        'user': user,
        # postdetail페이지에서 가져온 user와 일치하는 유저만 filter로 뽑아냄
        'blogs': Blog.objects.filter(writer=user),
        'followings': user.profile.followings.all(),
        'followers': user.profile.followers.all(),
    }
    return render(request, 'users/mypage.html', context)


def follow(request, id):
    user = request.user
    followed_user = get_object_or_404(User, pk=id)  # 현재 요청된 url에 있는 user id불러옴
    is_follower = user.profile in followed_user.profile.followers.all()  # 팔로우된 유저인지 확인
    if is_follower:
        user.profile.followings.remove(followed_user.profile)
    else:
        user.profile.followings.add(followed_user.profile)
    return redirect('users:mypage', followed_user.id)
