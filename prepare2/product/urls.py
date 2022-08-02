from . import views
from django.urls import path

urlpatterns = [
    path("run_massive_tasks/", views.RunMassiveTasks.as_view()),
]