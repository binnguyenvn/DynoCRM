"""
    App Controller
    Configs Management
"""
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import redirect, render

from risocrm.app_mgmt.helpers import module_label_tuple, module_name_tuple
from risocrm.configs.forms import ExternalConfigFS, ReportConfigFS, FieldConfigFS
from risocrm.configs.models import ExternalConfig, FieldConfig, ReportConfig


@login_required
def external(request, pk):
    obj_list = ExternalConfig.objects.filter(module=pk)
    context = {
        'page_title': 'External Configs',
        'table_title': F'Update external configs of {pk}',
        'go_back_url': request.META.get('HTTP_REFERER', None) or '/',
        'go_back_desc': 'Back',
        'module': pk
    }
    external = module_label_tuple()
    if request.method == 'GET':
        formset = ExternalConfigFS(initial=[
            {
                'last_modified_by': request.user,
                'module': pk
            }
        ],
            queryset=obj_list
        )
        for form in formset:
            form.fields['external'].widget.choices = [('', '----------')] + external
        context['formset'] = formset
        return render(request, 'configs-external.html', context)
    else:
        formset = ExternalConfigFS(request.POST, queryset=obj_list)
        if not formset.is_valid():
            formset = ExternalConfigFS(request.POST, queryset=obj_list)
            for form in formset:
                form.fields['external'].widget.choices = [('', '----------')] + external
            context['formset'] = formset
            context['msg_error'] = F"Formset have error, please check again! {formset.errors}"
            return render(request, 'configs-external.html', context)
        instances = formset.save(commit=False)
        for instance in instances:
            if instance.id is None:
                instance.creator = request.user
            instance.save()
        messages.add_message(request, messages.SUCCESS, 'Update external config success')
        return redirect('configs:external', pk)


@login_required
def report(request, pk):
    obj_list = ReportConfig.objects.filter(module=pk)
    context = {
        'page_title': 'Report Configs',
        'table_title': F'Update report configs of {pk}',
        'go_back_url': request.META.get('HTTP_REFERER', None) or '/',
        'go_back_desc': 'Back',
        'module': pk
    }
    report = module_label_tuple()
    if request.method == 'GET':
        formset = ReportConfigFS(initial=[
            {
                'last_modified_by': request.user,
                'module': pk
            }
        ],
            queryset=obj_list
        )
        for form in formset:
            form.fields['field'].widget.choices = [('', '----------')] + report
        context['formset'] = formset
        return render(request, 'configs-report.html', context)
    else:
        formset = ReportConfigFS(request.POST, queryset=obj_list)
        if not formset.is_valid():
            formset = ReportConfigFS(request.POST, queryset=obj_list)
            for form in formset:
                form.fields['field'].widget.choices = [('', '----------')] + report
            context['formset'] = formset
            context['msg_error'] = F"Formset have error, please check again! {formset.errors}"
            return render(request, 'configs-report.html', context)
        instances = formset.save(commit=False)
        for instance in instances:
            if instance.id is None:
                instance.creator = request.user
            instance.save()
        messages.add_message(request, messages.SUCCESS, 'Update report config success')
        return redirect('configs:report', pk)


@login_required
def field(request, pk):
    obj_list = FieldConfig.objects.filter(module=pk)
    context = {
        'page_title': 'Field Configs',
        'table_title': F'Update field configs of {pk}',
        'go_back_url': request.META.get('HTTP_REFERER', None) or '/',
        'go_back_desc': 'Back',
        'module': pk
    }
    field = module_label_tuple()
    if request.method == 'GET':
        formset = FieldConfigFS(initial=[
            {
                'last_modified_by': request.user,
                'module': pk
            }
        ],
            queryset=obj_list
        )
        for form in formset:
            form.fields['field'].widget.choices = [('', '----------')] + field
        context['formset'] = formset
        return render(request, 'configs-field.html', context)
    else:
        formset = FieldConfigFS(request.POST, queryset=obj_list)
        if not formset.is_valid():
            formset = FieldConfigFS(request.POST, queryset=obj_list)
            for form in formset:
                form.fields['field'].widget.choices = [('', '----------')] + field
            context['formset'] = formset
            context['msg_error'] = F"Formset have error, please check again! {formset.errors}"
            return render(request, 'configs-field.html', context)
        instances = formset.save(commit=False)
        for instance in instances:
            if instance.id is None:
                instance.creator = request.user
            instance.save()
        messages.add_message(request, messages.SUCCESS, 'Update field config success')
        return redirect('configs:field', pk)
