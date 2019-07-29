from django.db import models


from django.contrib.auth.models import AbstractUser
from simple_email_confirmation.models import SimpleEmailConfirmationUserMixin
# from django.contrib.postgres.fields import ArrayField

class User(SimpleEmailConfirmationUserMixin, AbstractUser):
	university = models.CharField(max_length=100)
	level = models.IntegerField(default=1)
	verified = models.BooleanField(default=False)

	
class University(models.Model):
	name = models.CharField(max_length=100)
	
class Lecture(models.Model):
	name = models.CharField(max_length=100)
	code = models.CharField(max_length=100)
	day_time = models.CharField(max_length=100)

	university = models.ForeignKey(
		University,
		on_delete = models.CASCADE,
		related_name = 'university',
	)


class Print(models.Model):
	# 요청 추가해야함!
	color = models.BooleanField(default=True)
	side = models.BooleanField(default=True)
	gather = models.IntegerField(default=1)
	direction = models.BooleanField(default=True)
	order = models.BooleanField(default=True)
	price = models.IntegerField(default=2500)
	cnt = models.IntegerField(default=0)


