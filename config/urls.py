from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views

setting_patterns = [
    path("apps/", include("risocrm.app_mgmt.urls")),
    path("filters/", include("risocrm.filters.urls")),
    path("choices/", include("risocrm.choices.urls")),
    # path("menus/", include("risocrm.menus.urls")),
    path("notices/", include("risocrm.notices.urls")),
    path("configs/", include("risocrm.configs.urls")),
]

urlpatterns = [
    path("", include("risocrm.dashboard.urls")),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("risocrm.users.urls", namespace="users")),

    # System
    path("settings/", include(setting_patterns)),
    path("accounts/", include("allauth.urls")),

    # NOTIFICATION
    path("webpush/", include("webpush.urls")),
    # Your stuff: custom urls includes go here
    # Contact management
    path("contacts/", include("risocrm.contacts.urls")),
    path("notes/", include("risocrm.notes.urls")),
    path("activities/", include("risocrm.activities.urls")),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns

# Automation adding app
