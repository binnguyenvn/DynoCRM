# Generated by Django 2.2.8 on 2020-01-10 03:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('time_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created on')),
                ('time_modified', models.DateTimeField(auto_now=True, null=True, verbose_name='Last modified on')),
                ('object_id', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('flaticon2-safe', 'System'), ('flaticon-facebook-letter-logo', 'Facebook'), ('flaticon-facebook-logo-button', 'Paid Facebook'), ('flaticon-letter-g', 'Google'), ('flaticon-mail-1', 'Email'), ('flaticon2-phone', 'Phone'), ('flaticon2-website', 'Website'), ('flaticon2-sheet', 'Form')], default='flaticon2-safe', max_length=50)),
                ('note', models.TextField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activities_activity_creator', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activities_activity_last_modified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
