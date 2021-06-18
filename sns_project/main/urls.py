from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path('', showmain, name="main"),
    path('info/', showinfo, name="info"),
    path('post/', showpost, name="post"),
    path('<str:id>', postdetail, name="postDetail"),
    path('postCreate/', postCreate, name="postCreate"),
    path('create/', create, name="create"),
    path('postEdit/<str:id>', postEdit, name="postEdit"),
    path('update/<str:id>', update, name="update"),
    path('delete/<str:id>', delete, name="delete"),
]