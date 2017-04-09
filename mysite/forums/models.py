from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class ForumDB(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    user_name = models.CharField(max_length=150,default="")
    count = models.IntegerField(default=0)
    house=models.CharField(max_length=200)
    fid=models.IntegerField(default=0)

    def __str__(self):
        return self.name + " - " + self.description


class ThreadDB(models.Model):
    forum_no = models.ForeignKey(ForumDB, on_delete=models.CASCADE)
    foid=models.IntegerField(default=0)
    post = models.CharField(max_length=5000)
    user_name = models.CharField(max_length=150)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    count = models.IntegerField(default=0)
    dislike=models.IntegerField(default=0)
    like=models.IntegerField(default=0)
    flag=models.IntegerField(default=0)
    delflag=models.IntegerField(default=0)
    postid=models.IntegerField(default=0)
    profile_pic = models.FileField(max_length=500, blank=True)

    def __str__(self):
        return str(self.forum_no)

class Mypost(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    pid=models.IntegerField(default=0)

class Report(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rid=models.IntegerField(default=0)
