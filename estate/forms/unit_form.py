from django.forms import ModelForm
from estate.models import Unit


class UnitForm(ModelForm):
    class Meta:
        model = Unit
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
