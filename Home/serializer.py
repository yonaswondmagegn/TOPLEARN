from rest_framework import serializers
from .models import (Course,VideoFiles,
                     VideoFinalQuestions,ChoiceForQuestion,
                     OtherMatterialsForTheVideo,
                     Comment,
                     Review,

)
from manager.serializer import (DoneQeustionSerializer,
                                DoneVideosSerializer,
                                
)
from manager.models import DoneVideos,Donequestions

# ^^^^imports


class CourseSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Course
        fields = "__all__"

class VideoFileSerializer(serializers.ModelSerializer):
    is_seen = serializers.SerializerMethodField(method_name='viewChecker')

    class Meta:
        model  = VideoFiles
        fields = "__all__"

    def viewChecker(self,video_c:VideoFiles):
        done_video = DoneVideos.objects.filter(
            student = self.context['request'].user,
            video = video_c).first()
        if done_video:
            serialized = DoneVideosSerializer(done_video)
            return serialized.data
        else:
            return False

class ChoiceForQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceForQuestion
        fields = ['id','choice']

class VideoFinalQuestionSerializer(serializers.ModelSerializer):
    is_done = serializers.SerializerMethodField(method_name='get_donequestions')
    choices = ChoiceForQuestionSerializer(many = True)
    
    class Meta:
        model = VideoFinalQuestions
        fields = "__all__"

    def get_donequestions(self, questiond:VideoFinalQuestions):
        finished_questions = Donequestions.objects.filter(
            student = self.context['request'].user,
            question = questiond).first()
        
        if finished_questions:
            serialized = DoneQeustionSerializer(finished_questions)
            return serialized.data
        else:
            return False



class ChoiceForQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceForQuestion
        fields = "__all__"

class OtherMatterialsForTheVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherMatterialsForTheVideo
        fields = "__all__"
        


# Serialize the review models 

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


