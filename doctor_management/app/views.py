from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup.html')

def patient_profile(request, pk):
    item = get_object_or_404(Patient, pk = pk)
    context = {
        'item' : item
    }
    return render(request, 'patient_profile.html', context)

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



def prescription_add(request):
    return render(request, 'prescription_add.html')
