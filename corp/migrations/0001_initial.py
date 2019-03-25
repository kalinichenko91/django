# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-08 12:47
# flake8: noqa
from __future__ import unicode_literals

import clublink.base.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CorpNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish_date', models.DateField()),
                ('headline', models.CharField(max_length=255)),
                ('summary', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('photo', models.ImageField(upload_to=clublink.base.utils.RandomizedUploadPath('club_news'))),
            ],
            options={
                'ordering': ('-publish_date',),
            },
        ),
    ]
