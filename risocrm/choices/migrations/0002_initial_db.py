from django.conf import settings
from django.db import migrations, models

from risocrm.choices.models import Choice


def update_user_forward(apps, schema_editor):
    """Set site domain and name."""
    Choice.objects.create(name="City")
    Choice.objects.create(name="Rate")
    Choice.objects.create(name="Source")
    Choice.objects.create(name="Job")


def update_user_backward(apps, schema_editor):
    """Revert site domain and name to default."""
    Choice.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [("choices", "0001_initial")]

    operations = [migrations.RunPython(update_user_forward, update_user_backward)]
