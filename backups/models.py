from django.db import models

# Create your models here.
from opinions.models import Opinion


class Backup(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True, blank=True)
    url = models.URLField()
    snapshot = models.URLField(null=True, blank=True)
    opinion = models.ForeignKey(Opinion, on_delete=models.PROTECT)
