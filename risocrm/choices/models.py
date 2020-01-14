"""
    App Models
    Choice model
"""
from django.db.models import CASCADE, CharField, ForeignKey, Model

from risocrm.bases.models import BaseModel


class Choice(BaseModel):
    """
        Choice
    """
    name = CharField(default="", max_length=50, )

    def __str__(self):
        return F"Choice {self.name}"

    def detail_counter(self):
        return self.choices_detail.all().count()


class ChoiceDetail(Model):
    choice = ForeignKey(Choice, related_name="choices_detail", on_delete=CASCADE)
    value = CharField(max_length=250)

    def __str__(self):
        return F"{self.value}"
