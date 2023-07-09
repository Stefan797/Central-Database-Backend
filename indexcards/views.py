from django.shortcuts import render

from rest_framework.views import APIView
from indexcards.models import IndexcardsItem
from indexcards.serializers import IndexcardsItemSerializer
from rest_framework.response import Response

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class IndexcardsItemView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        indexcards = IndexcardsItem.objects.all()
        serializer = IndexcardsItemSerializer(indexcards, many=True)
        return Response(serializer.data)