from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Doctor, Patient, Pill, Prescription)
class ViewAdmin(admin.ModelAdmin):
    pass 