# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-28 21:34
from __future__ import unicode_literals

from django.db import migrations

def triptime(apps, schema_editor):

    TestModel = apps.get_model('endpoint', 'TestModel')
    for entry in TestModel.objects.all():
        starttime = entry.starttime
        endtime = entry.stoptime
        tripdir = endtime - starttime
        entry.trip_duration = tripdir
        entry.save()



class Migration(migrations.Migration):

    dependencies = [
        ('endpoint', '0002_testmodel_trip_duration'),
    ]

    operations = [
        migrations.RunPython(triptime),
    ]