from django.db import models
from django.conf import settings


class Profile(models.Model):
    profetion = (
        ("S","Student"),
        ("T","Teacher")
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    user_profetion = models.CharField(choices=profetion,default="S",max_length=1)
    image = models.ImageField(upload_to='profile_pics',default='default.jpg')
    birth_date = models.DateField(null=True)
    grade_level = models.IntegerField(default=12)
    

