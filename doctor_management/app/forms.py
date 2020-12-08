from django import forms
from .models import *

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('lastName', 'firstName', 'birthday', 'contact', 'relativeContact', 'pathologies', 'information')


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ('pill', 'duration', 'frequency', 'quantity', 'otherFill')
