from django import forms
from .models import VIN

class VINForm(forms.ModelForm):
    class Meta:
        model = VIN
        fields = ['version', 'equipment_code', 'year_of_issue', 'place_of_production']
