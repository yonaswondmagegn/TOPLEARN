from django.urls import path
from .views import DoneQuestionViewset,DoneVideosViewset
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register('donequestions', DoneQuestionViewset,basename = 'donequestions')
router.register('donevideos',DoneVideosViewset,basename='donevideos')


urlpatterns = router.urls