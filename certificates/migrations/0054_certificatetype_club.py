# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-05 12:37
# flake8: noqa
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0027_auto_20170406_2306'),
        ('certificates', '0053_auto_20170505_0720'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificatetype',
            name='club',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='certificate_types', to='clubs.Club'),
        ),
    ]
