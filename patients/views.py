from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.views import redirect_user_dashboard


@login_required
def patient_dashboard(request):
    if not request.user.groups.filter(name="Patient").exists():
        return redirect_user_dashboard(request.user)

    return render(request, "patients/patient_dashboard.html")