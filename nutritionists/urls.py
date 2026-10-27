from django.urls import path
from . import views

urlpatterns = [
    path(
        "dashboard/",
        views.nutritionist_dashboard,
        name="nutritionist_dashboard",
    ),
]