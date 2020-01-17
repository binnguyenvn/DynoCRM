"""
    App Celery Task
    Contact Management
"""
import string

import requests
from django.urls import reverse

from config import celery_app
from openpyxl import load_workbook
from risocrm.app_mgmt.models import Dynafield
from risocrm.bases.fields import app_field_name_list, app_get_field_object
from risocrm.bases.variables import BASE_FIELD, RELATION_TYPE
from risocrm.notices.models import Notice
from risocrm.contacts.serializers import internalContactSerializer

@celery_app.task()
def import_contact(url, user):
    req = requests.get(url)
    with open('Contact.xlsx', 'wb') as f:
        f.write(req.content)

    fields = sorted(list(set(app_field_name_list('Contact')) ^ set(BASE_FIELD)))

    anony = []
    for field in fields:
        _type = app_get_field_object('Contact', field)
        if _type.get_internal_type() in RELATION_TYPE:
            anony.append(field)

    workbook = load_workbook(filename=f.name)
    sheet = workbook.active

    data = []
    for row in sheet:
        field = {a: b.value for a, b in zip(fields, row)}
        data.append(field)

    for item in data:
        item['creator_id'] = user.id
        item['last_modified_by_id'] = user.id
        for field in fields:
            _type = app_get_field_object('Contact', field)
            if field in anony:
                try:
                    _field = Dynafield.objects.filter(module='Contact').filter(name=field).first()
                    if _type.related_model.__module__.split(".")[1] == 'choices':
                        obj, created = _type.related_model.objects.get_or_create(choice_id=_field.option.id, value=item[field])
                    else:
                        obj, created = _type.related_model.objects.get_or_create(name=item[field])
                    item[field] = obj.id
                except Exception:
                    pass
            else:
                f_type = _type.get_internal_type()
                if f_type == 'DateField':
                    item[field] = item[field].date()
                elif f_type == 'TimeField':
                    item[field] = item[field].time()
                else:
                    pass

    serializer = internalContactSerializer(data=data, many=True)
    if serializer.is_valid():
        serializer.save()
        Notice.objects.create(
            content='Import Contact is completed',
            to_user=user,
            type='flaticon2-gear',
            url=reverse('contacts:list')
        )
    else:
        ble = serializer.errors
        Notice.objects.create(
            content='Something went wrong, Please check your file',
            to_user=user,
            type='flaticon2-gear',
            url=reverse('contacts:list')
        )
