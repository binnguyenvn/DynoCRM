# Generated by Django 2.2.8 on 2020-01-10 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configs', '0002_externalconfig_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportconfig',
            name='type',
            field=models.CharField(choices=[('count', 'Count'), ('percent', 'Percent')], max_length=200),
        ),
    ]
