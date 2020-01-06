"""
    Base serializer
"""
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.files.storage import default_storage
from rest_framework.serializers import CharField, FileField, ModelSerializer, Serializer

User = get_user_model()


class UserNestedViewSerializer(ModelSerializer):
    """
        User exclude password, username, email to update user profile
    """
    class Meta:
        model = User
        fields = ('id', 'first_name',)


class BaseSerializer(ModelSerializer):
    """
        Base serializer
    """
    creator = UserNestedViewSerializer(read_only=True)
    last_modified_by = UserNestedViewSerializer(read_only=True)

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(BaseSerializer, self).__init__(*args, **kwargs)

        fields = self.context['request'].query_params.get('fields')
        if fields:
            fields = fields.split(',')
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class Base64ImageField(CharField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid
        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                data = data.split(';base64,')[1]

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12]  # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)
            if file_extension is not None:
                complete_file_name = "%s.%s" % (file_name, file_extension, )

                _file = ContentFile(decoded_file, name=complete_file_name)
                data = default_storage.save(complete_file_name, _file)
                data = settings.MEDIA_URL + data
        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension


class SeoSerializer(BaseSerializer):
    """
        Seo serializer
    """
    seo_title = CharField(required=True)
    seo_description = CharField(required=True)
    seo_keywords = CharField(required=True)
    image = Base64ImageField(required=True)
    name = CharField(required=True)
    url = CharField(required=True)
    description = CharField(required=True)


def custom_fields(model, add_fields, remove_fields):
    """
        Function to get all field of model and add new field
    """
    all_field = [f.name for f in model._meta.get_fields()]
    for item in remove_fields:
        all_field.remove(item)
    for item in add_fields:
        all_field.append(item)
    return tuple(all_field)


class FileSerializer(Serializer):
    """
        Upload file
    """
    file = FileField(required=True)
