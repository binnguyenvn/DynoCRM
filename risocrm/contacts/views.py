"""
    App Controller
    Contacts Management
"""
import string

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from risocrm.app_mgmt.helpers import get_group_distinct_list
from risocrm.app_mgmt.models import Dynafield
from risocrm.bases.fields import app_field_name_list
from risocrm.bases.forms import DynoForm
from risocrm.bases.variables import BASE_FIELD
from risocrm.configs.models import ExternalConfig, FieldConfig, ReportConfig
from risocrm.contacts.forms import ContactForm
from risocrm.contacts.models import Contact
from risocrm.contacts.tasks import import_contact
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
    try:
        obj = Contact.objects.filter(pk=pk).select_related('city').first()
    except Exception:
        messages.add_message(request, messages.ERROR, 'Contact not found')
        return redirect('contacts:list')

    groups = get_group_distinct_list('Contact')
    groups = [{'group': group, 'fields': Dynafield.objects.filter(group=group)} for group in groups]
    context = {
        'page_title': 'Contacts',
        'table_title': F'Update {obj.name}',
        'go_back_url': reverse('contacts:list'),
        'go_back_desc': 'Contacts list',
        'obj': obj,
        'fields': FieldConfig.objects.filter(creator=request.user).filter(module='Contact'),
        'externals': ExternalConfig.objects.filter(module='Contact'),
        'reports': ReportConfig.objects.filter(module='Contact'),
        'groups': groups
    }
    return render(request, 'contacts-view.html', context)


@login_required
def create(request):
    context = {
        'page_title': 'Contacts',
        'table_title': 'Create new Contact',
        'go_back_url': reverse('contacts:list'),
        'go_back_desc': 'Contacts list',
    }
    if request.method == 'GET':
        context['forms'] = DynoForm('Contact', Contact)
        return render(request, 'contacts-edit.html', context)
    else:
        real_form = ContactForm(request.POST)
        if not real_form.is_valid():
            forms = DynoForm('Contact', Contact)
            for form in forms:
                form['form'] = form['form'](initial=real_form.data)
            context['forms'] = forms
            context['msg_error'] = "Contact form have error, please check again!"
            return render(request, 'contacts-edit.html', context)
        else:
            contact = real_form.save(commit=False)
            contact.creator = request.user
            contact.last_modified_by = request.user
            contact.save()
            messages.add_message(request, messages.SUCCESS, F'Create contact {contact.name} success')
            return redirect('contacts:edit', contact.id)


@login_required
def edit(request, pk):
    obj = get_object_or_404(Contact, pk=pk)
    context = {
        'page_title': 'Contacts',
        'table_title': F'Update {obj.name}',
        'go_back_url': reverse('contacts:list'),
        'go_back_desc': 'Contacts list',
        'obj': obj,
        'pk': pk
    }
    if request.method == 'GET':
        forms = DynoForm('Contact', Contact)
        for form in forms:
            form['form'] = form['form'](instance=obj)
        context['forms'] = forms
        return render(request, 'contacts-edit.html', context)
    else:
        real_form = ContactForm(request.POST, instance=obj)
        if not real_form.is_valid():
            forms = DynoForm('Contact', Contact)
            for form in forms:
                form['form'] = form['form'](instance=obj)
            context['forms'] = forms
            context['msg_error'] = "Contact form have error, please check again!"
            return render(request, 'contacts-edit.html', context)
        else:
            contact = real_form.save(commit=False)
            contact.last_modified_by = request.user
            contact.save()
            messages.add_message(request, messages.SUCCESS, F'Update contact {obj.name} success')
            return redirect('contacts:edit', contact.id)


@login_required
def delete(request):
    if request.method == 'POST':
        del_list = request.POST.get('idlist')
        if del_list is not None:
            _del_list = [id for id in del_list[:-1].split(',')]
            Contact.objects.filter(id__in=_del_list).delete()
    return redirect('contacts:list')


@login_required
def importcontacts(request):
    context = {
        'page_title': 'Contacts',
        'table_title': 'Import contact',
        'go_back_url': reverse('contacts:list'),
        'go_back_desc': 'Contacts list',
    }
    if request.method == 'GET':
        alpha = list(string.ascii_uppercase)
        fields = list(set(app_field_name_list('Contact')) ^ set(BASE_FIELD))
        context['format'] = [{'col': a, 'field': b} for a, b in zip(alpha, sorted(fields))]
        return render(request, 'contacts-import.html', context)
    else:
        file = request.FILES['file']
        file_name = default_storage.save(file.name, file)
        url = default_storage.url(file_name)
        import_contact.delay(url, request.user)
        messages.add_message(request, messages.SUCCESS,
                             'Import contact is in progress, system will notice to you when its finish')
        return redirect('contacts:list')


@login_required
def exportcontacts(request):

    messages.add_message(request, messages.SUCCESS,
                         'Export contact is in progress, system will notice to you when its finish')
    return redirect('contacts:list')
