from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from backups.models import Backup
from backups.serializers import BackupSerializer


class BackupViewSet(ModelViewSet):
    queryset = Backup.objects.all()
    serializer_class = BackupSerializer