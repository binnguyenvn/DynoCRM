from django.contrib.contenttypes.models import ContentType
from django.urls import resolve


def contentype_from_url(path):
    """
        Return contentType base on path
    """
    if path is None:
        return None
    path = '/'+'/'.join(path.split('/')[3:])

    app = resolve(path).app_names[0]
    return ContentType.objects.get(app_label=app)
