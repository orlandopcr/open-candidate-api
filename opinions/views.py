from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from opinions.models import Opinion, KeyTopic, Tag
from opinions.serializers import OpinionSerializer, KeyTopicSerializer, TagSerializer


class OpinionViewSet(ModelViewSet):
    queryset = Opinion.objects.all()
    serializer_class = OpinionSerializer


class KeyTopicViewSet(ModelViewSet):
    queryset = KeyTopic.objects.all()
    serializer_class = KeyTopicSerializer


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
