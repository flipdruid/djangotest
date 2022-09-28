from django.db import models

# Create your models here.

from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Core(models.Model):
    poll_title          =   models.CharField (max_length=200)
    description         =   models.TextField(null=True)
    author              =   models.ForeignKey(User, on_delete=models.CASCADE, related_name='core')    
    updated             =   models.DateTimeField(auto_now=True)
    published           =   models.DateTimeField(default=timezone.now)   

    class Meta:
        ordering    =   ['-published']

    def __str__(self):
        return self.poll_title

class Currentpolls(models.Model):
    currentUser         =   models.CharField(max_length=20)
    pollID              =   models.IntegerField(default=0)
    pollComments        =   models.CharField(max_length=200)
    commentsDate        =   models.DateTimeField(auto_now =True)   


    