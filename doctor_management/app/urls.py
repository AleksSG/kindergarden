from django.conf.urls import url
from .views import index, signup, patient_information

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^signup$', signup, name = 'signup'),
    url(r'^patient_information$', patient_information, name = 'patient_information')
]