from django.shortcuts import render, get_object_or_404
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

    if request.method == "POST":
        form = PatientForm(request.POST, instance =item)
        if form.is_valid():
            form.save()
            return redirect('patient_profile') #do I have to add the item? for identifying which patient I am looking at
    else:
        form = PatientForm(instance = item)
        return render(request, 'patient_update', {'form' : form})
