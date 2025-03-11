# forms.py
from django import forms
from .models import Country, State

class LocationForm(forms.Form):
    country = forms.ModelChoiceField(queryset=Country.objects.all(), empty_label="Choose a country", required=True)
    state = forms.ModelChoiceField(queryset=State.objects.none(), empty_label="Choose a state", required=True)
