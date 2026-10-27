from django.urls import path
from . import views

urlpatterns = [
    path("", views.patient_dashboard, name="patient_dashboard"),
    path("dashboard/", views.patient_dashboard, name="patient_dashboard_alt"),
]