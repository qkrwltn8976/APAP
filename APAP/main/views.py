from django.shortcuts import render, redirect, get_object_or_404
from models.models import *
from django.core.mail import send_mail

def home(request, username):
	user = get_object_or_404(User, pk=2) #로그인 구현 전 임시 설정
	#user = request.user
	username = user.username
	return render(request, 'main/home.html')
	
	# if user.verified == True: #인증을 한 유저인 경우 
	# 	return render(request, 'main/home.html')
	# else: #인증하지 않은 유저인 경우
	# 	# email = 'original@here.com'
	# 	# user = User.objects.create_user(email, email=email)
	# 	# user.is_confirmed # False

	# 	# send_mail(email, 'Use %s to confirm your email' % user.password, email, [email])
	# 	# # User gets email, passes the confirmation_key back to your server

	# 	# user.confirm_email(user.password)
	# 	# user.is_confirmed # True
	# 	return render(request, 'main/verify.html')



def upload(request, username):
	return render(request, 'main/upload.html')


def popup(request, username):
    	return render(request, 'main/popup.html')



def detail(request, username, id):
	return render(request, 'main/detail.html')


def mypage(request, username):
	user = get_object_or_404(User, pk=2) #로그인 구현 전 임시 설정
	#user = request.user
	username = user.username

	# if user.verified == True:
	# 	#
	# else:
	# 	#

	return render(request, 'main/mypage.html')
# Create your views here.
