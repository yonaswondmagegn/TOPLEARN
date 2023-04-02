from django.db import models
from django.core.validators import FileExtensionValidator
from Profile.models import Profile
from django.utils import timezone
from django.conf import settings



# the choice filed for videoFinalQuestion model 
class ChoiceForQuestion(models.Model):
    choice = models.TextField()
    is_correct = models.BooleanField(default=False)



# bundle for one specfic course 
class Course(models.Model): 
    title = models.CharField(max_length=225)
    thumbnail = models.ImageField(upload_to='course_thumbnail',
                                  default='course_thumbnail.jpg')
    
    lectures = models.ManyToManyField(Profile,related_name="lectures")
    description = models.TextField()
    date = models.DateTimeField(timezone.now)


# list of videos that in compass with one course 
class VideoFiles(models.Model):
    title = models.CharField(max_length=225)
    thumbnail = models.ImageField(upload_to='thumbnail_field',
                                  default = 'video_thumbnail.jpg')
    video = models.FileField(upload_to='course_videos',
                             validators=[FileExtensionValidator(
        allowed_extensions=['MP4','AVI'])])
    
    description = models.TextField()
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    date = models.DateTimeField(default=timezone.now)

# final question for each vidofile
class VideoFinalQuestions(models.Model):
    qtype = (
        ('S','SHORTANSWERE'),
        ('C','CHOISE')
    )
    question = models.TextField()
    videos = models.ForeignKey(VideoFiles,on_delete=models.CASCADE,related_name='videos',null=True)
    questiontype = models.CharField(choices=qtype,default='C',max_length=1)
    choices = models.ManyToManyField(ChoiceForQuestion,related_name="choices",blank=True)
    answere = models.TextField(null=True)
    description = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now)


# other matterials connected to videos by the lectures or other students
class OtherMatterialsForTheVideo(models.Model):
    uploder = models.ForeignKey(Profile,on_delete=models.CASCADE)
    file = models.FileField(upload_to='other_matterials_forthevideo')
    description = models.TextField()
    video = models.ForeignKey(VideoFiles,on_delete=models.CASCADE,null = True)
    date = models.DateTimeField(default=timezone.now)


# the model under this comment is responsible for manageing reviews 


class Comment(models.Model):
    tag = (
        ('Q',"QUESTION"),
        ('A','ANSWERE'),
        
    )
    video = models.ForeignKey(VideoFiles,on_delete=models.CASCADE)
    answerefor = models.ForeignKey('self',blank= True,on_delete=models.CASCADE)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    question_text  = models.TextField()
    type = models.CharField(choices=tag,default='A',max_length=1)
    date = models.DateTimeField(default=timezone.now)

class Review(models.Model):
    rating  = (
        (1,"*"),
        (2,"**"),
        (3,"***"),
        (4,"****"),
        (5,"*****"),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    rating = models.IntegerField(choices=rating)
    date = models.DateTimeField(default=timezone.now)
