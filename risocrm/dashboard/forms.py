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
            'dashboard': Select(attrs={'class': 'form-control'}),
            'type': Select(attrs={'class': 'form-control'}),
            'module': Select(attrs={'class': 'form-control'}),
            'field': Select(attrs={'class': 'form-control'}),
        }


class TileDetailForm(ModelForm):
    class Meta:
        model = TileDetail
        fields = '__all__'
        widgets = {
            'type': Select(attrs={'class': 'form-control'}),
            'field': Select(attrs={'class': 'form-control'}),
            'formula': TextInput(attrs={'class': 'form-control'}),
        }


TileFS = formset_factory(TileForm)
TileDetailFS = inlineformset_factory(Tile, TileDetail, form=TileDetailForm, extra=1)
