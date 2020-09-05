from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from nx.models import *


class MainPageInfo(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        finance_rate= Finance_rates.objects.all()
        default_rates = [[ra.rate,ra.currency] for ra in finance_rate]
        data = {
            "request1": Requests.objects.filter(status=1).count(),
            "request2": Requests.objects.filter(status=2).count(),
            'users': Users.objects.all().count(),
            'default_rate':default_rates,


        }
        return Response(data)
