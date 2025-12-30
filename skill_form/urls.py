from django.urls import path
from . import views

app_name = 'skill_form'

urlpatterns = [
    path('', views.form_view, name='form'),
    path("dashboard/", views.dashboard_view, name="dashboard"),
]