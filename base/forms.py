from django import forms

# Reordering Form and Views


class PositionForm(forms.Form):
    position = forms.CharField()
