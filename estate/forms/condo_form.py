from django.forms import ModelForm, TextInput, Textarea, NumberInput

from estate.models import Condo


class CondoForm(ModelForm):
    class Meta:
        model = Condo
        fields = ['name', 'description', 'number_of_floors', 'amenities']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': "form-control"}),
            'number_of_floors': NumberInput(attrs={'class': 'form-control'}),
            }
