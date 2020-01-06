"""
    App Publish API
    Notification system
"""
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.urls import reverse

from risocrm.notices.models import Notice


@login_required
def unread_count(request):
    return JsonResponse({'unread': Notice.objects.filter(to_user=request.user, is_read=False).count()}, safe=False)

@login_required
def reading(request, id):
    nt = Notice.objects.get(pk=id)
    nt.is_read = True
    nt.save()
    return JsonResponse({'data': nt.url}, safe=False)


@login_required
def get_list(request):
    data = list(request.user.read_notifications.all().order_by('-id').values())
    return JsonResponse({'data': data}, safe=False)
