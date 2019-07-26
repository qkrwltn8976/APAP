from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
	path('home/', views.home, name="home"),
	path('<username>/request', views.request, name="request"),
	path('<username>/request/<int:id>', views.detail, name="detail"),
	path('<username>/mypage', views.mypage, name="mypage"),
] 