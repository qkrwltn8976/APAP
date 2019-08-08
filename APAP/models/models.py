from django.db import models
from django.contrib.auth.models import AbstractUser
from simple_email_confirmation.models import SimpleEmailConfirmationUserMixin
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
from pusherable.mixins import PusherDetailMixin, PusherUpdateMixin
from django.utils import timezone

class University(models.Model):
	objects = models.Manager()
	name = models.CharField(max_length=100)
	

class Lecture(models.Model):
	objects = models.Manager()
	name = models.CharField(max_length=100)
	code = models.CharField(max_length=100)
	day_time = models.CharField(max_length=100)

	university = models.ForeignKey(
		University,
		on_delete = models.CASCADE,
		related_name = 'university',
	)

	def __str__(self):
		return self.name


class User(SimpleEmailConfirmationUserMixin, AbstractUser):
	university = models.CharField(max_length=100)
	level = models.IntegerField(default=1)
	verified = models.BooleanField(default=False)
	lectures = models.ManyToManyField(Lecture, related_name = 'lectures', through='Schedule')
	point = models.IntegerField(default=5000)


class Schedule(models.Model): #User와 Lecture사이의 관계를 정의하는 중계모델
	objects = models.Manager()
	user = models.ForeignKey(
		User,
		on_delete = models.CASCADE,
		related_name = 'user',
	)
	lecture = models.ForeignKey(
		Lecture,
		on_delete = models.PROTECT,
		related_name = 'lecture',
	)
	req_print = models.ForeignKey(
		'Print',
		on_delete = models.PROTECT,
		related_name = 'req_print',
		null=True,
	)

	def __str__(self):
		return "{}:{}".format(self.lecture.name, self.lecture.code)


	
class Print(models.Model):
	objects = models.Manager()
	uploader = models.ForeignKey(User, on_delete = models.CASCADE)
	
	colorful="colorful"
	grayish="grayish"
	color_choices = (colorful, '컬러'), (grayish, '흑백')
	color = models.CharField(max_length=10, choices=color_choices, blank=True)

	single="single"
	double="double"
	side_choices = (single, '단면'), (double, '양면')
	side = models.CharField(max_length=10, choices=side_choices, blank=True)

	gather = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(8)], blank=True)

	horizontal="horizontal"
	vertical="vertical"
	direction_choices = (horizontal, '가로'), (vertical, '세로')
	direction = models.CharField(max_length=10, choices=direction_choices, blank=True)

	delivery_price = models.IntegerField(default=2500, blank=True) #배송비
	print_price = models.IntegerField(default=0, blank=True) #인쇄비

	date = models.DateTimeField(default=datetime.now, blank=True) 
	file = models.FileField(null=True, blank=True)

	valid = models.BooleanField(default=True)
	schedule = models.ForeignKey(
		Schedule,
		on_delete = models.CASCADE,
		related_name = 'schedule',
		blank=True
	)
	requests = models.ManyToManyField(
		User, 
		related_name='requests',
		blank=True
	)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	# def __str__(self):
	# 	if self.date == timezone.localtime():
	# 		self.valid = False

class PrintRequest(models.Model):
	from_user = models.ForeignKey(
		User,
		on_delete = models.CASCADE,
		related_name = 'from_user',
	)
	to_user = models.ForeignKey(
		User,
		on_delete = models.CASCADE,
		related_name = 'to_user',
	)
	req_p = models.ForeignKey(
		Print,
		on_delete = models.CASCADE,
		related_name = 'req_p',
	)
	point = models.IntegerField(default=0, blank=True)

	# def __str__(self):
	# 	if self.req_p.date == 
	







