from django.contrib import admin
from django.urls import path

from . import views

app_name = "main"

urlpatterns = [
	path('<str:username>/', views.home, name="home"),
	path('<str:username>/request', views.request, name="request"),
	path('<str:username>/request/<int:id>', views.detail, name="detail"),
	path('<str:username>/mypage/', views.mypage, name="mypage"),
	path('selected_lectures/', views.selected_lectures, name="selected_lectures"),
] 