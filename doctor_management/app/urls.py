from django.conf.urls import url
from .views import *
from django.urls import include, path
from rest_framework import routers
from django.contrib.auth.models import User
from . import views 
from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()
router.register(r'doctor', views.DoctorViewSet)
router.register(r'patient', views.PatientViewSet)
router.register(r'pill', views.PillViewSet)
router.register(r'prescription', views.PrescriptionViewSet)
#router.register(r'checkpatient', views.check_patient)

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^search$', search, name='search'),
    url(r'^signup$', signup, name = 'signup'),
    url(r'^patient_profile/(?P<pk>\d+)$', patient_profile, name = 'patient_profile'),
    url(r'^patient_add$', patient_add, name = 'patient_add'),
    url(r'^patient_update/(?P<pk>\d+)$', patient_update, name = 'patient_update'),
    url(r'^prescription_add/(?P<pk>\d+)$', prescription_add, name = 'prescription_add'),
    url(r'^patient_delete/(?P<pk>\d+)$', patient_delete, name='patient_delete'),
    url(r'^prescription_delete/(\d+)/(\d+)$', prescription_delete, name='prescription_delete'),

    url(r'checkpatient$', views.check_patient, name='check_patient'),
    
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
