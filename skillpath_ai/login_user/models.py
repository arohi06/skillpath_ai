from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    degree = models.CharField(max_length=200, blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    end_goal = models.CharField(max_length=200, blank=True, null=True)
    time_available = models.CharField(max_length=100, blank=True, null=True)
    form_completed = models.BooleanField(default=False)
    roadmap = models.JSONField(blank=True, null=True)

    def is_complete(self):
        return all([self.degree, self.skills, self.end_goal, self.time_available])