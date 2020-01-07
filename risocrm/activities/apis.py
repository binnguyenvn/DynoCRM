"""
    App Publish API
    Activity API
"""
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet
from url_filter.integrations.drf import DjangoFilterBackend

from risocrm.activities.models import Activity
from risocrm.activities.serializers import ActivityDepthSerializer


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
