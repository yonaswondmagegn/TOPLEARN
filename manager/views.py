from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .serializer import DoneQeustionSerializer,DoneVideosSerializer
from .models import Donequestions,DoneVideos
from Home.models import VideoFinalQuestions,VideoFiles
from Home.CustomPermision import PaymentVerified
from rest_framework.permissions import IsAuthenticated
from django.conf import settings



class DoneQuestionViewset(ModelViewSet):
    serializer_class = DoneQeustionSerializer
    permission_classes = [IsAuthenticated,PaymentVerified]

    def get_queryset(self):
        queryset = Donequestions.objects.filter(student = self.request.user)
        return queryset
    
    def create(self, request, *args, **kwargs):
        serialized = self.get_serializer(data = request.data)
        serialized.is_valid(raise_exception = True)

        correctness = False
        question = VideoFinalQuestions.objects.get(id = serialized.validated_data['question'].id)
        student_answere = serialized.validated_data['student_answere']

        if (question.questiontype == "S"):
            if(student_answere == question.answere):
                correctness = True
        else:
            qid = int(student_answere)
            queryset = ''
            for qset in question.choices:
                if qset.id == qid:
                    queryset = qset
            
            if queryset:
                correctness == queryset.is_correct

        serialized.save(is_correct = correctness)
    
        return Response(serialized.data,status=status.HTTP_201_CREATED)
    


class DoneVideosViewset(ModelViewSet):
    serializer_class = DoneVideosSerializer
    permission_classes = [IsAuthenticated,PaymentVerified]

    def get_queryset(self):
        queryset = DoneVideos.objects.filter(student = self.request.user)
        return queryset
    





