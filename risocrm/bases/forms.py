"""
    Dynamic Form render
"""
from django.forms import (CheckboxInput, DateInput, DateTimeInput, FileInput,
                          NumberInput, Select, SelectMultiple, TextInput,
                          TimeInput, modelform_factory)
from django.urls import reverse

from risocrm.app_mgmt.helpers import (get_field_distinct_list,
                                      get_field_object,
                                      get_group_distinct_list)
from risocrm.bases.global_variables import (BOOL_TYPE, FILE_TYPE, NUMBER_TYPE,
                                            STRING_TYPE)
from risocrm.app_mgmt.models import Dynafield

DATE_TYPE = ['DateField']
DATETIME_TYPE = ['DateTimeField']
TIME_TYPE = ['TimeField']
ONE_TYPE = ['ForeignKey', 'OneToOneField']
TWO_TYPE = ['ManyToManyField']


def get_type(model, name):
    _type = get_field_object(model, name)
    if _type.get_internal_type() in BOOL_TYPE:
        return CheckboxInput(attrs={'class': 'bool-field form-control'})

    if _type.get_internal_type() in FILE_TYPE:
        return FileInput(attrs={'class': 'file-field form-control'})

    if _type.get_internal_type() in NUMBER_TYPE:
        return NumberInput(attrs={'class': 'number-field form-control'})

    if _type.get_internal_type() in ONE_TYPE:
        related_model = _type.related_model.__module__.split(".")[1]
        if related_model == 'choices':
            _field = Dynafield.objects.filter(module=model).filter(name=name).first()
            url = reverse(F'{related_model}:edit', kwargs={'pk': _field.option.id})
            refresh_url = reverse(F'{_type.related_model.__module__.split(".")[1]}:choice_childs', kwargs={'pk': _field.option.id})
        else:
            url = reverse(F'{related_model}:create')
            refresh_url = reverse(F'{_type.related_model.__module__.split(".")[1]}:create')
        return Select(attrs={'class': 'relation-field form-control kt-select2', 'fk':name, 'created': url, 'refresh': refresh_url})

    if _type.get_internal_type() in TWO_TYPE:
        url = reverse(F'{_type.related_model.__module__.split(".")[1]}:create')
        refresh_url = reverse(F'{_type.related_model.__module__.split(".")[1]}:create')
        return SelectMultiple(attrs={'class': 'relation-field form-control kt-select2', 'fk':name, 'created': url, 'refresh': refresh_url})

    if _type.get_internal_type() in STRING_TYPE:
        return TextInput(attrs={'class': 'string-field form-control'})

    if _type.get_internal_type() in DATE_TYPE:
        return DateInput(attrs={'class': 'date-field form-control', 'placeholder': 'Select date'})

    if _type.get_internal_type() in DATETIME_TYPE:
        return DateTimeInput(attrs={'class': 'datetime-field form-control', 'placeholder': 'Select date & time'})

    if _type.get_internal_type() in TIME_TYPE:
        return TimeInput(attrs={'class': 'time-field form-control', 'placeholder': 'Select time'})

    return TextInput()


def DynoForm(model, module):
    groups = get_group_distinct_list(model)
    hidden_fields = [
        'creator',
        'last_modified_by']
    forms = [
        {
            'group': 'Hidden',
            'form': modelform_factory(
                module,
                fields=hidden_fields,
                widgets={
                    'creator': TextInput(attrs={'class': 'd-none'}),
                    'last_modified_by': TextInput(attrs={'class': 'd-none'})
                }
            )
        }
    ]
    for group in groups:
        fields = get_field_distinct_list(model, group)
        widgets = {name: get_type(model, name) for name in fields}
        forms.append(
            {
                'group': group,
                'form': modelform_factory(module, fields=fields, widgets=widgets)
            }
        )
    return forms
