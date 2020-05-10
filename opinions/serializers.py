from rest_framework.serializers import ModelSerializer

from opinions.models import Opinion, KeyTopic, Tag


class OpinionSerializer(ModelSerializer):

    class Meta:
        model = Opinion
        fields = '__all__'


class KeyTopicSerializer(ModelSerializer):

    class Meta:
        model = KeyTopic
        fields = '__all__'


class TagSerializer(ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'
