from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from . import views

app_name = "main"

urlpatterns = [
   path('home/', views.home, name="home"),
   path('home/details/<int:id>', views.detail, name="detail"),
   path('<str:username>/mypage/', views.mypage, name="mypage"),
   path('<str:username>/upload/', views.upload, name="upload"),
   path('update/<int:id>', views.update, name="update"),
   path('delete/<int:id>', views.delete, name = "delete"),
   path('selected_lectures/', views.selected_lectures, name="selected_lectures"),
   path('endtimer/', views.endtimer, name="endtimer"),
   path('filter/', views.filter, name="filter"),
   path('requests/<int:id>', views.requests, name="requests"),
   path('test/', views.test, name="test"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)