from django.urls import path
from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    # 개별 유저 아이디로 마이페이지 접속
    path('<int:id>/mypage/', views.mypage, name="mypage"),
    path('<int:id>/follow/', views.follow, name="follow"),
]
