"""
    Choice API
"""
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from risocrm.choices.models import Choice


def choice_list(request):
    """
        Return list choice
    """
    data = [{'id': m.id, 'name': m.name} for m in Choice.objects.all()]
    return JsonResponse({'data': data}, status=200)


def choice_childs(request, pk):
    """
        Return list option of choice
    """
    choice = get_object_or_404(Choice, pk=pk)
    data = [{'id': m.id, 'value': m.value} for m in choice.choices_detail.all()]
    return JsonResponse({'data': data}, status=200)
