from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)  # 작성자에 대한 일대다관계
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    like_user_set = models.ManyToManyField(
        User, blank=True, related_name='likes_user_set', through='Like')
    unlike_user_set = models.ManyToManyField(
        User, blank=True, related_name='unlikes_user_set', through='unLike')

    def summary(self):
        return self.body[:20]

    @property  # get함수를 더 쉽게 해주는 데코레이터
    def like_count(self):
        return self.like_user_set.count()

    @property
    def unlike_count(self):
        return self.unlike_user_set.count()


class Comment(models.Model):
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('user', 'post'))


class unLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('user', 'post'))
