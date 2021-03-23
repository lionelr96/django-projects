from django.forms import ModelForm
from .models import Breed

# create the form class


class MakeForm(ModelForm):
    class Meta:
        model = Breed
        fields = '__all__'
