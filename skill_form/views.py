from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .gemini_client import generate_roadmap
from login_user.models import Profile

@login_required
def form_view(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == "POST":
        profile.degree = request.POST.get("degree")
        profile.skills = request.POST.get("skills")
        profile.end_goal = request.POST.get("end_goal")
        profile.time_available = request.POST.get("time_available")
        profile.form_completed = True

        profile_data = {
            "degree": profile.degree,
            "skills": profile.skills,
            "end_goal": profile.end_goal,
            "time_available": profile.time_available,
        }

        
        roadmap = generate_roadmap(profile_data)
        profile.roadmap = roadmap
        profile.save()

        return redirect("dashboard:dashboard")

    return render(request, "skill_form/form.html")

@login_required
def dashboard_view(request):
    profile = Profile.objects.get(user=request.user)

    return render(
        request,
        "dashboard/dashboard.html",
        {"roadmap": profile.roadmap}
    )
