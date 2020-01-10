from django.conf import settings
from django.db import migrations, models

from risocrm.app_mgmt.models import Dynafield
from risocrm.choices.models import Choice


def update_field_forward(apps, schema_editor):
    city = Choice.objects.get(name="City")
    rate = Choice.objects.get(name="Rate")
    source = Choice.objects.get(name="Source")
    job = Choice.objects.get(name="Job")
    Dynafield.objects.create(
        module="Contact",
        name="name",
        type="CharField",
        verbose_name="Name of contact",
        fkmodule="",
        on_delete="",
        default=None,
        max_length=20,
        group="Contact Infomation",
        option=None,
        is_base=True)
    Dynafield.objects.create(
        module="Contact",
        name="email",
        type="CharField",
        verbose_name="Email",
        fkmodule="",
        on_delete="",
        default=None,
        max_length=20,
        group="Contact Infomation",
        option=None,
        is_base=True)
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
        option=None,
        is_base=True)
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
        option=None,
        is_base=True)
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
        option=city,
        is_base=True)
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
        option=rate,
        is_base=True)
    Dynafield.objects.create(
        module="Contact",
        name="job",
        type="CharField",
        verbose_name="Job",
        fkmodule="Choice",
        on_delete="DO_NOTHING",
        default=None,
        max_length=None,
        group="Contact Infomation",
        option=job,
        is_base=True)
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
        option=source,
        is_base=True)
    Dynafield.objects.create(
        module="Contact",
        name="dob",
        type="DateField",
        verbose_name="Date of Birth",
        fkmodule="",
        on_delete="",
        default=None,
        max_length=None,
        group="Contact Infomation",
        option=None,
        is_base=True)
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
        option=None,
        is_base=True)
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
        option=None,
        is_base=True)
    Dynafield.objects.create(
        module="Contact",
        name="facebook_uid",
        type="CharField",
        verbose_name="Facebook UID",
        fkmodule="",
        on_delete="",
        default=None,
        max_length=200,
        group="Facebook Infomation",
        option=None,
        is_base=True)
    


def update_field_backward(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [("choices", "0002_initial_db"), ("app_mgmt", "0001_initial")]

    operations = [migrations.RunPython(update_field_forward, update_field_backward)]
