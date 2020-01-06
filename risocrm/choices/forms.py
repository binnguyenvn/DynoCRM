"""
    App serializer
    Choice serializer
"""

from django.forms import ModelForm, inlineformset_factory

from risocrm.choices.models import Choice, ChoiceDetail


class ChoiceForm(ModelForm):

    class Meta:
        model = Choice
        fields = '__all__'


class ChoiceDetailForm(ModelForm):
    class Meta:
        model = ChoiceDetail
        fields = '__all__'


ChoiceDetailFS = inlineformset_factory(Choice, ChoiceDetail, form=ChoiceDetailForm, extra=1)
