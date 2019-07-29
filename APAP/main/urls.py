from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
	path('<str:username>/', views.home, name="home"),
	path('<str:username>/<int:id>', views.detail, name="detail"),
	path('<str:username>/mypage', views.mypage, name="mypage"),
	path('<str:username>/upload', views.upload, name="upload"),
	path('<str:username>/upload/popup', views.popup, name="popup"),
] 