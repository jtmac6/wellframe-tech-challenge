from django.urls import path
from django.conf.urls import url, include
from rest_framework_nested import routers

from . import views

router = routers.DefaultRouter()
router.register(r'patients', views.PatientViewSet)
router.register(r'medications', views.MedicationViewSet)
router.register(r'prescriptions', views.PrescriptionViewSet)

patients_router = routers.NestedDefaultRouter(router, r'patients', lookup='patient')
patients_router.register(r'prescriptions', views.PrescriptionViewSet, base_name='prescriptions')

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/', include(patients_router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]