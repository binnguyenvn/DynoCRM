"""
    App Router
    Activity Router
"""
from django.urls import include, path
from rest_framework.routers import SimpleRouter
from risocrm.activities.apis import ActivityViewSet

app_name = 'activities'

router = SimpleRouter(trailing_slash=False)
router.register(r"", ActivityViewSet)

urlpatterns = [
    path('api', include(router.urls)),
]