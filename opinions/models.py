from django.db import models


# Create your models here.
from candidates.models import Candidate


class KeyTopic(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=200)


class Tag(models.Model):
    name = models.CharField(max_length=40)


class Opinion(models.Model):
    OVERALL_TAGS = (
        ('A FAVOR', 'A favor'),
        ('EN CONTRAR', 'En contra'),
        ('NO OPINA', 'No opina'),
        ('IMPRECISO', 'Impreciso')
    )
    overall = models.CharField(choices=OVERALL_TAGS, max_length=20)
    tittle = models.CharField(max_length=200)
    description = models.TextField()
    candidate = models.ForeignKey(Candidate, on_delete=models.PROTECT)
    key_topic = models.ForeignKey(KeyTopic, on_delete=models.PROTECT)
    tag = models.ManyToManyField(Tag)
