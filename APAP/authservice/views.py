from django.shortcuts import render


def signin(request):
	return render(request, 'authservice/signin.html')


def signup(request):
	return render(request, 'authservice/signup.html')

# Create your views here.
