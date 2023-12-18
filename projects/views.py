from django.shortcuts import render, redirect
from projects.models import Project
from django.contrib.auth.decorators import login_required

# Create your views here.
def list_projects(request):
    projects = Project.objects.all()
    context = {
        "projects": projects,
    }
    return render(request, "projects/list_projects.html", context)

def redirect_to_home(request):
    return redirect("list_projects")
