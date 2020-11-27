from django.conf.urls import url
from .views import index, patient_information

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'patient_information^$', patient_information, name = 'patient_information')
]