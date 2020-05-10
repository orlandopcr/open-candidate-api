from rest_framework import routers

from candidates.views import CandidateViewSet, PoliticalCoalitionViewSet

router = routers.DefaultRouter()

router.register(r'candidates', CandidateViewSet, basename='candidates')
router.register(r'political-coalitions', PoliticalCoalitionViewSet, basename='political-coalitions')

urlpatterns = router.urls
