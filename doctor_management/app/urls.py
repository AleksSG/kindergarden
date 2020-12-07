from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^search$', search, name='search'),
    url(r'^signup$', signup, name = 'signup'),
    url(r'^patient_profile/(?P<pk>\d+)$', patient_profile, name = 'patient_profile'),
    url(r'^patient_update/(?P<pk>\d+)$', patient_update, name = 'patient_update'),
    url(r'^prescription_add/(?P<pk>\d+)$', prescription_add, name = 'prescription_add')

]
