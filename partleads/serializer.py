from rest_framework import serializers

from partleads.models import Candidate


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['name', 'position', 'vote_count']