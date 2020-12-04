from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^signup$', signup, name = 'signup'),
    url(r'^patient_profile$', patient_profile, name = 'patient_profile'),
    url(r'^patient_update/(?P<pk>\d+)$', patient_update, name = 'patient_update')
]
