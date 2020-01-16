"""
    App Celery Task
    Contact Management
"""
import string

import requests
from django.urls import reverse

from config import celery_app
from openpyxl import load_workbook
from risocrm.bases.fields import app_field_name_list
from risocrm.bases.variables import BASE_FIELD
from risocrm.contacts.models import Contact
from risocrm.notices.models import Notice


@celery_app.task()
def import_contact(url, user):
    req = requests.get(url)
    with open('/Users/scott/Downloads/cat3.jpg', 'wb') as f:
        f.write(req.content)

    fields = sorted(list(set(app_field_name_list('Contact')) ^ set(BASE_FIELD)))

    workbook = load_workbook(filename=f.name)
    sheet = workbook.active

    Notice.objects.create(
        content='',
        to_user=user,
        type='flaticon2-gear',
        url=reverse('contacts:list')
    )
