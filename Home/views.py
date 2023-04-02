from django.shortcuts import render,get_object_or_404
from .models import (Course,
                     VideoFiles,
                     VideoFinalQuestions,
                     OtherMatterialsForTheVideo,
                     Comment,
                     Review
                     )
from .serializer import (
    CourseSerializer,
    VideoFileSerializer,
    VideoFinalQuestionSerializer,
    OtherMatterialsForTheVideoSerializer,
    CommentSerializer,
    ReviewSerializer,
)
from rest_framework.views import APIView
from rest_framework.permissions import (AllowAny,IsAuthenticated,
                                        SAFE_METHODS,
                                        IsAdminUser,
                                        )
from rest_framework.viewsets import ModelViewSet
from .CustomPermision import PaymentVerified,isAdminOrReadOnly,Authorized_toGive_Review


class CourseViewsets(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]


class VideoFilesViewSets(ModelViewSet):
    serializer_class = VideoFileSerializer
    permission_classes = [IsAuthenticated,PaymentVerified,isAdminOrReadOnly]
 
    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [IsAuthenticated(),PaymentVerified()]
        else:
            return [IsAuthenticated(),IsAdminUser()]
    
    def get_queryset(self):
        c_id = self.kwargs['course_pk']
        queryset = VideoFiles.objects.filter(course_id = c_id)

        return queryset
    

class VideoFinalQuestionsViewset(ModelViewSet):
    serializer_class = VideoFinalQuestionSerializer
    permission_classes = [IsAuthenticated,PaymentVerified,isAdminOrReadOnly]


    def get_queryset(self):
        vid_id = self.kwargs['video_pk']
        queryset = VideoFinalQuestions.objects.filter(videos_id = vid_id)
        return queryset


class OtherMatterialsViewSet(ModelViewSet):
    serializer_class = OtherMatterialsForTheVideoSerializer
    permission_classes = [IsAuthenticated,PaymentVerified,isAdminOrReadOnly]

        
    def get_queryset(self):
        vid_id = self.kwargs['video_pk']
        queryset = OtherMatterialsForTheVideo.objects.filter(video_id = vid_id)
        return queryset
    

#Review view sets 

class CommentViewset(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated,PaymentVerified]

    def get_queryset(self):
        vid_id = self.kwargs['video_pk']
        queryset = Comment.objects.filter(video_id = vid_id)
        return queryset
    

class ReviewViewset(ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated,PaymentVerified,Authorized_toGive_Review]


    def get_queryset(self):
        cour_id  = self.kwargs['course_pk']
        queryset = Review.objects.filter(course_id = cour_id)
        return queryset

    
