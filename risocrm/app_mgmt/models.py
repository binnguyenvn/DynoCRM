"""
    App Model
    App Management
"""
from django.db.models import (CASCADE, BooleanField, CharField, ForeignKey,
                              IntegerField, Model, TextField)
from django.contrib.contenttypes.models import ContentType
from risocrm.bases.global_variables import (FIELD_TYPE_CHOICES,
                                            ON_DELETE_CHOICES)


class Dynafield(Model):
    """
        Dynamic Field
    """
    module = CharField(max_length=200, null=False, blank=False)
    name = CharField(max_length=250, null=False, blank=False)
    type = CharField(choices=FIELD_TYPE_CHOICES, max_length=150, null=False, blank=False)
    verbose_name = CharField(max_length=250, null=True, blank=True)
    fkmodule = CharField(max_length=200, null=True, blank=True)
    on_delete = CharField(choices=ON_DELETE_CHOICES, max_length=50, null=True, blank=True)

    default = CharField(max_length=200, null=True, blank=True)
    max_length = IntegerField(default=50, null=True, blank=True)
    group = CharField(max_length=250, null=True, blank=True)

    option = ForeignKey("choices.Choice", related_name="field_choices", on_delete=CASCADE, null=True, blank=True)

    is_base = BooleanField(default=False)

    def __str__(self):
        return F'Field {self.name} of {self.module}'

    def object(self):
        ctt = ContentType.objects.get(model=self.module.lower()).model_class()
        return [field for field in ctt._meta.concrete_fields if field.name == self.name][0]
