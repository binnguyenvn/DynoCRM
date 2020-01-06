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
    
    def __str__(self):
        return "Contact"