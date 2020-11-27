from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def patient_information(request):
    return render(request, 'patient_information.html')
