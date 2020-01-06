"""
    App Celery Task
    Contact Management
"""
from config import celery_app

from risocrm.contacts.models import Contact


# @celery_app.task()
# def get_contact_count():
#     """A pointless Celery task to demonstrate usage."""
#     return Contact.objects.count()
