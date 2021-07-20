from django.shortcuts import redirect, render, get_object_or_404
from main.models import Post
from django.contrib.auth.models import User

# Create your views here.


def mypage(request, id):
    user = get_object_or_404(User, pk=id)
    context = {
        'user': user,
        'posts': Post.objects.filter(writer=user),
        'followings': user.profile.followings.all(),
        'followers': user.profile.followers.all(),
    }
    return render(request, 'users/mypage.html', context)


def follow(request, id):  # 팔로우할 유저의 id 가지고 옴
    user = request.user
    followed_user = get_object_or_404(User, pk=id)
    is_follower = user.profile in followed_user.profile.followers.all()  # 팔로잉 되어있는지 확인하는 변수
    if is_follower:
        user.profile.followings.remove(followed_user.profile)
    else:
        user.profile.followings.add(followed_user.profile)
    return redirect('users:mypage', followed_user.id)
