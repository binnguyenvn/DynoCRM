"""
    Reuseable response
"""
import datetime

from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_503_SERVICE_UNAVAILABLE
)


def Response_200(r_id=0, func='', data='', desc=''):
    return Response(
        {
            'RequestID': r_id,
            'FunctionName': func,
            'Data': data,
            'Description': desc,
            'ResponseDateTime': datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        },
        status=HTTP_200_OK
    )


def Response_201(r_id=0, func='', data='', desc=''):
    return Response(
        {
            'RequestID': r_id,
            'FunctionName': func,
            'Data': data,
            'Description': desc,
            'ResponseDateTime': datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        },
        status=HTTP_201_CREATED
    )


def Response_400(r_id=0, func='', data='', desc=''):
    return Response(
        {
            'RequestID': r_id,
            'FunctionName': func,
            'Data': data,
            'Description': desc,
            'ResponseDateTime': datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        },
        status=HTTP_400_BAD_REQUEST
    )


def Response_404(r_id=0, func='', data='', desc=''):
    return Response(
        {
            'RequestID': r_id,
            'FunctionName': func,
            'Data': data,
            'Description': desc,
            'ResponseDateTime': datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        },
        status=HTTP_404_NOT_FOUND
    )


def Response_500(r_id=0, func='', data='', desc=''):
    return Response(
        {
            'RequestID': r_id,
            'FunctionName': func,
            'Data': data,
            'Description': desc,
            'ResponseDateTime': datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        },
        status=HTTP_500_INTERNAL_SERVER_ERROR
    )


def Response_503(r_id=0, func='', data='', desc=''):
    return Response(
        {
            'RequestID': r_id,
            'FunctionName': func,
            'Data': data,
            'Description': desc,
            'ResponseDateTime': datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        },
        status=HTTP_503_SERVICE_UNAVAILABLE
    )
