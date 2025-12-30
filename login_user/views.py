from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from login_user.models import Profile


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            messages.error(request, "⚠️ Username and Password are required.")
            return redirect("login_user:login")

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            profile, _ = Profile.objects.get_or_create(user=user)
            if profile.is_complete():
                return redirect("dashboard:dashboard")
            else:
                return redirect("skill_form:form")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("login_user:login")

    return render(request, "login_user/login.html")



def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if not username or not password or not confirm_password:
            messages.error(request, "All fields are required.")
            return redirect("login_user:register")

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("login_user:register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "User already exists. Please login instead.")
            return redirect("login_user:login")

        try:
            User.objects.create_user(username=username, password=password)
            messages.success(request, "Registration successful. Please login.")
            return redirect("login_user:login")
        except Exception as e:
            messages.error(request, f" Something went wrong: {str(e)}")
            return redirect("login_user:register")

    return render(request, "login_user/register.html")





def forgot_password(request):
    if request.method == "POST":
        username = request.POST.get("username")
        new_password = request.POST.get("new_password")

        if not username or not new_password:
            messages.error(request, " Username and New Password are required.")
            return redirect("login_user:forgot_password")

        try:
            user = User.objects.get(username=username)
            user.set_password(new_password)
            user.save()
            messages.success(request, "Password reset successful. Please login.")
            return redirect("login_user:login")
        except User.DoesNotExist:
            messages.error(request, "Username not found.")
            return redirect("login_user:forgot_password")

    return render(request, "login_user/forgot_password.html")