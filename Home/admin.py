from django.contrib import admin
from .models import Course,VideoFiles,VideoFinalQuestions

admin.site.register(Course)
admin.site.register(VideoFinalQuestions)
admin.site.register(VideoFiles)

