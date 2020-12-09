from django.db import models

# Create your models here.

class Doctor(models.Model):
    lastName = models.CharField(max_length=100, blank=True)
    login = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=100, blank=True)

class Pill(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=100, blank=True)
    picture = models.ImageField(upload_to ='Documents/')
    otherFill = models.CharField(max_length=100, blank=True)

    def _str_(self):
        return name

class Prescription(models.Model):
        #patient = models.ForeignKey(to=Patient, on_delete=models.CASCADE)
        periods = [('daily', 'day'), ('weekly', 'week'), ('monthly', 'month')]
        pill = models.ForeignKey(to=Pill, on_delete=models.CASCADE, blank=True)
        duration_start = models.DateField()
        duration_end = models.DateField()
        frequency_period = models.CharField(max_length=100, choices=periods, default='weekly')
        frequency_rel_period = models.IntegerField()
        quantity = models.IntegerField ()
        otherFill = models.CharField(max_length=100, blank=True)

        def _str_(self):
            return 'Prescription: {0}'


class Patient(models.Model):
    lastName = models.CharField(max_length=100, blank=True)
    firstName = models.CharField(max_length=100, blank=True)
    birthday = models.DateField(max_length=100, blank=True)
    contact = models.CharField(max_length=100, blank=True)
    relativeContact = models.CharField(max_length=100, blank=True)
    pathologies = models.CharField(max_length=100, blank=True)
    information = models.CharField(max_length=100, blank=True)
    prescription = models.ManyToManyField(Prescription, blank=True)

    def _str_(self):
        return 'Client: {0}'
