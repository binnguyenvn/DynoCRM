"""
    App Publish API
    Note API
"""
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet
from url_filter.integrations.drf import DjangoFilterBackend

from risocrm.bases.contenttype import contentype_from_url
from risocrm.notes.models import Note
from risocrm.notes.serializers import NoteDepthSerializer


class NoteViewSet(ReadOnlyModelViewSet):
    """
        Note API for Admin manage
    """
    queryset = Note.objects.all()
    serializer_class = NoteDepthSerializer
    permission_classes = (IsAuthenticated,)

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filter_fields = "__all__"

    ordering_fields = "__all__"
    ordering = ('-time_created')

    def list(self, request, *args, **kwargs):
        path = request.META.get('HTTP_REFERER', None) or '/'
        content_type = contentype_from_url(path)
        if content_type is None:
            return JsonResponse({'data': 'Cannot find Model'}, status=400)
        self.queryset = Note.objects.filter(content_type=content_type, object_id=path.split('/')[-1])
        return super(NoteViewSet, self).list(request, *args, **kwargs)


@login_required()
def create(request):
    note = request.POST.get('note', None)
    if note is None:
        return JsonResponse({'data': 'Note cannot None'}, status=400)
    path = request.META.get('HTTP_REFERER', None) or '/'
    content_type = contentype_from_url(path)
    if content_type is None:
        return JsonResponse({'data': 'Cannot find Model'}, status=400)
    Note.objects.create(
        content_type=content_type,
        object_id=path.split('/')[-1],
        type=request.POST.get('type'),
        note=note,
        creator=request.user
    )
    return JsonResponse({'data': 'Create done'}, status=200)
