from django.urls import path
from rest_framework_nested import routers
from .views import (CourseViewsets,
                    VideoFilesViewSets,
                    VideoFinalQuestionsViewset,
                    OtherMatterialsViewSet,
                    CommentViewset,
                    ReviewViewset
)

router = routers.DefaultRouter()
router.register('courses',CourseViewsets)

nested_router = routers.NestedDefaultRouter(router,
                                            'courses',lookup = 'course')
nested_router.register('videos',VideoFilesViewSets,basename='videos')
nested_router.register('review',ReviewViewset,basename='review')




double_router = routers.NestedDefaultRouter(nested_router,'videos',
                                            lookup = 'video')
double_router.register('finalquestions',VideoFinalQuestionsViewset,
                       basename='eachvideofinalquestion')
double_router.register('othermatterials',OtherMatterialsViewSet,
                       basename='othermatterials')
double_router.register('comments',CommentViewset,basename='comment')


urlpatterns = router.urls +nested_router.urls+double_router.urls