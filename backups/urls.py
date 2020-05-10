from rest_framework import routers

from backups.views import BackupViewSet

router = routers.DefaultRouter()

router.register(r'backups', BackupViewSet, basename='backups')

urlpatterns = router.urls
