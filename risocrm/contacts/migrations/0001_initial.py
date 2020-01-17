# Generated by Django 2.2.8 on 2020-01-10 03:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('choices', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('time_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created on')),
                ('time_modified', models.DateTimeField(auto_now=True, null=True, verbose_name='Last modified on')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Name of contact')),
                ('email', models.CharField(blank=True, max_length=200, null=True, verbose_name='Email')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone number')),
                ('address', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Address')),
                ('facebook', models.CharField(blank=True, max_length=100, null=True, verbose_name='Facebook name')),
                ('facebook_url', models.CharField(blank=True, max_length=200, null=True, verbose_name='Facebook url')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='contacts_contact_city', to='choices.ChoiceDetail', verbose_name='City')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contacts_contact_creator', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contacts_contact_last_modified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by')),
                ('rate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='contacts_contact_rate', to='choices.ChoiceDetail', verbose_name='Rate')),
                ('source', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='contacts_contact_source', to='choices.ChoiceDetail', verbose_name='Source')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
