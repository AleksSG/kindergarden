from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

from rest_framework import viewsets
from .serializers import DoctorSerializer, PatientSerializer, PillSerializer, PrescriptionSerializer
from django.views.generic import ListView, DetailView

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create views

def index(request):
    items = Patient.objects.all()
    context = {
        'items' : items,
    }
    return render(request, 'index.html', context)

def search(request):
    search_term = request.GET['search']
    if search_term != '':
        items = Patient.objects.filter(lastName__startswith = search_term)
        return render(request, 'index.html', {'items':items})
    else:
        items = Patient.objects.all()
        return render(request, 'index.html', {'items':items})

def signup(request):
    return render(request, 'signup.html')

def patient_profile(request, pk):
    item = get_object_or_404(Patient, pk = pk)
    context = {
        'item' : item
    }
    return render(request, 'patient_profile.html', context)


def patient_add(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            form = PatientForm()
            return render(request, 'patient_add.html', {'form': form})
    else:
        form = PatientForm()
        return render(request, 'patient_add.html', {'form': form})

def patient_update(request, pk):
    item = get_object_or_404(Patient, pk = pk)
    context = {
        'item' : item
    }
    if request.method == "POST":
        form = PatientForm(request.POST, instance =item)
        if form.is_valid():
            form.save()
            return redirect('patient_profile', pk = pk)
    else:
        form = PatientForm(instance = item)
        return render(request, 'patient_update.html', {'form' : form})


def prescription_add(request, pk):
    if request.method == "POST":
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            f = form.save()
            Patient.objects.get(pk = pk).prescription.add(f)
            return redirect('patient_profile', pk = pk)
    else:
        form = PrescriptionForm()
        return render(request, 'prescription_add.html', {'form' : form})

def patient_delete(request, pk):
    Patient.objects.get(pk=pk).delete()
    return redirect('index')

def prescription_delete(request, pk, p_pk):
    Prescription.objects.get(pk=pk).delete()
    return redirect('patient_profile', pk = p_pk)

def check_patient(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        patients = Patient.objects.all()
        for patient in patients:
            if patient.email == body['email'] and patient.password == body['password']:
                return HttpResponse(status=200)
    return HttpResponse(status=404)

def update_patient(request):
    if request.method == "PATCH":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        patients = Patient.objects.all()
        for patient in patients:
            if patient.email == body['email']:
                patient.u_id = body['UID']
                return HttpResponse(status=200)
                

#API classes

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PillViewSet(viewsets.ModelViewSet):
    queryset = Pill.objects.all()
    serializer_class = PillSerializer

class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
