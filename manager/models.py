from django.db import models
from django.conf import settings
from Home.models import VideoFinalQuestions,VideoFiles
from django.utils import timezone

# To store the question that was done and also was the student correct or not 

class Donequestions(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    question = models.ForeignKey(VideoFinalQuestions,on_delete=models.CASCADE)
    student_answere = models.TextField(null=True)
    is_correct = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)
    
""""
    The done videos model is to manage how much the students done the course 
    the view set connected to this model will be responsible to analyze and responed how 
    the student progress is going  

"""
class DoneVideos(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    video = models.ForeignKey(VideoFiles,on_delete=models.CASCADE)
    persentage= models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
