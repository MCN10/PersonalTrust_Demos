
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models import Count
from django.conf import settings


# Create your models here.
class Owner(models.Model):
    User            = settings.AUTH_USER_MODEL
    user            = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    date_created    = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    email 			= models.EmailField(verbose_name="email", max_length=60, unique=True, null=True)

    def __str__(self):
        if self.email:
            return self.email


class Task(models.Model):
    PRIORITY = (
        ('P1', 'P1'),
        ('P2' , 'P2'),
        ('P3', 'P3'),
        )
    STATUS = (
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Complete', 'Complete'),
        ('Back-log', 'Back-log'),
        )
    name                = models.CharField(max_length=200, null=True)
    creator                = models.CharField(max_length=200, null=True)
    assignee               = models.ForeignKey(Owner, on_delete=models.SET_NULL, blank=True, null=True)
    description         = models.TextField(max_length=200, null=True)
    priority            = models.CharField(max_length=200, null=True, choices=PRIORITY)
    notes               = models.TextField(max_length=200, null=True , blank=True)
    status              = models.CharField(max_length=200, null=True, choices=STATUS)
    date_created        = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    due_date            = models.DateTimeField(auto_now_add=False, null=True, blank=True)


    def __str__(self):
        return str(self.name)
