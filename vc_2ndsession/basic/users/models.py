from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followings = models.ManyToManyField(
        "self", related_name="followers", symmetrical=False)
    # 팔로우하면 자동으로 팔로잉, 팔로우가 동시에 되는걸 방지하기 위해 symmetrical=False


@receiver(post_save, sender=User)
# sender => receiver에서 지정한 User모델
# post_save가 생성되면 create_user_profile과 save_user_profile이 생성
# 유저가 생성될 때 profile모델도 생성되도록 한다.
def create_user_profile(sender, instance, created, **kwargs):
    # created 새로 가입한 회원인지 전달하는 boolean형태의 데이터
    # **kwargs은 딕셔너리 형태의 데이터를 전달한다.
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
