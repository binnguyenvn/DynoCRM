"""
    App serializer
    Dashboard Management
"""

from django.forms import (CheckboxInput, ModelForm, Select, TextInput,
                          formset_factory, inlineformset_factory)

from risocrm.dashboard.models import Tile, TileDetail


class TileForm(ModelForm):
    class Meta:
        model = Tile
        fields = '__all__'
        widgets = {
            'dashboard': Select(),
            'type': Select(),
            'module': Select(),
            'field': Select(),
        }


class TileDetailForm(ModelForm):
    class Meta:
        model = TileDetail
        fields = '__all__'
        widgets = {
            'type': Select(),
            'field': Select(),
            'formula': TextInput(),
        }


TileFS = formset_factory(TileForm)
TileDetailFS = inlineformset_factory(Tile, TileDetail, form=TileDetailForm, extra=1)
