from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
	path('<str:username>/', views.home, name="home"),
	path('<str:username>/request', views.request, name="request"),
	path('<str:username>/request/<int:id>', views.detail, name="detail"),
	path('<str:username>/mypage', views.mypage, name="mypage"),
] 