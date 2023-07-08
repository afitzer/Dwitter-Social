# dwitter/forms.py

from django import forms
from .models import Dweet

class DweetForm(forms.ModelForm):
    body = forms.CharField(
        required=True, 
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Dweet what's happening!!",
                "class": "textarea is-success is-medium",
                "rows": 2,}),
        label="",)

    class Meta:
        model = Dweet
        exclude = ("user", )