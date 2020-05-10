from rest_framework.serializers import ModelSerializer

from candidates.models import Candidate, PoliticalCoalition


class CandidateSerializer(ModelSerializer):

    class Meta:
        model = Candidate
        fields = '__all__'


class PoliticalCoalitionSerializer(ModelSerializer):

    class Meta:
        model = PoliticalCoalition
        fields = '__all__'
