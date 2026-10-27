
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # Django built-in admin
    path("admin/", admin.site.urls),

    # Shared pages
    path("", views.home, name="home"),

    # Authentication
    path("", include("accounts.urls")),

    # User dashboards
    path("patients/", include("patients.urls")),
    path("nutritionists/", include("nutritionists.urls")),
    path("admin-dashboard/", include("admin_dashboard.urls")),
]
