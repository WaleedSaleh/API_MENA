from django.shortcuts import render
from .models import BTC
from django.http import JsonResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import time
from .serializers import BTCSerializer
from .tasks import fetch_btc_every_hour

# Create your views here.

class BTCList(APIView):
    """
    For listing all the objects.
    """

    def get(self, request):
        btcs = BTC.objects.all()
        serializer = BTCSerializer(btcs, many =True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ForceExchangeRate(APIView):
    """
    Forcing the task to retrue value
    """
    def post(self, request):
        fetch_btc_every_hour(now=True)
        btc_data = BTC.objects.last()
        serializer = BTCSerializer(btc_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(status=status.HTTP_400_BAD_REQUEST)


