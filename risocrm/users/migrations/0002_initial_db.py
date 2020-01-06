from allauth.socialaccount.models import SocialApp
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db import migrations, models

User = get_user_model()


def update_user_forward(apps, schema_editor):
    """Set site domain and name."""
    group = Group.objects.update_or_create(
        id=1,
        name="Administrator"
    )
    Group.objects.update_or_create(
        id=2,
        name="Manager"
    )
    Group.objects.update_or_create(
        id=3,
        name="Leader"
    )
    Group.objects.update_or_create(
        id=4,
        name="Sale"
    )
    


def update_user_backward(apps, schema_editor):
    """Revert site domain and name to default."""
    Group.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [("users", "0001_initial")]

    operations = [migrations.RunPython(update_user_forward, update_user_backward)]
