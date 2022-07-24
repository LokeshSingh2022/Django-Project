from django.forms import ModelForm
from .models import State_details

class State_details_form(ModelForm):
    class Meta:
        model = State_details
        fields = '__all__'