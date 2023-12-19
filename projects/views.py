from django.shortcuts import render, redirect, get_object_or_404
from projects.models import Project
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def list_projects(request):
    projects = Project.objects.filter(owner=request.user)
    context = {
        "projects": projects,
    }
    return render(request, "projects/list_projects.html", context)

def redirect_to_home(request):
    return redirect("list_projects")

@login_required
def show_project(request, id):
    project = get_object_or_404(Project, id=id)
    context = {
        "project_object": project,
    }
    return render(request, "projects/show_project.html", context)
