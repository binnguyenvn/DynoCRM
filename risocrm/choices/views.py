"""
    App Controller
    Choices Management
"""

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from risocrm.choices.forms import ChoiceDetailFS, ChoiceForm
from risocrm.choices.models import Choice

User = get_user_model()


@login_required
def index(request):
    context = {
        'page_title': 'Choices',
        'table_title': 'List',
        'go_back_url': '',
        'go_back_desc': '',
        'obj_list': Choice.objects.all()
    }
    return render(request, 'choices-list.html', context)


@login_required
def view(request, pk):
    obj = get_object_or_404(Choice, pk=pk)
    context = {
        'page_title': 'Choices',
        'table_title': F'Detail {obj.name}',
        'go_back_url': reverse('choices:list'),
        'go_back_desc': 'Choices list',
        'obj': obj,
        'choices': obj.choices_detail.all()
    }
    return render(request, 'choices-view.html', context)


@login_required
def create(request):
    context = {
        'page_title': 'Choices',
        'table_title': 'Create new Choice',
        'go_back_url': reverse('choices:list'),
        'go_back_desc': 'Choices list'
    }
    _choice = Choice()
    if request.method == 'GET':
        context['form'] = ChoiceForm()
        context['formset'] = ChoiceDetailFS(instance=_choice)
        return render(request, 'choices-edit.html', context)
    else:
        form = ChoiceForm(request.POST)
        if not form.is_valid():
            context['form'] = form
            context['formset'] = ChoiceDetailFS(request.POST, instance=_choice)
            context['msg_error'] = "Choice form have error, please check again!"
            return render(request, 'choices-edit.html', context)
        else:
            choice = form.save(commit=False)
            formset = ChoiceDetailFS(request.POST, instance=choice)
            for _form in formset:
                if not _form.is_valid():
                    context['form'] = form
                    context['formset'] = ChoiceDetailFS(request.POST, instance=_choice)
                    context['msg_error'] = "Detail form have error, please check again!"
                    return render(request, 'choices-edit.html', context)
            with transaction.atomic():
                choice.creator = request.user
                choice.save()
                formset.save()
                messages.add_message(request, messages.SUCCESS, 'Create new choice success')
                return redirect('choices:edit', choice.id)


@login_required
def edit(request, pk):
    choice_obj = get_object_or_404(Choice, pk=pk)
    context = {
        'page_title': 'Choices',
        'table_title': F'Update {choice_obj.name}',
        'go_back_url': reverse('choices:list'),
        'go_back_desc': 'Choices list',
        'choice': choice_obj,
    }
    if request.method == 'GET':
        context['form'] = ChoiceForm(instance=choice_obj)
        context['formset'] = ChoiceDetailFS(instance=choice_obj)
        return render(request, 'choices-edit.html', context)
    else:
        form = ChoiceForm(request.POST, instance=choice_obj)
        if not form.is_valid():
            context['form'] = form
            context['formset'] = ChoiceDetailFS(request.POST, instance=choice_obj)
            context['msg_error'] = "Form have error, please check again!"
            return render(request, 'choices-edit.html', context)
        else:
            formset = ChoiceDetailFS(request.POST, instance=choice_obj)
            if not formset.is_valid():
                context['form'] = form
                context['formset'] = ChoiceDetailFS(request.POST, instance=choice_obj)
                context['msg_error'] = "Formset have error, please check again!"
                return render(request, 'choices-edit.html', context)
            else:
                choice = form.save(commit=False)
                choice.last_modified_by = request.user
                choice.save()
                formset.save()
                messages.add_message(request, messages.SUCCESS, 'Create new tile success')
                return redirect('choices:edit', choice.id)


@login_required
def delete(request):
    if request.method == 'POST':
        del_list = request.POST.get('idlist')
        if del_list is not None:
            _del_list = [int(id) for id in del_list[:-1].split(',')]
            Choice.objects.choice(id__in=_del_list).delete()
    return redirect('choices:list')
