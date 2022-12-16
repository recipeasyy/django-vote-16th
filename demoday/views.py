from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
from demoday.models import Team
from demoday.serializer import TeamSerializer

class TeamView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)

    def post(self, request):
        # 유저 토큰 관련 예외 처리 필요
        # 유저 투표권 개수에 따른 투표/취소 구현 필요

        serializer = TeamSerializer(data=request.data)

        if serializer.is_valid():
            team = get_object_or_404(Team, team_name=serializer.data['team_name'])
            team.vote_count += 1
            team.save()
            serializer = TeamSerializer(team)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'Message': 'Team not found'}, status=status.HTTP_404_NOT_FOUND)
