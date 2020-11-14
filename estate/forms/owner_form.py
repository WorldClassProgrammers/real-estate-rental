from django.forms import ModelForm
from estate.models import Owner


class OwnerForm(ModelForm):
    class Meta:
        model = Owner
        fields = ['name', 'email', 'line_id', 'phone_number']
