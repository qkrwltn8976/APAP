from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from . import views

app_name = "main"

urlpatterns = [
	path('home/', views.home, name="home"),
	path('<str:username>/<int:id>', views.detail, name="detail"),
	path('<str:username>/mypage/', views.mypage, name="mypage"),
	path('<str:username>/detail/', views.detail, name="detail"),
	path('<str:username>/upload/', views.upload, name="upload"),
	path('<str:username>/username/<int:id>', views.update, name="update"),
	path('<str:username>/upload/popup', views.popup, name="popup"),
	path('selected_lectures/', views.selected_lectures, name="selected_lectures"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

