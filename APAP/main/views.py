from django.shortcuts import render, redirect, get_object_or_404
from models.models import *
from django.core.mail import send_mail
from .forms import Printform
import time, math
from media.pdf_page_counter import *
from django.conf import settings

def home(request):
	user = request.user #로그인 구현 전 임시 설정
	id = user.pk
	username = user.username
	lecture_pks = user.lectures.all()
	lecture_list = Lecture.objects.filter(pk__in=lecture_pks)
	prints = Print.objects.filter(
		schedule__lecture__in=[l for l in lecture_list]
	).filter(
		valid=True
	)

	for l in lecture_list:
		print("=========="+l.name)

	timer = ""
	while timer:
		mins, secs = divmod(t, 60)
		timeformat = '{:02d}:{:02d}'.format(mins, secs)
		print(timeformat, end='\r')
		timer.sleep(1)
		timer -= 1

	return render(request, 'main/home.html', {'prints' : prints, 'timer' : timer})


def endtimer(request):
	user = request.user
	if request.method == "POST":
		id = request.POST.get('valid')
		obj = get_object_or_404(Print, pk=id)
		obj.valid = False
		rprint = PrintRequest.objects.filter(
			req_p = obj
		).update(
			point =  obj.print_price + obj.delivery_price / user.requests.count()
		)
		obj.save()
		print("신청이 만료되었습니다")
	return redirect('main:home') 


def upload(request, username):
	user = request.user #로그인 구현 전 임시 설정
	username = user.username

	form = Printform(request.user, request.POST, request.FILES or None)
	if request.method == "POST":
		if form.is_valid():
			form = form.save(commit=False) # form을 당장 저장하지 않음. 데이터 저장 전 뭔가 하고 싶을 때 사용.
			form.uploader = request.user
			form.save()
			# 인쇄비 계산 
			form.pages = pagecounter(form.file.path)
			if(form.color=="colorful"):
				color_price = 200
			else:
				color_price = 40
			form.print_price = math.ceil(form.pages/form.gather)*color_price
			form.save()
		  
			return redirect('main:home')
	else:
		form = Printform(request.user, request.POST)
	return render(request, 'main/upload.html', {'form' : form})

def test(request):
	printobj = get_object_or_404(Print, pk=14)
	print(printobj.file.path)
	cnt = pagecounter(printobj.file.path)
	print("~~~~~~~~~~"+str(cnt))
	return redirect('main:upload', username=request.user.username)

def selected_lectures(request):

	user = request.user #로그인 구현 전 임시 설정

	username = user.username
	if request.method == 'POST':
		lectures_id = request.POST.getlist('lectures') #시간표 id 받아오는 리스트
		for id in lectures_id:
			lecture = get_object_or_404(Lecture, pk=id)
			Schedule.objects.create(user=user, lecture=lecture)
	return redirect('main:mypage', username = user)


def mypage(request, username):

	user = request.user #로그인 구현 전 임시 설정

	username = user.username
	lectures = Lecture.objects.all()
	schedule = Schedule.objects.filter(
		user = user
	)

	prints = Print.objects.filter(
		uploader = user
	)
	pprints = Print.objects.filter(
		requests = user
	)
	#print("====="+str(schedule.count()))
	return render(request, 'main/mypage.html', {'user' : user, 'lectures' : lectures, 'schedule' : schedule, 'prints' : prints, 'pprints' : pprints})

def detail(request, id):
	pprint = get_object_or_404(Print, pk=id)
	user = request.user #로그인 구현 전 임시 설정
	id = user.pk

	if user == pprint.uploader:
		valid = True
		print("일치")
	else:
		valid = False
		print("불일치")

	username = user.username
	lectures = Lecture.objects.all()
	rprint = PrintRequest.objects.filter(
		req_p = pprint
	)
	cnt = pprint.requests.count()
	return render(request, 'main/detail.html', {'user' : user, 'lectures' : lectures, 'print': pprint, 'valid': valid, 'cnt':cnt, 'rprint' : rprint})


def update(request, id):
	pprint = get_object_or_404(Print, pk=id)
	form = Printform(request.user, request.POST or None, request.FILES or None, instance=pprint)
	
	if form.is_valid():
		form.save()
		return redirect('main:home')
	return render(request, 'main/update.html', {"pprint": pprint, "form":form})


def delete(request, id):
	pprint = get_object_or_404(Print, pk=id)
	pprint.delete()
	return redirect('main:home')


def requests(request, id):
	if request.user.is_active:
		user = request.user
		pprint = get_object_or_404(Print, pk=id)

		request_print = user.requests.filter(pk=id)
		request_print_model = PrintRequest.objects.filter(from_user=user, req_p=pprint)
		if request_print_model.exists():
			user.requests.remove(pprint)
			request_print_model.delete()
			print("=======취소=======")

		else:
			user.requests.add(pprint)
			request = PrintRequest.objects.create(from_user=user, to_user=pprint.uploader, req_p=pprint)
			print("=======추가=======")
		print("+++++++++"+str(request_print_model.count()))
		return redirect('main:detail', id)
	else:
		return redirect('main:home', username = user.username)


def filter(request):
	user = request.user
	prints = Print.objects.all()
	# lecture_list = Lecture.objects.all()
	if request.method == "POST":
		filter_type = request.POST['action']
		if filter_type == '모두':
			lecture_pks = user.lectures.all()
			lecture_list = Lecture.objects.filter(pk__in=lecture_pks)
			prints = Print.objects.filter(
				schedule__lecture__in=[l for l in lecture_list]
			)

			for l in lecture_list:
				print("=========="+l.name+l.day_time)
			prints = Print.objects.filter(
				schedule__lecture__in=[l for l in lecture_list]
			).filter(
				valid=True
			)
		else:
			print("++++++"+filter_type)
			lecture_pks = user.lectures.filter(day_time__icontains=filter_type)
			print(lecture_pks)
			lecture_list = Lecture.objects.filter(pk__in=lecture_pks)
			for l in lecture_list:
				print("=========="+l.name+"/"+str(l.pk)+l.day_time)
			prints = Print.objects.filter(
				schedule__lecture__in=[l for l in lecture_list]
				# schedule__lecture__in=l
			).filter(
				valid=True
			)

		return render(request, 'main/home.html', {'prints': prints})

