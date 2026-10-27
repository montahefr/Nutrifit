from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.views import redirect_user_dashboard


@login_required
def nutritionist_dashboard(request):
    if not request.user.groups.filter(name="Nutritionist").exists():
        return redirect_user_dashboard(request.user)

    return render(
        request,
        "nutritionists/nutritionist_dashboard.html"
    )