from django.shortcuts import render


def signin(request):
	return render(request, 'authservice/signin.html')


def signup(request):
	return render(request, 'authservice/signup.html')


def index(request):
	return render(request, 'index.html')

# Create your views here.
