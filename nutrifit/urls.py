
from django.contrib import admin
from django.urls import path
from nutrifit.views import (
    home,
    login_view,
    register_view,
    logout_view,
    dashboard,
    patient_dashboard,
    nutritionist_dashboard,
    admin_dashboard,
)

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", home, name="home"),
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("logout/", logout_view, name="logout"),

    path("patient/dashboard/", patient_dashboard, name="patient_dashboard"),
    path("nutritionist/dashboard/", nutritionist_dashboard, name="nutritionist_dashboard"),
    path("admin-dashboard/", admin_dashboard, name="admin_dashboard"),
]
