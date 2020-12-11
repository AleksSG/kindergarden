from django.db import models

# Create your models here.


class Pill(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=100, blank=True)
    picture = models.ImageField(upload_to ='Documents/')
    otherFill = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Prescription(models.Model):
        periods = [('daily', 'day'), ('weekly', 'week'), ('monthly', 'month')]
        pill = models.ForeignKey(to=Pill, on_delete=models.CASCADE, blank=True)
        duration_start = models.DateField()
        duration_end = models.DateField()
        frequency_period = models.CharField(max_length=100, choices=periods, default='weekly')
        frequency_rel_period = models.IntegerField()
        quantity = models.IntegerField ()
        otherFill = models.CharField(max_length=100, blank=True)

        def __str__(self):
            return str(self.id)



class Doctor(models.Model):
    lastName = models.CharField(max_length=100, blank=True)
    firstName = models.CharField(max_length=100, blank=True)
    speciality = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    phonenumber = models.CharField(max_length=100, blank=True)
    notes = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.lastName+" "+self.firstName


class Patient(models.Model):
    doctors = models.ManyToManyField(Doctor, blank=True)
    u_id = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=100, blank=True)
    lastName = models.CharField(max_length=100, blank=True)
    firstName = models.CharField(max_length=100, blank=True)
    birthday = models.DateField(max_length=100, blank=True)
    contact = models.CharField(max_length=100, blank=True)
    relativeContact = models.CharField(max_length=100, blank=True)
    pathologies = models.CharField(max_length=100, blank=True)
    information = models.CharField(max_length=100, blank=True)
    prescription = models.ManyToManyField(Prescription, blank=True)

    def __str__(self):
        return self.lastName+" "+self.firstName
