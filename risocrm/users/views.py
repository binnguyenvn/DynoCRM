"""
    App Controller
    Staff Management
"""
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.db import transaction
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import DetailView, RedirectView, UpdateView

from risocrm.bases.permissions import isSelfOrSuperOrDenie, roleAdministrator
from risocrm.users.forms import UserChangeForm, UserCreationForm, UserForm

User = get_user_model()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()


@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='/')
def index(request):
    context = {
        'page_title': 'Users',
        'table_title': 'User ist',
        'go_back_url': '',
        'go_back_desc': '',
        'obj_list': User.objects.all()
    }
    return render(request, 'users-list.html', context)


@login_required
def view(request, username):
    user_obj = get_object_or_404(User, username=username)
    context = {
        'page_title': 'Users',
        'table_title': F'Detail of {user_obj.first_name} {user_obj.username}',
        'go_back_url': reverse('users:list'),
        'go_back_desc': 'Users list',
        'user': user_obj,
        'form': UserForm(instance=user_obj)
    }
    return render(request, 'users-view.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='/')
def create(request):
    context = {
        'page_title': 'Users',
        'table_title': 'Create new User',
        'go_back_url': reverse('users:list'),
        'go_back_desc': 'Users list'
    }
    if request.method == 'GET':
        form = UserCreationForm()
        context['form'] = form
        return render(request, 'users-create.html', context)
    else:
        form = UserCreationForm(request.POST)
        if not form.is_valid():
            context['form'] = form
            context['msg_error'] = "User form have error, please check again!"
            return render(request, 'users-create.html', context)
        else:
            user = form.save()
            if form.data['groups']:
                group = Group.objects.get(pk=form.data['groups'])
                user.groups.add(group)
            messages.add_message(request, messages.SUCCESS, 'Create new user success')
            return redirect('users:detail', user.username)


@login_required
@user_passes_test(isSelfOrSuperOrDenie)
def detail(request, username):
    try:
        referer = request.META.get('HTTP_REFERER')
        if 'socials' in referer:
            return redirect('socials:list')
    except Exception:
        pass

    user_obj = get_object_or_404(User, username=username)
    context = {
        'page_title': 'Users',
        'table_title': F'Update {user_obj.first_name} {user_obj.username}',
        'go_back_url': reverse('users:list'),
        'go_back_desc': 'Users list',
        'user': user_obj,
    }
    if request.method == 'GET':
        form = UserChangeForm(instance=user_obj)
        context['form'] = form
        return render(request, 'users-edit.html', context)
    else:
        form = UserChangeForm(request.POST, request.FILES, instance=user_obj)
        if not form.is_valid():
            context['form'] = form
            context['msg_error'] = "User form have error, please check again!"
            return render(request, 'users-edit.html', context)
        else:
            user = form.save()
            if not request.user.groups.filter(name='Administrator').exists():
                user.groups = user_obj.groups
                user.save()
            messages.add_message(request, messages.SUCCESS, F'Edit user {user.first_name} success')
            return redirect('users:detail', user.username)


@login_required
@user_passes_test(roleAdministrator, login_url='/')
def delete(request):
    if request.method == 'POST':
        del_list = request.POST.get('idlist')
        if del_list is not None:
            _del_list = [int(id) for id in del_list[:-1].split(',')]
            User.objects.filter(id__in=_del_list).delete()
    return redirect('users:list')
