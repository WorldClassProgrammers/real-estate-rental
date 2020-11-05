from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from estate.models.custom_user import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ["username", "role"]
