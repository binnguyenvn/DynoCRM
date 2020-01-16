"""
    App Publish API
    Activity API
"""
from django.http import JsonResponse
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet
from url_filter.integrations.drf import DjangoFilterBackend

from risocrm.activities.models import Activity
from risocrm.activities.serializers import ActivityDepthSerializer
from risocrm.bases.contenttype import contentype_from_url


class ActivityViewSet(ReadOnlyModelViewSet):
    """
        Activity API for Admin manage
    """
    queryset = Activity.objects.all()
    serializer_class = ActivityDepthSerializer
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
        self.queryset = Activity.objects.filter(content_type=content_type, object_id=path.split('/')[-1])
        return super(ActivityViewSet, self).list(request, *args, **kwargs)
