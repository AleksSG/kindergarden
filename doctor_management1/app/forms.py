from django import forms
from .models import *

class LoginForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('email', 'password')

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('lastName', 'firstName', 'speciality', 'phonenumber', 'address', 'email', 'password', 'notes')

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('lastName', 'firstName', 'birthday', 'contact', 'email', 'relativeContact', 'pathologies', 'information')


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ('pill', 'duration_start', 'duration_end', 'frequency_period', 'frequency_rel_period', 'quantity', 'otherFill')
