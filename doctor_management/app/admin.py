from django.contrib import admin
from .models import *

@admin.register(Doctor, Patient, Pill, Prescription)
class ViewAdmin(admin.ModelAdmin):
    pass
