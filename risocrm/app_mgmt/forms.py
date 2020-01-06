"""
    App Forms
    App Management
"""

from django.forms import (CheckboxInput, ModelForm, Select, TextInput,
                          inlineformset_factory, CharField)

from risocrm.app_mgmt.models import Dynafield


class DynafieldForm(ModelForm):

    class Meta:
        model = Dynafield
        fields = '__all__'
        widgets = {
            'type': Select(attrs={'class': 'form-control kt-select2'}),
            'module': Select(attrs={'class': 'form-control kt-select2'}),
            'fkmodule': Select(attrs={'class': 'form-control kt-select2'}),
            'group': Select(attrs={'class': 'form-control kt-select2'}),
            'option': Select(attrs={'class': 'form-control kt-select2'}),
            'default': Select(attrs={'class': 'form-control kt-select2'}),
        }
