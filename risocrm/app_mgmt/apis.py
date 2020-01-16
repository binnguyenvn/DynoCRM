"""
    App Public API
    App Management
"""
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from risocrm.bases.contenttype import contentype_from_url
from risocrm.bases.apps import app_label_name_list, app_name_list, app_get_foreign_module
from risocrm.bases.commands import *
from risocrm.bases.fields import (app_field_name_list,
                                  app_field_name_vname_exclue_base_dict,
                                  app_filter_field_name_vname_list,
                                  app_get_field_type)
from risocrm.bases.variables import ADDED_APP, BASE_MODEL, BASE_USER


@login_required
def make_migrations(request):
    return JsonResponse({'data': Make_Migration()}, status=200)


@login_required
def migrate(request):
    return JsonResponse({'data': Migrate()}, status=200)


@login_required
def get_module(request):
    """
        Get list model name which can use filter
    """
    modules = app_name_list()
    modules = list(set(modules) ^ set(BASE_MODEL+ADDED_APP))
    return JsonResponse({'data': modules}, status=200)


@login_required
def get_label(request):
    """
        Get list model name which can use filter
    """
    return JsonResponse({'data': app_label_name_list()}, status=200)


@login_required
def get_field(request):
    """
        Get list field of model
        paramete ?model=
    """
    model = request.GET.get("model", None)
    if not model:
        return JsonResponse({'data': 'missing'}, status=400)

    # get field list
    try:
        field_names = list(set(app_field_name_list(model)) ^ set(BASE_USER))
        return JsonResponse({'data': app_filter_field_name_vname_list(model, field_names)}, status=200)
    except Exception:
        return JsonResponse({'data': 'try catch'}, status=400)


@login_required
def get_field_type(request):
    """
        Get list field of model
        paramete ?model= & field name
    """
    model = request.GET.get("model", None)
    field = request.GET.get("field", None)
    if not model or not field:
        return JsonResponse({'data': 'missing'}, status=400)

    try:
        return JsonResponse({'data': app_get_field_type(model, field)}, status=200)
    except Exception:
        return JsonResponse({'data': 'try catch'}, status=400)


@login_required
def get_field_label(request):
    """
        Get list field of model
        paramete ?model= & field name
    """
    path = request.META.get('HTTP_REFERER', None) or '/'
    content_type = contentype_from_url(path)
    if content_type is None:
        return JsonResponse({'data': 'Cannot find Model'}, status=400)
    try:
        return JsonResponse({'data': app_field_name_vname_exclue_base_dict(content_type.model.title())}, status=200)
    except Exception:
        return JsonResponse({'data': content_type.model.title()}, status=400)


def get_foreign_data(request):
    """
        Get obj list or return None
    """
    model = request.GET.get("model", None)
    field = request.GET.get("field", None)
    if not model or not field:
        return JsonResponse({'data': 'missing'}, status=400)

    try:
        models = get_foreign_module(model, field).objects.all().values()
        return JsonResponse({'data': list(models)}, status=200)
    except Exception:
        return JsonResponse({'data': 'try catch'}, status=400)
