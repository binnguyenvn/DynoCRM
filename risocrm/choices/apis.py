"""
    Choice API
"""
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from url_filter.integrations.drf import DjangoFilterBackend

from risocrm.bases.responses import (Response_200, Response_201, Response_400,
                                     Response_404)
from risocrm.choices.models import Choice
from risocrm.choices.serializers import (ChoiceDepthNestedSerializer,
                                         ChoiceDepthSerializer,
                                         ChoiceNestedSerializer,
                                         ChoiceSerializer)


class ChoiceViewSet(ModelViewSet):
    """
        Choice API for Admin manage
    """
    queryset = Choice.objects.all()
    serializer_class = ChoiceDepthSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = LimitOffsetPagination

    filter_backends = [DjangoFilterBackend]
    filter_fields = "__all__"

    def list(self, request, *args, **kwargs):
        response = super(ChoiceViewSet, self).list(request, *args, **kwargs)
        return Response_200(data=response.data)

    def retrieve(self, request, *args, **kwargs):
        try:
            response = super(ChoiceViewSet, self).retrieve(request, *args, **kwargs)
            return Response_200(data=response.data)
        except Http404:
            return Response_404(data={"non_field_errors": "FILTER_NOT_FOUND"})

    def create(self, request, *args, **kwargs):
        serializer = ChoiceSerializer(data=request.data)
        if not serializer.is_valid():
            return Response_400(data=serializer.errors)
        obj = serializer.save(creator=request.user)
        serializer = ChoiceDepthSerializer(obj)
        return Response_201(data=serializer.data)

    @action(detail=False, methods=['post'])
    def create_nested(self, request, *args, **kwargs):
        serializer = ChoiceNestedSerializer(data=request.data)
        if not serializer.is_valid():
            return Response_400(data=serializer.errors)
        obj = serializer.save(creator=request.user)
        serializer = ChoiceDepthNestedSerializer(obj)
        return Response_201(data=serializer.data)

    def update(self, request, *args, **kwargs):
        try:
            obj = Choice.objects.get(pk=kwargs["pk"])
            serializer = ChoiceSerializer(obj, data=request.data, partial=True)
            if not serializer.is_valid():
                return Response_400(data=serializer.errors)
            obj = serializer.save(last_modified_by=request.user)
            serializer = ChoiceDepthSerializer(obj)
            return Response_200(data=serializer.data)
        except Http404:
            return Response_400(data={"non_field_errors": "FILTER_NOT_FOUND"})

    def partial_update(self, request, *args, **kwargs):
        try:
            obj = Choice.objects.get(pk=kwargs["pk"])
            serializer = ChoiceSerializer(obj, data=request.data, partial=True)
            if not serializer.is_valid():
                return Response_400(data=serializer.errors)
            obj = serializer.save(last_modified_by=request.user)
            serializer = ChoiceDepthSerializer(obj)
            return Response_200(data=serializer.data)
        except Http404:
            return Response_400(data={"non_field_errors": "FILTER_NOT_FOUND"})

    def destroy(self, request, *args, **kwargs):
        try:
            response = super(ChoiceViewSet, self).destroy(request, *args, **kwargs)
            return Response_200(data=response.data)
        except Http404:
            return Response_404(data={"non_field_errors": "FILTER_NOT_FOUND"})


def choice_childs(request, pk):
    choice = get_object_or_404(Choice, pk=pk)
    data = [{'id': m.id, 'value': m.value} for m in choice.choices_detail.all()]
    return JsonResponse({'data': data}, status=200)
