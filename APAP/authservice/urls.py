from django.contrib import admin
from django.urls import path

from . import views

app_name = "authservice"

urlpatterns = [
	path('', views.signin, name="signin"),
	path('register/', views.register, name="register"),
	path('signup/', views.signup, name="signup"),
	path('login/', views.login, name="login"),
	path('logout/', views.logout, name='logout'),
]  
