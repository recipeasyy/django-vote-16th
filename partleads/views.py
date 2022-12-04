from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from partleads.models import Candidate
from partleads.serializer import CandidateSerializer

POSITION_DICT = {
    'backend': 'BE',
    'frontend': 'FE'
}

class CandidateView(APIView):
    def get(self, request, position):
        candidates = Candidate.objects.filter(position=POSITION_DICT[position])
        serializer = CandidateSerializer(candidates, many=True)
        return Response(serializer.data)

    def post(self, request):
        # 유저 토큰 관련 예외 처리 필요
        # 유저 투표권 개수에 따른 투표/취소 구현 필요

        serializer = CandidateSerializer(data=request.data)

        if(serializer.is_valid()):
            candidate = get_object_or_404(Candidate, position=serializer.data['position'], name=serializer.data['name'])
            candidate.vote_count += 1
            candidate.save()
            serializer = CandidateSerializer(candidate)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({'Message': 'Candidate not found'}, status=status.HTTP_404_NOT_FOUND)