"""
    App Helper DRY
    App Management
"""
import re

from jinja2 import Template

from risocrm.app_mgmt.models import Dynafield
from risocrm.bases.apps import get_app_label
from risocrm.bases.variables import (BOOL_TYPE, FILE_TYPE, NUMBER_TYPE,
                                     RELATION_TYPE, STRING_TYPE, TIME_TYPE)


def get_group_distinct_tuple(module=""):
    if module != "":
        return [(m, m) for m in Dynafield.objects.filter(module=module).values_list('group', flat=True).distinct()]
    return [(m, m) for m in Dynafield.objects.all().values_list('group', flat=True).distinct()]


def get_group_distinct_list(module=""):
    if module != "":
        return [m for m in Dynafield.objects.filter(module=module).values_list('group', flat=True).distinct()]
    return [m for m in Dynafield.objects.all().values_list('group', flat=True).distinct()]


def get_field_distinct_list(module="", group=""):
    if module != "":
        return [m for m in Dynafield.objects.filter(module=module).filter(group=group).values_list('name', flat=True).distinct()]
    return [m for m in Dynafield.objects.all().values_list('group', flat=True).distinct()]


# Tool for Dynamic and changing Model
####################################
def field_line(field, module):
    """
        Base on type of field
        Return string with their option
        TODO: Need to clean NULL option
    """
    _default = ''
    if field.default is not None:
        _default = F'default={field.default}, '
    if field.type in RELATION_TYPE:
        return F'{field.name} = {field.type}(\
            "{module}.{field.fkmodule}",\
            related_name="%(app_label)s_%(class)s_{field.name}",\
            verbose_name="{field.verbose_name}",\
            {_default}null=True, blank=True)'
    if field.type in STRING_TYPE:
        if field.option is None:
            return F'{field.name} = {field.type}(\
                max_length={field.max_length},\
                verbose_name="{field.verbose_name}",\
                {_default}null=True, blank=True)'
        return F'{field.name} = ForeignKey(\
            "choices.ChoiceDetail",\
            related_name="%(app_label)s_%(class)s_{field.name}",\
            on_delete=DO_NOTHING,\
            verbose_name="{field.verbose_name}",\
            {_default}null=True, blank=True)'
    if field.type in BOOL_TYPE:
        return F'{field.name} = {field.type}(\
            verbose_name="{field.verbose_name}",\
            {_default}blank=True)'
    if field.type in TIME_TYPE:
        return F'{field.name} = {field.type}(\
            auto_now_add=False,\
            editable=True,\
            verbose_name="{field.verbose_name}",\
            {_default}null=True, blank=True)'
    if field.type in NUMBER_TYPE:
        return F'{field.name} = {field.type}(\
            verbose_name="{field.verbose_name}",\
            {_default}null=True, blank=True)'
    if field.type in FILE_TYPE:
        return F'{field.name} = {field.type}(\
            upload_to="uploads/%Y/%m/%d/",\
            verbose_name="{field.verbose_name}",\
            null=True, blank=True)'


def model_render(model, field_list):
    fields = []
    import_fields = 'DO_NOTHING, ForeignKey, '
    module = get_app_label(model)
    for field in field_list:
        _field = re.sub(' +', ' ', field_line(field, module))
        fields.append(_field)
        if field.type not in import_fields:
            import_fields += field.type + ', '
        if field.type in RELATION_TYPE:
            import_fields += F'{field.on_delete},'
    model_path = F'risocrm/{module}/models.py'
    file = open('risocrm/app_mgmt/templates/model_temp', 'r')
    content = file.read()
    templ = Template(content)
    new_content = templ.render({
        'modules': module,
        'fields': fields,
        'import_fields': import_fields[:-2]})
    file = open(model_path, 'w+')
    file.write(new_content)
    file.close()
