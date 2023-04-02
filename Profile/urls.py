from django.urls import path
from .views import ProfileViewset
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register('profile', ProfileViewset)

urlpatterns = router.urls