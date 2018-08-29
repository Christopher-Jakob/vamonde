# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class TestModel(models.Model):
    trip_id = models.IntegerField()
    starttime = models.DateTimeField()
    stoptime = models.DateTimeField()
    bikeid = models.IntegerField()
    from_station_id = models.IntegerField()
    from_station_name = models.CharField(max_length=200)
    to_station_id = models.IntegerField()
    to_station_name = models.CharField(max_length=200)
    usertype = models.CharField(max_length=100)
    gender = models.CharField(max_length=2, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    trip_duration = models.DurationField(blank=True, null=True)


import csv
import os

def csvimport():
    path = "/home/rickus/Desktop/"
    os.chdir(path)
    with open('divvy_vamonde.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        count = 0
        for row in reader:
            count += 1
            print(str(count) + ' thats the current count')
            p = TestModel(trip_id=row['trip_id'], starttime=row['starttime'], stoptime=row['stoptime'], bikeid=row['bikeid'], from_station_id=row['from_station_id'], from_station_name=row['from_station_name'], to_station_id=row['to_station_id'], to_station_name=row['to_station_name'], usertype=row['usertype'])
            p.save()