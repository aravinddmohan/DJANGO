from django import forms

class VisitorForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)