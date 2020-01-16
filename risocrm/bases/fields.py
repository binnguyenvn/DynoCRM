from risocrm.bases.apps import app_name_object_tuple
from risocrm.bases.variables import BASE_USER


def app_field_list(module):
    """
        Get all field of module
    """
    models = app_name_object_tuple()
    return [a[1]._meta.concrete_fields for a in models if a[0] == module][0]
    # return [a[1]._meta.get_fields() for a in models if a[0] == module][0]


def app_field_name_list(module):
    """
        Get all field name of module
    """
    fields = app_field_list(module)
    return [field.name for field in fields]


def app_field_name_tuple(module):
    """
        Get all field name of module
    """
    fields = app_field_list(module)
    return [(field.name, field.name) for field in fields]


def app_filter_field_name_vname_list(module, fields_name):
    """
        Get field name and verbose name of module and follow list field name
    """
    fields = app_field_list(module)
    return [{'val': field.name, 'name': field.verbose_name} for field in fields if field.name in fields_name]


def app_field_name_vname_tuple(module):
    """
        Get field name and verbose name of module and follow list field name
    """
    field_names = list(set(app_field_name_list(module)) ^ set(BASE_USER))
    fields = app_field_list(module)
    return [(field.name, field.verbose_name) for field in fields if field.name in field_names]


def app_field_name_vname_exclue_base_dict(module):
    """
        Get field name and verbose name of module and follow list field name
    """
    field_names = list(set(app_field_name_list(module)) ^ set(BASE_USER))
    fields = app_field_list(module)
    return {field.name: field.verbose_name for field in fields if field.name in field_names}



def app_get_field_object(module, name):
    """
        Get field name and object of module
    """
    fields = app_field_list(module)
    return [field for field in fields if field.name == name][0]


def app_get_field_type(module, field):
    """
        Get field object and class name of field
    """
    fields = app_field_list(module)
    field_type_list = [_field.__class__.__name__ for _field in fields if _field.name == field]
    if len(field_type_list) > 0:
        return field_type_list[0]
