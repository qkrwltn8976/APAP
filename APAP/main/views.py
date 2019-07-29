from django.shortcuts import render


def home(request, username):
	return render(request, 'main/home.html')


def upload(request, username):
	return render(request, 'main/upload.html')


def popup(request, username):
    	return render(request, 'main/popup.html')



def detail(request, username, id):
	return render(request, 'main/detail.html')


def mypage(request, username):
	return render(request, 'main/mypage.html')
# Create your views here.
