from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    subscription = (
        ('N',"NOT_SUBSCRIBED"),
        ('P','PREMIAM'),
        ('PP','PREMIMEPRO')
    )
    subscriptiontype = models.CharField(choices=subscription,default='N',max_length=225)
