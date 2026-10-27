
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required


def register_view(request):
    if request.user.is_authenticated:
        return redirect_user_dashboard(request.user)

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip().lower()
        role = request.POST.get("role", "Patient")
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm_password", "")

        if not name or not email or not password or not confirm_password:
            messages.error(request, "Please complete every field.")

        elif role not in ("Patient", "Nutritionist"):
            messages.error(request, "Please choose a valid account type.")

        elif len(name) > 150:
            messages.error(request, "Your name is too long.")

        elif User.objects.filter(email__iexact=email).exists():
            messages.error(request, "This email is already registered.")

        elif password != confirm_password:
            messages.error(request, "Your passwords do not match.")

        elif len(password) < 8:
            messages.error(
                request,
                "Your password must contain at least 8 characters."
            )

        else:
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password,
                first_name=name,
            )

            group, _ = Group.objects.get_or_create(name=role)
            user.groups.add(group)

            messages.success(
                request,
                "Your account is ready! Please sign in."
            )
            return redirect("login")

    return render(request, "accounts/register.html")


def login_view(request):
    if request.user.is_authenticated:
        return redirect_user_dashboard(request.user)

    if request.method == "POST":
        email = request.POST.get("email", "").strip().lower()
        password = request.POST.get("password", "")

        try:
            account = User.objects.get(email__iexact=email)
            user = authenticate(
                request,
                username=account.username,
                password=password,
            )
        except User.DoesNotExist:
            user = None

        if user is not None:
            login(request, user)
            messages.success(request, "Welcome back!")
            return redirect_user_dashboard(user)

        messages.error(request, "Incorrect email or password.")

    return render(request, "accounts/login.html")


def redirect_user_dashboard(user):
    if user.is_superuser or user.is_staff:
        return redirect("admin_dashboard")

    if user.groups.filter(name="Nutritionist").exists():
        return redirect("nutritionist_dashboard")

    if user.groups.filter(name="Patient").exists():
        return redirect("patient_dashboard")

    return redirect("dashboard")


@login_required
def dashboard(request):
    return redirect_user_dashboard(request.user)


def logout_view(request):
    logout(request)
    messages.success(request, "You have signed out.")
    return redirect("home")
