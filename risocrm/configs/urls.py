"""
    App Urls
    Filters Router
"""
from django.urls import path

from risocrm.configs.views import external, report,field

app_name = 'configs'

urlpatterns = [
    path('external/<str:pk>', external, name="external"),
    path('report/<str:pk>', report, name="report"),
    path('field/<str:pk>', field, name="field"),
]
