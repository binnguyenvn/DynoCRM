"""
    App Controller
    App Management
"""
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from risocrm.app_mgmt.forms import DynafieldForm
from risocrm.app_mgmt.helpers import get_group_distinct_tuple, model_render
from risocrm.app_mgmt.models import Dynafield
from risocrm.bases.apps import app_name_tuple, app_name_list
from risocrm.bases.variables import ADDED_APP, BASE_MODEL


@login_required()
def index(request):
    """
        Return all model on project
    """
    content = {
        'page_title': 'App Mangement',
        'table_title': 'Model list',
        'go_back_url': '',
        'go_back_desc': '',
    }
    model_list = app_name_list()
    # Remove Module of System
    content['models'] = list(set(model_list) ^ set(BASE_MODEL + ADDED_APP))

    return render(request, 'app_mgmt-list.html', content)


@login_required()
def view(request):
    """
        View detail field of 1 model
        Input is request parameter ?model=
    """
    model = request.GET.get("model", None)
    if not model:
        return redirect('app_mgmt:index')

    content = {
        'page_title': 'App Management',
        'table_title': 'List field of module' + model,
        'go_back_url': reverse('app_mgmt:index'),
        'go_back_desc': 'Model list',
        'model': model,
    }
    content['obj_list'] = Dynafield.objects.filter(module=model).order_by('group')

    return render(request, 'app_mgmt-view.html', content)


@login_required
def create(request):
    model = request.GET.get("model", "")
    context = {
        'page_title': 'App Mangement',
        'table_title': 'Create new field',
        'go_back_url': reverse('app_mgmt:index'),
        'go_back_desc': 'Model list',
        'model': model
    }

    if request.method == 'GET':
        form = DynafieldForm()
        form.fields['group'].widget.choices = [('', '----------')] + get_group_distinct_tuple(model)
        form.fields['module'].widget.choices = [('', '----------')] + app_name_tuple()
        form.fields['fkmodule'].widget.choices = [('', '----------')] + app_name_tuple()
        context['form'] = form
        return render(request, 'app_mgmt-edit.html', context)
    else:
        form = DynafieldForm(request.POST)
        form.fields['group'].widget.choices = [('', '----------')] + get_group_distinct_tuple(model)
        form.fields['module'].widget.choices = [('', '----------')] + app_name_tuple()
        form.fields['fkmodule'].widget.choices = [('', '----------')] + app_name_tuple()
        if not form.is_valid():
            context['form'] = form
            context['msg_error'] = "Dynafield form have error, please check again!"
            return render(request, 'app_mgmt-edit.html', context)
        else:
            menu = form.save(commit=False)
            menu.creator = request.user
            menu.save()
            model_render(menu.module, Dynafield.objects.filter(module=menu.module))
            messages.add_message(request, messages.SUCCESS, 'Create new field success')
            return redirect('app_mgmt:edit', menu.id)


@login_required
def edit(request, pk):
    obj = get_object_or_404(Dynafield, pk=pk)
    context = {
        'page_title': 'Dynafields',
        'table_title': F'Update {obj.name}',
        'go_back_url': F"{reverse('app_mgmt:view')}?model={obj.module}",
        'go_back_desc': 'Dynafields list',
        'menu': obj,
        'model': obj.module
    }

    if request.method == 'GET':
        form = DynafieldForm(instance=obj)
        form.fields['group'].widget.choices = [('', '----------')] + get_group_distinct_tuple()
        form.fields['module'].widget.choices = [('', '----------')] + app_name_tuple()
        form.fields['fkmodule'].widget.choices = [('', '----------')] + app_name_tuple()
        if obj.option:
            form.fields['default'].widget.choices = [('', '----------')] + [(m.id, m.value)
                                                                            for m in obj.option.choices_detail.all()]
        context['form'] = form
        return render(request, 'app_mgmt-edit.html', context)
    else:
        form = DynafieldForm(request.POST, instance=obj)
        form.fields['group'].widget.choices = [('', '----------')] + get_group_distinct_tuple()
        form.fields['module'].widget.choices = [('', '----------')] + app_name_tuple()
        form.fields['fkmodule'].widget.choices = [('', '----------')] + app_name_tuple()
        if obj.option:
            form.fields['default'].widget.choices = [('', '----------')] + [(m.id, m.value)
                                                                            for m in obj.option.choices_detail.all()]
        if not form.is_valid():
            context['form'] = form
            return render(request, 'app_mgmt-edit.html', context)
        else:
            menu = form.save()
            menu.last_modified_by = request.user
            menu.save()
            model_render(obj.module, Dynafield.objects.filter(module=obj.module))
            messages.add_message(request, messages.SUCCESS, 'Update field success')
            return redirect('app_mgmt:edit', menu.id)


@login_required
def delete(request):
    if request.method == 'POST':
        del_list = request.POST.get('idlist')
        if del_list is not None:
            _del_list = [int(id) for id in del_list[:-1].split(',')]
            for field in _del_list:
                try:
                    obj = Dynafield.objects.get(pk=field)
                    model_render(obj.module, Dynafield.objects.filter(module=obj.module))
                    obj.delete()
                except Exception:
                    raise Http404
    return redirect('app_mgmt:index')
