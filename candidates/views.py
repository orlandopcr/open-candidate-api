from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from candidates.models import Candidate, PoliticalCoalition
from candidates.serializers import CandidateSerializer, PoliticalCoalitionSerializer


class CandidateViewSet(ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


class PoliticalCoalitionViewSet(ModelViewSet):
    queryset = PoliticalCoalition.objects.all()
    serializer_class = PoliticalCoalitionSerializer
