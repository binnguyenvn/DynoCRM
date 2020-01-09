# Generated by Django 2.2.8 on 2020-01-09 09:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tile',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dashboard_tile_creator', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='tile',
            name='last_modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dashboard_tile_last_modified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by'),
        ),
        migrations.AlterField(
            model_name='tile',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created on'),
        ),
        migrations.AlterField(
            model_name='tile',
            name='time_modified',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Last modified on'),
        ),
    ]