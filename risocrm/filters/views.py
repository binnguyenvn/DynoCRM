"""
    App Controller
    Filters
"""

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from risocrm.bases.apps import app_name_tuple
from risocrm.bases.fields import app_field_name_tuple
from risocrm.configs.models import FilterConfig
from risocrm.filters.forms import FilterDetailFS, FilterForm
from risocrm.filters.models import Filter

User = get_user_model()


@login_required
def index(request):
    module = request.GET.get("model", None)
    context = {
        'page_title': 'Filters',
        'table_title': 'List',
        'go_back_url': '',
        'go_back_desc': '',
    }
    if module:
        response = Filter.objects.filter(creator=request.user).filter(module=module)
    else:
        response = Filter.objects.filter(creator=request.user)
    context['obj_list'] = response
    return render(request, 'filters-list.html', context)


@login_required
def create(request):
    context = {
        'page_title': 'Filters',
        'table_title': 'Create new Filter',
        'go_back_url': reverse('filters:list'),
        'go_back_desc': 'Filters list'
    }
    _filter = Filter()
    if request.method == 'GET':
        form = FilterForm()
        form.fields['module'].widget.choices = [('', '----------')] + app_name_tuple()
        context['form'] = form
        context['formset'] = FilterDetailFS(instance=_filter)
        return render(request, 'filters-edit.html', context)
    else:
        form = FilterForm(request.POST)
        if not form.is_valid():
            form.fields['module'].widget.choices = [('', '----------')] + app_name_tuple()
            form.fields['order_by'].widget.choices = [('', '----------')] + app_field_name_tuple(form.data['module'])
            form.fields['field_list'].widget.choices = [('', '----------')] + app_field_name_tuple(form.data['module'])
            context['form'] = form
            context['formset'] = FilterDetailFS(request.POST, instance=_filter)
            context['msg_error'] = "Filter form have error, please check again!"
            return render(request, 'filters-edit.html', context)
        else:
            filter = form.save(commit=False)
            formset = FilterDetailFS(request.POST, instance=filter)
            for _form in formset:
                if not _form.is_valid():
                    form.fields['module'].widget.choices = [('', '----------')] + app_name_tuple()
                    form.fields['order_by'].widget.choices = [
                        ('', '----------')] + app_field_name_tuple(form.data['module'])
                    form.fields['field_list'].widget.choices = [
                        ('', '----------')] + app_field_name_tuple(form.data['module'])
                    context['form'] = form
                    context['formset'] = FilterDetailFS(request.POST, instance=_filter)
                    context['msg_error'] = "Detail form have error, please check again!"
                    return render(request, 'filters-edit.html', context)
            with transaction.atomic():
                filter.field_list = ','.join(request.POST.getlist('field_list'))
                filter.creator = request.user
                filter.save()
                formset.save()
                if request.POST.get('default'):
                    conf = FilterConfig.objects.filter(creator=request.user).filter(
                        module=form.data['module']).first()
                    if conf:
                        conf.filter = filter
                        conf.save()
                    else:
                        FilterConfig.objects.create(creator=request.user, module=form.data['module'], filter=filter)
                messages.add_message(request, messages.SUCCESS, 'Create new filter success')
                return redirect('filters:edit', filter.id)


@login_required
def edit(request, pk):
    filter_obj = get_object_or_404(Filter, pk=pk)
    context = {
        'page_title': 'Filters',
        'table_title': F'Update {filter_obj.name}',
        'go_back_url': reverse('filters:list'),
        'go_back_desc': 'Filters list',
        'filter': filter_obj,
    }
    if request.method == 'GET':
        form = FilterForm(instance=filter_obj)
        form.fields['module'].widget.choices = [('', '----------')] + app_name_tuple()
        form.fields['order_by'].widget.choices = [('', '----------')] + app_field_name_tuple(filter_obj.module)
        form.fields['field_list'].widget.choices = [('', '----------')] + app_field_name_tuple(filter_obj.module)
        context['form'] = form
        formset = FilterDetailFS(instance=filter_obj)
        for form in formset:
            form.fields['field_name'].widget.choices = [('', '----------')] + app_field_name_tuple(filter_obj.module)
        context['formset'] = formset
        return render(request, 'filters-edit.html', context)
    else:
        form = FilterForm(request.POST, instance=filter_obj)
        if not form.is_valid():
            context['form'] = form
            context['formset'] = FilterDetailFS(request.POST, instance=filter_obj)
            context['msg_error'] = "Form have error, please check again!"
            return render(request, 'filters-edit.html', context)
        else:
            formset = FilterDetailFS(request.POST, instance=filter_obj)
            if not formset.is_valid():
                context['form'] = form
                context['formset'] = FilterDetailFS(request.POST, instance=filter_obj)
                context['msg_error'] = "Formset have error, please check again!"
                return render(request, 'filters-edit.html', context)
            else:
                filter = form.save(commit=False)
                filter.field_list = ','.join(request.POST.getlist('field_list'))
                filter.last_modified_by = request.user
                formset.save()
                filter.save()
                if request.POST.get('default'):
                    conf = FilterConfig.objects.filter(creator=request.user).filter(
                        module=form.data['module']).first()
                    if conf:
                        conf.filter = filter
                        conf.save()
                    else:
                        FilterConfig.objects.create(creator=request.user, module=form.data['module'], filter=filter)
                messages.add_message(request, messages.SUCCESS, 'pdate Filter success')
                return redirect('filters:edit', filter.id)


@login_required
def delete(request):
    if request.method == 'POST':
        del_list = request.POST.get('idlist')
        if del_list is not None:
            _del_list = [int(id) for id in del_list[:-1].split(',')]
            Filter.objects.filter(id__in=_del_list).delete()
    return redirect('filters:list')
