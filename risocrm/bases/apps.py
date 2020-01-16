from django.contrib.contenttypes.models import ContentType

from risocrm.bases.variables import BASE_MODEL


def app_name_list():
    """
        Get all model in ContentType
    """
    return [m.model_class().__name__ for m in ContentType.objects.all()]


def app_name_tuple():
    """
        Get all model in ContentType
    """
    modules = app_name_list()
    return [(name, name) for name in modules]


def get_app_label(model):
    """
        Get all model in ContentType
    """
    return [m for m in ContentType.objects.all() if m.model_class().__name__ == model][0].app_label


def app_name_object_tuple():
    """
        Get all model name and object in ContentType
    """
    return [(m.model_class().__name__, m.model_class()) for m in ContentType.objects.all()]


def app_label_name_list():
    """
        Get all model name and object in ContentType
    """
    return [{'label': m.app_label, 'name': m.model_class().__name__} for m in ContentType.objects.all() if m.model_class().__name__ not in BASE_MODEL]


def app_label_name_tuple():
    """
        Get all model name and object in ContentType
    """
    return [(m.app_label, m.model_class().__name__) for m in ContentType.objects.all() if m.model_class().__name__ not in BASE_MODEL]


def app_get_foreign_module(module, _field):
    curr_module = [m.model_class() for m in ContentType.objects.all() if m.model_class().__name__ == module][0]
    return curr_module._meta.get_field(_field).remote_field.model
