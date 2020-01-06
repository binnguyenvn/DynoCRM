"""
    App serializer
    Contact serializer
"""

from django.forms import ModelForm, Select, TextInput
from risocrm.contacts.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'