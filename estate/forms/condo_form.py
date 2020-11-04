from django.forms import ModelForm
from estate.models import Condo


class CondoForm(ModelForm):
    class Meta:
        model = Condo
        fields = ['name', 'description', 'number_of_floors', 'amenities']
