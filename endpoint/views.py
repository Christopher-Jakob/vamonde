# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.response import Response
from models import TestModel
from rest_framework.views import APIView

# Create your views here.

class Endpoint(APIView):

    def get(self, request, *args, **kwargs):
        from_station_id = kwargs.get('from_station_id')
        starttime = kwargs.get('starttime')
        endtime = kwargs.get('endtime')
        entries = TestModel.objects.filter(from_station_id=from_station_id,
                                           starttime=starttime,
                                           endtime=endtime)
        stationname = entries[0].from_station_name
        duration = None
        count = 0
        for entry in entries:
            count += 1
            duration = duration +  entry.trip_duration
        duration = duration / count
        return Response({
            "average_duration": duration,
            "station_id": from_station_id,
            "station_name": stationname
        })




        



