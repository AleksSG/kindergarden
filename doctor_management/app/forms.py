from django import forms
from .models import *

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('lastName', 'firstName', 'birthday', 'contact', 'relativeContact', 'pathologies', 'information')


class PillForm(forms.ModelForm):
    class Meta:
        model = Pill
        fields = ('name', 'description', 'picture', 'otherFill')