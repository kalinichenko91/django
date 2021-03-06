# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-07-02 21:19
from __future__ import unicode_literals

from django.db import migrations


SYSTEM_PAGES = [
    '',
    'about',
    'about/gallery',
    'about/golf-shop',
    'about/policies',
    'about/team',
    'contact-us',
    'daily-fee-golf',
    'daily-fee-golf/book',
    'daily-fee-golf/rates',
    'events',
    'events/golf-tournaments',
    'events/meetings',
    'events/weddings',
    'game-improvement',
    'linkline',
    'linkline/book-a-tee-time',
    'linkline/golf-policies',
    'linkline/terms-of-use',
    'membership',
    'membership/guest-fees',
    'my-account',
    'my-account/annual-dues',
    'my-account/member-services',
    'my-account/payment-terms',
    'my-account/statement',
    'my-account/update-profile',
    'my-club',
    'my-club/bistro-menus',
    'my-club/calendar',
    'my-club/roster',
    'news'
]


def create_system_pages(apps, schema_editor):
    Club = apps.get_model('clubs', 'Club')
    ClubPage = apps.get_model('cms', 'ClubPage')

    for club in Club.objects.all():
        for path in SYSTEM_PAGES:
            base_path = path.split('/')
            slug = base_path.pop()
            base_path = '/'.join(base_path)

            parent = ClubPage.objects.get(club=club, full_path=base_path) if base_path else None
            page, _ = ClubPage.objects.get_or_create(club=club, parent=parent, slug=slug)
            page.full_path = path
            page.is_locked = True
            page.save()


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0029_auto_20170702_1652'),
    ]

    operations = [
        migrations.RunPython(create_system_pages),
    ]
