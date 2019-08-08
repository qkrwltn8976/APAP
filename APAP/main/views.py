from django.shortcuts import render, redirect, get_object_or_404
from models.models import *
from django.core.mail import send_mail
from .forms import Printform
import time, math

def home(request):
   user = request.user #로그인 구현 전 임시 설정
   id = user.pk
   username = user.username
   lecture_pks = user.lectures.all()
   lecture_list = Lecture.objects.filter(pk__in=lecture_pks)
   prints = Print.objects.filter(
      schedule__lecture__in=[l for l in lecture_list]
   )

   for l in lecture_list:
      print("=========="+l.name)
   prints = Print.objects.filter(
      schedule__lecture__in=[l for l in lecture_list]
   )

   timer = ""
   while timer:
      mins, secs = divmod(t, 60)
      timeformat = '{:02d}:{:02d}'.format(mins, secs)
      print(timeformat, end='\r')
      timer.sleep(1)
      timer -= 1
   return render(request, 'main/home.html', {'prints' : prints, 'timer' : timer})
# def home(request, id):
#    user = get_object_or_404(User, pk=id) #로그인 구현 전 임시 설정
#    username = user.username
#    return render(request, 'main/home.html', {'username': username})

   # if user.verified == True: #인증을 한 유저인 경우
   #    return render(request, 'main/home.html')
   # else: #인증하지 않은 유저인 경우
   #    # email = 'original@here.com'
   #    # user = User.objects.create_user(email, email=email)
   #    # user.is_confirmed # False

   #    # send_mail(email, 'Use %s to confirm your email' % user.password, email, [email])
   #    # # User gets email, passes the confirmation_key back to your server

   #    # user.confirm_email(user.password)
   #    # user.is_confirmed # True
   #    return render(request, 'main/verify.html')



def upload(request, username):
   user = request.user #로그인 구현 전 임시 설정
   username = user.username

   form = Printform(request.user, request.POST, request.FILES or None)
   if request.method == "POST":
      if form.is_valid():
         form = form.save(commit=False) # form을 당장 저장하지 않음. 데이터 저장 전 뭔가 하고 싶을 때 사용.
         form.uploader = request.user
         
         # 인쇄비 계산 
         pages = 20
         if(form.color=="colorful"):
         	color_price = 200
         else:
         	color_price = 40
         form.print_price = math.ceil(pages/form.gather)*color_price
        
         form.save()
        
         return redirect('main:home')
   else:
      form = Printform(request.user, request.POST)
   return render(request, 'main/upload.html', {'form' : form})


def check(directory):
	if directory.endswith(".pdf"):
		pdf_files.append("./"+directory)
	else :
		pdf_files.extend(search(directory.rstrip("/").encode('utf-8'), bool(args.recursive)))


def count_pages(filename):
	data = open(filename, "rb").read()
	return len(rxcountpages.findall(str(data)))


def search(root_dir, recursive_search):
	file_list = []
	for (dirpath, dirnames, filenames) in os.walk(settings.MEDIA_ROOT):
		for filename in filenames:
			if filename.endswith(b'.pdf'):
				file_list.append(dirpath.decode('utf-8') + '/' + filename.decode('utf-8'))
				if not recursive_search:
					break
		return file_list


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
	schedule = Schedule.objects.filter(user = user)

	prints = Print.objects.filter(
		uploader = user
	)
	pprints = Print.objects.filter(
      requests = user
	)
	return render(request, 'main/mypage.html', {'user' : user, 'lectures' : lectures, 'schedule' : schedule, 'prints' : prints, 'pprints' : pprints})

def detail(request, id):
	pprint = get_object_or_404(Print, pk=id)
	user = request.user
	id = user.pk


	if user == pprint.uploader:
		valid = True
		print("일치")
	else:
		valid = False
		print("불일치")

	username = user.username
	lectures = Lecture.objects.all()
	cnt = pprint.requests.count()
	return render(request, 'main/detail.html', {'user' : user, 'lectures' : lectures, 'print': pprint, 'valid': valid, 'cnt':cnt})



def update(request, id):
	form = Printform(request.user)
	pprint = get_object_or_404(Print, pk=id)
	if request.method == "POST":
		color = request.POST.get('color')
		gather = request.POST.get('gather')
		side = request.POST.get('side')
		direction = request.POST.get('direction')
		price = request.POST.get('price')
		pprint.color = color
		pprint.gather = gather
		pprint.side = side
		pprint.direction = direction
		pprint.price = price
		pprint.save()
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
		if user == pprint.uploader:
			valid = True
			print("일치")
		else:
			valid = False
			print("불일치")
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
		return redirect('main:home', username = user.username, {'valid':valid})


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
         )

      return render(request, 'main/home.html', {'prints': prints})

