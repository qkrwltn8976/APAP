from django.shortcuts import render


def home(request, username):
	return render(request, 'main/home.html')


def request(request, username):
	return render(request, 'main/request.html')


def detail(request, username, id):
	return render(request, 'main/detail.html')


def mypage(request, username):
	return render(request, 'main/mypage.html')
# Create your views here.
