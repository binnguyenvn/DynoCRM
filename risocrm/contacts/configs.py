"""
    App Config
    Contacts Management
"""
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from risocrm.contacts.forms import ContactForm
from risocrm.contacts.models import Contact

User = get_user_model()


@login_required
def model_index(request):
    context = {
        'page_title': 'Contact Model',
        'table_title': 'List',
        'go_back_url': '',
        'go_back_desc': '',
        'obj_list': [],
    }
    return render(request, 'models-list.html', context)


@login_required
def model_create(request):
    context = {
        'page_title': 'Contacts',
        'table_title': 'Create new Contact',
        'go_back_url': reverse('contacts:index'),
        'go_back_desc': 'Contacts list'
    }
    if request.method == 'GET':
        context['form'] = ContactForm()
        return render(request, 'models-detail.html', context)
    else:
        form = ContactForm(request.POST)
        if not form.is_valid():
            context['form'] = form
            return render(request, 'models-detail.html', context)
        else:
            contact = form.save()
            contact.creator = request.user
            contact.save()
            messages.add_message(request, messages.SUCCESS, 'Create new Contact success')
            return redirect(request.META.get('HTTP_REFERER'))


@login_required
def model_edit(request, pk):
    contact_obj = get_object_or_404(Contact, pk=pk)
    context = {
        'page_title': 'Contacts',
        'table_title': 'Update contact_obj.name',
        'go_back_url': reverse('contacts:index'),
        'go_back_desc': 'Contacts list',
        'contact': contact_obj,
    }
    if request.method == 'GET':
        context['form'] = ContactForm(instance=contact_obj)
        return render(request, 'models-detail.html', context)
    else:
        form = ContactForm(request.POST, instance=contact_obj)
        if not form.is_valid():
            context['form'] = form
            return render(request, 'models-detail.html', context)
        else:
            contact = form.save()
            contact.last_modified_by = request.user
            contact.save()
            messages.add_message(request, messages.SUCCESS, 'Update Contact success')
            return redirect('contacts:edit', contact.id)


@login_required
def model_view(request, pk):
    contact_obj = get_object_or_404(Contact, pk=pk)
    context = {
        'page_title': 'Contacts',
        'table_title': 'Update contact_obj.name',
        'go_back_url': reverse('contacts:index'),
        'go_back_desc': 'Contacts list',
        'contact': contact_obj,
    }
    context['form'] = ContactForm(instance=contact_obj)
    return render(request, 'models-detail.html', context)


@login_required
def model_delete(request):
    if request.method == 'POST':
        del_list = request.POST.get('idlist')
        del_obj = request.POST.get('idsingle')
        if del_obj is not None:
            try:
                obj = Contact.objects.get(pk=int(del_obj))
                obj.delete()
            except Exception:
                raise Http404
        elif del_list is not None:
            _del_list = del_list.split(',')
            for item in _del_list:
                try:
                    obj = Contact.objects.get(pk=int(item))
                    obj.delete()
                except Exception:
                    raise Http404
    return redirect('contacts:list')
