"""
    App serializer
    Filter serializer
"""

from django.forms import BooleanField, CheckboxInput, ModelForm, Select, TextInput, inlineformset_factory, SelectMultiple

from risocrm.filters.models import Filter, FilterDetail


class FilterForm(ModelForm):
    default = BooleanField(required=False)

    class Meta:
        model = Filter
        fields = '__all__'
        widgets = {
            'default': CheckboxInput(),
            'module': Select(attrs={'class': 'form-control kt-select2'}),
            'field_list': SelectMultiple(attrs={'class': 'form-control kt-select2'}),
            'order_by': Select(attrs={'class': 'form-control kt-select2'}),
            'query_string': TextInput(attrs={'class': 'form-control', 'disabled':''}),
        }


class FilterDetailForm(ModelForm):
    class Meta:
        model = FilterDetail
        fields = '__all__'
        widgets = {
            'field_name': Select(attrs={'class': 'field-name form-control'}),
            'operator': Select(attrs={'class': 'field-operator form-control'}),
            'value': TextInput(attrs={'class': 'field-value form-control'}),
            'private': CheckboxInput(),
        }


FilterDetailFS = inlineformset_factory(Filter, FilterDetail, form=FilterDetailForm, extra=1)
