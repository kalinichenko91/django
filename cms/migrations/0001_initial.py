# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-13 10:27
# flake8: noqa
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clubs', '0003_club_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=64)),
                ('club', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pages', to='clubs.Club')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='cms.Page')),
            ],
        ),
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locale', models.CharField(choices=[('en', 'English'), ('fr', 'French')], max_length=2)),
                ('slug', models.CharField(max_length=64)),
                ('content', models.TextField()),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='snippets', to='cms.Page')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='snippet',
            unique_together=set([('page', 'locale', 'slug')]),
        ),
        migrations.AlterUniqueTogether(
            name='page',
            unique_together=set([('club', 'slug')]),
        ),
    ]
