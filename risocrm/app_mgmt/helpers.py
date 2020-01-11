"""
    App Helper DRY
    App Management
"""
import re

from django.contrib.contenttypes.models import ContentType
from django.urls import resolve
from jinja2 import Template

from risocrm.app_mgmt.models import Dynafield
from risocrm.bases.global_variables import (BASE_MODEL, BOOL_TYPE, FILE_TYPE,
                                            NUMBER_TYPE, RELATION_TYPE,
                                            STRING_TYPE, TIME_TYPE, ADDED_APP, BASE_USER)


def module_name_list():
    """
        Get all model in ContentType
    """
    return [m.model_class().__name__ for m in ContentType.objects.all()]


def get_app_label(model):
    """
        Get all model in ContentType
    """
    return [m for m in ContentType.objects.all() if m.model_class().__name__ == model][0].app_label


def module_name_tuple():
    """
        Get all model in ContentType
    """
    modules = module_name_list()
    modules = list(set(modules) ^ set(BASE_MODEL+ADDED_APP))
    return [(name, name) for name in modules]


def module_name_full_tuple():
    """
        Get all model in ContentType
    """
    modules = module_name_list()
    return [(name, name) for name in modules]


def module_object_list():
    """
        Get all model name and object in ContentType
    """
    return [(m.model_class().__name__, m.model_class()) for m in ContentType.objects.all()]


def module_label_list():
    """
        Get all model name and object in ContentType
    """
    return [{'label': m.app_label, 'name': m.model_class().__name__} for m in ContentType.objects.all() if m.model_class().__name__ not in BASE_MODEL]


def module_label_tuple():
    """
        Get all model name and object in ContentType
    """
    return [(m.app_label, m.model_class().__name__) for m in ContentType.objects.all() if m.model_class().__name__ not in BASE_MODEL]


def field_list(module):
    """
        Get all field of module
    """
    models = module_object_list()
    return [a[1]._meta.concrete_fields for a in models if a[0] == module][0]
    # return [a[1]._meta.get_fields() for a in models if a[0] == module][0]


def field_name_list(module):
    """
        Get all field name of module
    """
    fields = field_list(module)
    return [field.name for field in fields]


def field_name_tuple(module):
    """
        Get all field name of module
    """
    fields = field_list(module)
    return [(field.name, field.name) for field in fields]


def field_both_name_list(module, fields_name):
    """
        Get field name and verbose name of module and follow list field name
    """
    fields = field_list(module)
    return [{'val': field.name, 'name': field.verbose_name} for field in fields if field.name in fields_name]


def field_both_name_tuple(module):
    """
        Get field name and verbose name of module and follow list field name
    """
    field_names = list(set(field_name_list(module)) ^ set(BASE_USER))
    fields = field_list(module)
    return [(field.name, field.verbose_name) for field in fields if field.name in field_names]


def field_object(module):
    """
        Get field name and object of module
    """
    fields = field_list(module)
    return [(field, field.__class__.__name__) for field in fields]


def get_field_object(module, name):
    """
        Get field name and object of module
    """
    fields = field_list(module)
    return [field for field in fields if field.name == name][0]


def field_detail(module, field):
    """
        Get field object and class name of field
    """
    fields = field_list(module)
    return [(_field, _field.__class__.__name__) for _field in fields if _field.name == field]


def field_type(module, field):
    """
        Get field object and class name of field
    """
    fields = field_list(module)
    field_type_list = [_field.__class__.__name__ for _field in fields if _field.name == field]
    if len(field_type_list) > 0:
        return field_type_list[0]


def get_foreign_module(module, _field):
    curr_module = [m.model_class() for m in ContentType.objects.all() if m.model_class().__name__ == module][0]
    return curr_module._meta.get_field(_field).remote_field.model


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

# Get Contentype ID
###########################


def contentype_from_url(path):
    if path is None:
        return None
    path = '/'+'/'.join(path.split('/')[3:])
    
    app = resolve(path).app_names[0]
    return ContentType.objects.get(app_label=app)
