from django import forms
from .models import Note

class notes_forms(forms.Form):
    notes_variety=forms.ModelChoiceField(
        queryset=Note.objects.all(),
        label="Select Note Variety"
        )
