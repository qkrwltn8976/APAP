from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
	path('<username>', views.home, name="home"),
	path('<username>/upload', views.upload, name="upload"),
	path('<username>/upload/popup', views.popup, name="popup"),
	path('<username>/request/<int:id>', views.detail, name="detail"),
	path('<username>/mypage', views.mypage, name="mypage"),
] 