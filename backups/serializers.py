from rest_framework.serializers import ModelSerializer

from backups.models import Backup


class BackupSerializer(ModelSerializer):

    class Meta:
        model = Backup
        fields = '__all__'