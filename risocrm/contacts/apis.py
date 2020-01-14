"""
    App Publish API
    Contact API
"""
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet
from url_filter.integrations.drf import DjangoFilterBackend
from risocrm.contacts.models import Contact
from risocrm.contacts.serializers import ContactDepthSerializer


class ContactViewSet(ReadOnlyModelViewSet):
    """
        Contact API for Admin manage
    """
    queryset = Contact.objects.all()
    serializer_class = ContactDepthSerializer
    permission_classes = (IsAuthenticated,)

    filter_backends = [DjangoFilterBackend]
    filter_fields = "__all__"
