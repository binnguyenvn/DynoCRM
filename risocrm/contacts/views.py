"""
    App Controller
    Contacts Management
"""
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from risocrm.contacts.models import Contact
from risocrm.filters.models import Filter

User = get_user_model()


@login_required
def index(request):
    context = {
        'page_title': 'Contacts',
        'table_title': 'List',
        'go_back_url': '',
        'go_back_desc': '',
        'filters': Filter.objects.filter(module='Contact').filter(Q(private=False) | Q(creator=request.user))
    }
    try:
        default_filter = request.user.configs_filterconfig_creator.get(module="Contact")
        context['default_filter'] = default_filter.filter.id
    except Exception:
        pass

    return render(request, 'contacts-list.html', context)


@login_required
def view(request, pk):
    obj = get_object_or_404(Contact, pk=pk)
    context = {
        'page_title': 'Contacts',
        'table_title': F'Update {obj.name}',
        'go_back_url': reverse('contacts:list'),
        'go_back_desc': 'Contacts list',
        'obj': obj,
    }
    return render(request, 'contacts-view.html', context)


@login_required
def create(request):
    context = {
        'page_title': 'Contacts',
        'table_title': 'Create new Contact',
        'go_back_url': reverse('contacts:list'),
        'go_back_desc': 'Contacts list'
    }
    return render(request, 'contacts-create.html', context)


@login_required
def edit(request, pk):
    obj = get_object_or_404(Contact, pk=pk)
    context = {
        'page_title': 'Contacts',
        'table_title': F'Update {obj.name}',
        'go_back_url': reverse('contacts:list'),
        'go_back_desc': 'Contacts list',
        'obj': obj,
    }
    return render(request, 'contacts-edit.html', context)


@login_required
def delete(request):
    if request.method == 'POST':
        del_list = request.POST.get('idlist')
        if del_list is not None:
            _del_list = [int(id) for id in del_list[:-1].split(',')]
            Contact.objects.filter(id__in=_del_list).delete()
    return redirect('contacts:list')
