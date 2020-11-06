from django.forms import ModelForm


from estate.models import Condo
from estate.models.condo import CondoImages


class CondoForm(ModelForm):
    class Meta:
        model = Condo
        fields = ['name', 'description', 'number_of_floors', 'amenities']


class CondoImagesForm(ModelForm):
    class Meta:
        model = CondoImages
        fields = ['image']
