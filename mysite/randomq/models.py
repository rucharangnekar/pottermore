#from django.contrib.postgres.fields import ArrayField

from django.db import models

# Create your models here.
class Rquiz(models.Model):
	numberr=models.IntegerField(default=0)
	questions=models.TextField(max_length=550)
	option1=models.CharField(max_length=250)
	option2=models.CharField(max_length=250)
	option3=models.CharField(max_length=250)
	option4=models.CharField(max_length=250)
	answer=models.IntegerField(default=0)
	imgee=models.FileField(null=True)
	tanswer=models.CharField(max_length=250)

class Quiz(models.Model):
	numberr = models.IntegerField(default=0)
	questions = models.TextField(max_length=550)
	option1 = models.CharField(max_length=250)
	option2 = models.CharField(max_length=250)
	option3 = models.CharField(max_length=250)
	option4 = models.CharField(max_length=250)
	answer = models.IntegerField(default=0)
	category=models.CharField(max_length=100)