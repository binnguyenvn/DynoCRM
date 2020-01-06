"""
    App Router
    Dashboard Management
"""
from django.urls import include, path
from rest_framework.routers import SimpleRouter
from risocrm.dashboard.views import index, delete, create, edit, dashboard

app_name = 'dashboard'

# router = SimpleRouter(trailing_slash=False)
# router.register(r"", MenuViewSet)

# fake_api = [
#     path('get_group', get_group, name="get_group"),
#     path('', include(router.urls)),
# ]

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('dashboard/list', index, name="list"),
    path('dashboard/create', create, name="create"),
    path('dashboard/delete', delete, name="delete"),
    # path('api/', include(fake_api)),
    path('dashboard/<str:pk>', edit, name="edit"),
]