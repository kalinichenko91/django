# Generated by Django 2.0.2 on 2018-04-06 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0086_corpeventsgallery_site'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubgalleryimage',
            name='gallery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='cms.ClubGallery'),
        ),
        migrations.AlterField(
            model_name='corpeventsgalleryimage',
            name='gallery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='cms.CorpEventsGallery'),
        ),
    ]
