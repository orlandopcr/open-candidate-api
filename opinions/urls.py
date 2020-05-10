from rest_framework import routers

from opinions.views import OpinionViewSet, KeyTopicViewSet, TagViewSet

router = routers.DefaultRouter()

router.register(r'opinions', OpinionViewSet, basename='opinions')
router.register(r'key-topics', KeyTopicViewSet, basename='key-topics')
router.register(r'tags', TagViewSet, basename='tags')

urlpatterns = router.urls
