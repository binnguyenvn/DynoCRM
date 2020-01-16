"""
    App Controller
    Dashboard
"""
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from risocrm.bases.apps import app_name_tuple
from risocrm.dashboard.forms import TileDetailFS, TileForm, TileFS
from risocrm.dashboard.helpers import get_group_distinct_tuple
from risocrm.dashboard.models import Tile

User = get_user_model()


@login_required()
def dashboard(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    context = {
        'page_title': 'Dashboard',
        'table_title': '',
        'go_back_url': '',
        'go_back_desc': '',
        'obj_list': ''
    }

    return render(request, 'dashboard.html', context)


@login_required
def index(request):
    context = {
        'page_title': 'Dashboards',
        'table_title': 'List',
        'go_back_url': '',
        'go_back_desc': '',
        'obj_list': Tile.objects.all()
    }
    return render(request, 'dashboard-list.html', context)


@login_required
def create(request):
    context = {
        'page_title': 'Dashboards',
        'table_title': 'Create new Tile',
        'go_back_url': reverse('dashboard:list'),
        'go_back_desc': 'Dashboard list'
    }
    _tile = Tile()
    if request.method == 'GET':
        form = TileForm()
        form.fields['dashboard'].widget.choices = [('', '----------')] + get_group_distinct_tuple()
        form.fields['module'].widget.choices = [('', '----------')] + app_name_tuple()
        context['form'] = form
        context['formset'] = TileDetailFS(instance=_tile)
        return render(request, 'dashboard-edit.html', context)
    else:
        form = TileForm(request.POST)
        if not form.is_valid():
            form.fields['dashboard'].widget.choices = [('', '----------')] + get_group_distinct_tuple()
            form.fields['module'].widget.choices = [('', '----------')] + app_name_tuple()
            context['form'] = form
            context['formset'] = TileDetailFS(request.POST, instance=_tile)
            context['msg_error'] = "Dashboard form have error, please check again!"
            return render(request, 'dashboard-edit.html', context)
        else:
            tile = form.save(commit=False)
            formset = TileDetailFS(instance=tile)

            with transaction.atomic():
                tile.creator = request.user
                tile.save()
                formset.save()
                messages.add_message(request, messages.SUCCESS, 'Create new tile success')
                return redirect('dashboard:view', tile.id)


@login_required
def edit(request, pk):
    tile_obj = get_object_or_404(Tile, pk=pk)
    context = {
        'page_title': 'Dashboards',
        'table_title': F'Update {tile_obj.name}',
        'go_back_url': reverse('dashboard:list'),
        'go_back_desc': 'Dashboards list',
        'tile': tile_obj,
    }
    if request.method == 'GET':
        form = TileForm(instance=tile_obj)
        form.fields['dashboard'].widget.choices = [('', '----------')] + get_group_distinct_tuple()
        form.fields['module'].widget.choices = [('', '----------')] + app_name_tuple()
        context['form'] = form
        context['formset'] = TileDetailFS(instance=tile_obj)
        return render(request, 'dashboard-edit.html', context)
    else:
        form = TileForm(request.POST, instance=tile_obj)
        if not form.is_valid():
            form.fields['dashboard'].widget.choices = [('', '----------')] + get_group_distinct_tuple()
            form.fields['module'].widget.choices = [('', '----------')] + app_name_tuple()
            context['form'] = form
            context['formset'] = TileDetailFS(request.POST, instance=tile_obj)
            context['msg_error'] = "Dashboard form have error, please check again!"
            return render(request, 'dashboard-edit.html', context)
        else:
            formset = TileDetailFS(request.POST, instance=tile_obj)
            if not formset.is_valid():
                form.fields['dashboard'].widget.choices = [('', '----------')] + get_group_distinct_tuple()
                form.fields['module'].widget.choices = [('', '----------')] + app_name_tuple()
                context['form'] = form
                context['formset'] = TileDetailFS(request.POST, instance=tile_obj)
                context['msg_error'] = "Dashboard formset have error, please check again!"
                return render(request, 'dashboard-edit.html', context)
            else:
                tile = form.save(commit=False)
                tile.last_modified_by = request.user
                tile.save()
                formset.save()
                messages.add_message(request, messages.SUCCESS, 'Create new tile success')
                return redirect('dashboard:edit', tile.id)


@login_required
def delete(request):
    if request.method == 'POST':
        del_list = request.POST.get('idlist')
        if del_list is not None:
            _del_list = [int(id) for id in del_list[:-1].split(',')]
            Tile.objects.filter(id__in=_del_list).delete()
    return redirect('dashboard:list')
