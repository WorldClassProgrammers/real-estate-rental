from django.forms import ModelForm, TextInput, Textarea, NumberInput, Select
from estate.models import Room


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = [
            'condo',
            'title',
            'description',
            'still_on_contract',
            'price_for_rent',
            'price_for_sell',
            'number',
            'floor_number',
            'number_of_bedroom',
            'number_of_bathroom',
            'area'
        ]
        widgets = {
            'condo': Select(attrs={'class': 'form-control'}),
            'title': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': "form-control"}),
            'price_for_rent': NumberInput(attrs={'class': 'form-control'}),
            'price_for_sell': NumberInput(attrs={'class': 'form-control'}),
            'number': TextInput(attrs={'class': 'form-control'}),
            'floor_number': NumberInput(attrs={'class': 'form-control'}),
            'number_of_bedroom': NumberInput(attrs={'class': 'form-control'}),
            'number_of_bathroom': NumberInput(attrs={'class': 'form-control'}),
            'area': NumberInput(attrs={'class': 'form-control', 'required': True}),
            }
