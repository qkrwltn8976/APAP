from django.contrib import admin
from django.urls import path

from . import views

app_name = "main"

urlpatterns = [
	path('<str:username>/home', views.home, name="home"),
	path('<str:username>/<int:id>', views.detail, name="detail"),
	path('<str:username>/mypage', views.mypage, name="mypage"),
	path('<str:username>/upload', views.upload, name="upload"),
	path('<str:username>/username/<int:id>', views.update, name="update"),
	path('selected_lectures/<int:id>', views.selected_lectures, name="selected_lectures"),

]