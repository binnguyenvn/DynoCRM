from django.conf import settings
from django.db import migrations, models

from risocrm.app_mgmt.models import Dynafield
from risocrm.choices.models import Choice


def update_field_forward(apps, schema_editor):
    city = Choice.objects.get(name="City")
    rate = Choice.objects.get(name="Rate")
    source = Choice.objects.get(name="Source")
    Dynafield.objects.create(
        module="Contact",
        name="phone",
        type="CharField",
        verbose_name="Phone number",
        fkmodule="",
        on_delete="",
        default=None,
        max_length=20,
        group="Contact Infomation",
        option=None)
    Dynafield.objects.create(
        module="Contact",
        name="address",
        type="CharField",
        verbose_name="Address",
        fkmodule="",
        on_delete="",
        default=None,
        max_length=1000,
        group="Contact Infomation",
        option=None)
    Dynafield.objects.create(
        module="Contact",
        name="city",
        type="CharField",
        verbose_name="City",
        fkmodule="Choice",
        on_delete="DO_NOTHING",
        default=None,
        max_length=None,
        group="Contact Infomation",
        option=city)
    Dynafield.objects.create(
        module="Contact",
        name="rate",
        type="CharField",
        verbose_name="Rate",
        fkmodule="Choice",
        on_delete="DO_NOTHING",
        default=None,
        max_length=None,
        group="Contact Infomation",
        option=rate)
    Dynafield.objects.create(
        module="Contact",
        name="source",
        type="CharField",
        verbose_name="Source",
        fkmodule="Choice",
        on_delete="DO_NOTHING",
        default=None,
        max_length=None,
        group="Contact Infomation",
        option=source)
    Dynafield.objects.create(
        module="Contact",
        name="facebook",
        type="CharField",
        verbose_name="Facebook name",
        fkmodule="",
        on_delete="",
        default=None,
        max_length=100,
        group="Facebook Infomation",
        option=None)
    Dynafield.objects.create(
        module="Contact",
        name="facebook_url",
        type="CharField",
        verbose_name="Facebook url",
        fkmodule="",
        on_delete="",
        default=None,
        max_length=200,
        group="Facebook Infomation",
        option=None)


def update_field_backward(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [("choices", "0002_initial_db"), ("app_mgmt", "0001_initial")]

    operations = [migrations.RunPython(update_field_forward, update_field_backward)]
