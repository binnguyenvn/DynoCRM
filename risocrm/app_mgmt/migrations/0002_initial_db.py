from django.conf import settings
from django.db import migrations, models

from risocrm.app_mgmt.models import Dynafield


def update_field_forward(apps, schema_editor):
    pass


def update_field_backward(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [("app_mgmt", "0001_initial")]

    operations = [migrations.RunPython(update_field_forward, update_field_backward)]
