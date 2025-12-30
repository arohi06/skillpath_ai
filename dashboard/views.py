from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from login_user.models import Profile


@login_required
def dashboard_view(request):
    profile = Profile.objects.get(user=request.user)

    return render(
        request,
        "dashboard/dashboard.html",
        {"roadmap": profile.roadmap}
    )
