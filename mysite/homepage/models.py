from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Myusr(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    score1 = models.IntegerField(default=0)
    score2 = models.IntegerField(default=0)
    score4 = models.IntegerField(default=0)
    score3 = models.IntegerField(default=0)
    score11 = models.IntegerField(default=0)
    score21 = models.IntegerField(default=0)
    score41 = models.IntegerField(default=0)
    score31 = models.IntegerField(default=0)
    score12 = models.IntegerField(default=0)
    score22 = models.IntegerField(default=0)
    score42 = models.IntegerField(default=0)
    score32 = models.IntegerField(default=0)
    tempscore = models.IntegerField(default=0)
    house = models.CharField(max_length=200,default=0)
    preferredh = models.CharField(max_length=200)
    totals = models.IntegerField(default=0)
    totals2 = models.IntegerField(default=0)
    totals3 = models.IntegerField(default=0)
    totals4 = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    level1 = models.IntegerField(default=1)
    level2 = models.IntegerField(default=1)
    level3 = models.IntegerField(default=1)
    level4 = models.IntegerField(default=1)
    grandtotal = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    bonfl=models.IntegerField(default=0)


class activa(models.Model):
    user1 = models.CharField(max_length=100)
    otp = models.CharField(max_length=100)	
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
	
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.FileField(max_length=500, blank=True)
    checker = models.IntegerField(default=0)

