from django.db import models


from django.contrib.auth.models import AbstractUser
# from django.contrib.postgres.fields import ArrayField

class User(AbstractUser):
	university = models.CharField(max_length=100)
	level = models.IntegerField(default=1)
	verified = models.BooleanField(default=False)

class University(models.Model):
	name = models.CharField(max_length=100)
	
class Lecture(models.Model):
	name = models.CharField(max_length=100)
	code = models.IntegerField()
	day_time = models.CharField(max_length=100)

	university = models.ForeignKey(
		University,
		on_delete = models.CASCADE,
		related_name = 'university',
	)



