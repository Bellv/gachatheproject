from django import forms

from .models import Characterfgo, FgoType


class FgoGachaForm(forms.Form):
    class Meta:
        model = FgoType
        fields = None

