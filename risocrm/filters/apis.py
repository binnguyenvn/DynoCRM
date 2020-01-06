"""
    Filter API
"""
from django.http import Http404, HttpResponse
from rest_framework import request, status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from url_filter.integrations.drf import DjangoFilterBackend

from risocrm.bases.responses import (Response_200, Response_201, Response_400,
                                     Response_404, Response_503)
from risocrm.filters.models import Filter
from risocrm.filters.serializers import FilterDepthSerializer, FilterSerializer


class FilterViewSet(ModelViewSet):
    """
        Filter API for Admin manage
    """
    queryset = Filter.objects.all()
    serializer_class = FilterDepthSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = LimitOffsetPagination

    filter_backends = [DjangoFilterBackend]
    filter_fields = "__all__"

    def list(self, request, *args, **kwargs):
        response = super(FilterViewSet, self).list(request, *args, **kwargs)
        return Response_200(data=response.data)

    def retrieve(self, request, *args, **kwargs):
        try:
            response = super(FilterViewSet, self).retrieve(request, *args, **kwargs)
            return Response_200(data=response.data)
        except Http404:
            return Response_404(data={"non_field_errors": "FILTER_NOT_FOUND"})

    def create(self, request, *args, **kwargs):
        serializer = FilterSerializer(data=request.data)
        if not serializer.is_valid():
            return Response_400(data=serializer.errors)
        obj = serializer.save(creator=request.user)
        serializer = FilterDepthSerializer(obj)
        return Response_201(data=serializer.data)

    def update(self, request, *args, **kwargs):
        try:
            obj = Filter.objects.get(pk=kwargs["pk"])
            serializer = FilterSerializer(obj, data=request.data, partial=True)
            if not serializer.is_valid():
                return Response_400(data=serializer.errors)
            obj = serializer.save(last_modified_by=request.user)
            serializer = FilterDepthSerializer(obj)
            return Response_200(data=serializer.data)
        except Http404:
            return Response_400(data={"non_field_errors": "FILTER_NOT_FOUND"})

    def partial_update(self, request, *args, **kwargs):
        try:
            obj = Filter.objects.get(pk=kwargs["pk"])
            serializer = FilterSerializer(obj, data=request.data, partial=True)
            if not serializer.is_valid():
                return Response_400(data=serializer.errors)
            obj = serializer.save(last_modified_by=request.user)
            serializer = FilterDepthSerializer(obj)
            return Response_200(data=serializer.data)
        except Http404:
            return Response_400(data={"non_field_errors": "FILTER_NOT_FOUND"})

    def destroy(self, request, *args, **kwargs):
        try:
            response = super(FilterViewSet, self).destroy(request, *args, **kwargs)
            return Response_200(data=response.data)
        except Http404:
            return Response_404(data={"non_field_errors": "FILTER_NOT_FOUND"})
