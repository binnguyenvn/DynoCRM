"""
    App Forms
    Configs Management
"""

from django.forms import ModelForm, Select, modelformset_factory, TextInput

from risocrm.configs.models import ExternalConfig, ReportConfig, FieldConfig


class ExternalConfigForm(ModelForm):

    class Meta:
        model = ExternalConfig
        fields = '__all__'
        widgets = {
            'external': Select(attrs={'class': 'form-control kt-select2'}),
        }


ExternalConfigFS = modelformset_factory(
    ExternalConfig,
    fields='__all__',
    extra=0,
    widgets=
        {
            'external': Select(attrs={'class': 'form-control kt-select2'}),
            'creator': Select(attrs={'class': 'form-control kt-select2 d-none'}),
            'last_modified_by': Select(attrs={'class': 'form-control kt-select2 d-none'}),
            'module': TextInput(attrs={'class': 'form-control kt-select2 d-none'}),
        }
    )


class ReportConfigForm(ModelForm):

    class Meta:
        model = ReportConfig
        fields = '__all__'
        widgets = {
            'field': Select(attrs={'class': 'form-control kt-select2'}),
            'type': Select(attrs={'class': 'form-control kt-select2'}),
        }


ReportConfigFS = modelformset_factory(
    ReportConfig,
    fields='__all__',
    extra=0,
    widgets=
        {
            'creator': Select(attrs={'class': 'form-control kt-select2 d-none'}),
            'last_modified_by': Select(attrs={'class': 'form-control kt-select2 d-none'}),
            'module': TextInput(attrs={'class': 'form-control kt-select2 d-none'}),
            
        }
    )


class FieldConfigForm(ModelForm):

    class Meta:
        model = FieldConfig
        fields = '__all__'
        widgets = {
            'field': Select(attrs={'class': 'form-control kt-select2'}),
            'type': Select(attrs={'class': 'form-control kt-select2'}),
        }


FieldConfigFS = modelformset_factory(
    FieldConfig,
    fields='__all__',
    extra=0,
    widgets=
        {
            'creator': Select(attrs={'class': 'form-control kt-select2 d-none'}),
            'last_modified_by': Select(attrs={'class': 'form-control kt-select2 d-none'}),
            'field': Select(attrs={'class': 'form-control kt-select2'}),
            'module': TextInput(attrs={'class': 'form-control kt-select2 d-none'}),
            
        }
    )
