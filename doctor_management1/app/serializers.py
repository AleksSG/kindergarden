from rest_framework import serializers

from .models import Doctor, Patient, Pill, Prescription

class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class PillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pill
        fields = '__all__'

class PrescriptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'
