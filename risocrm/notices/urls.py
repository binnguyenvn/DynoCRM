"""
    App Router
    Menu Management
"""
from django.urls import include, path
from rest_framework.routers import SimpleRouter

from risocrm.notices.apis import unread_count, get_list, reading

app_name = 'notices'

# router = SimpleRouter(trailing_slash=False)
# router.register(r"", MenuViewSet)

fake_api = [
    path('unread_count', unread_count, name="unread_count"),
    path('get_list', get_list, name="get_list"),
    path('reading/<str:id>', reading, name="reading"),
    # path('', include(router.urls)),
]

urlpatterns = [
    path('api/', include(fake_api)),
]
