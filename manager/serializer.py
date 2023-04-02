from rest_framework.serializers import ModelSerializer
from .models import Donequestions,DoneVideos



class DoneQeustionSerializer(ModelSerializer):
    class Meta:
        model = Donequestions
        fields = "__all__"

class DoneVideosSerializer(ModelSerializer):
    class Meta:
        model = DoneVideos
        fields = "__all__"

        