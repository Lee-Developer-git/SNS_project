from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(User, on_delete=models.CASCADE) # 일대다관계로 수정
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="blog/", blank=True, null=True) # null값을 가질 수 있음

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:10]