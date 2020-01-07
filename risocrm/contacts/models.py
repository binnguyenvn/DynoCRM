"""
    App Models
    Contact model
"""
from django.db.models import DO_NOTHING, ForeignKey, CharField

from risocrm.bases.models import BaseModel


class Contact(BaseModel):
    """
        Contact
    """
    
    email = CharField( max_length=20, verbose_name="Email", null=True, blank=True)
    phone = CharField( max_length=20, verbose_name="Phone number", null=True, blank=True)
    address = CharField( max_length=1000, verbose_name="Address", null=True, blank=True)
    city = ForeignKey( "choices.ChoiceDetail", related_name="%(app_label)s_%(class)s_city", on_delete=DO_NOTHING, verbose_name="City", null=True, blank=True)
    rate = ForeignKey( "choices.ChoiceDetail", related_name="%(app_label)s_%(class)s_rate", on_delete=DO_NOTHING, verbose_name="Rate", null=True, blank=True)
    source = ForeignKey( "choices.ChoiceDetail", related_name="%(app_label)s_%(class)s_source", on_delete=DO_NOTHING, verbose_name="Source", null=True, blank=True)
    facebook = CharField( max_length=100, verbose_name="Facebook name", null=True, blank=True)
    facebook_url = CharField( max_length=200, verbose_name="Facebook url", null=True, blank=True)
    name = CharField( max_length=200, verbose_name="Name of contact", null=True, blank=True)
    def __str__(self):
        return "Contact"