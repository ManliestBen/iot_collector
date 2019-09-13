from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Project, Component
from .forms import ProgressForm

def home(request):
    return render(request, 'projects/index.html')

def about(request):
    return render(request, 'about.html')

def projects_index(request):
    projects = Project.objects.all()
    return render(request, 'projects/index.html', { 'projects': projects })
# Create your views here.

def projects_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    components_project_doesnt_have = Component.objects.exclude(id__in = project.components.all().values_list('id'))
    progress_form = ProgressForm()
    return render(request, 'projects/detail.html', { 'project': project, 'progress_form': progress_form, 'components': components_project_doesnt_have })

def add_progress(request, project_id):
    form = ProgressForm(request.POST)
    if form.is_valid():
        new_progress = form.save(commit=False)
        new_progress.project_id = project_id
        new_progress.save()
    return redirect('detail', project_id=project_id)

def assoc_component(request, project_id, component_id):
    Project.objects.get(id=project_id).components.add(component_id)
    return redirect('detail', project_id=project_id)


class ProjectCreate(CreateView):
    model = Project
    fields = '__all__'
    success_url = '/projects/'

class ProjectUpdate(UpdateView):
  model = Project
  fields = '__all__'

class ProjectDelete(DeleteView):
  model = Project
  success_url = '/projects/'

class ComponentList(ListView):
  model = Component

class ComponentDetail(DetailView):
  model = Component

class ComponentCreate(CreateView):
  model = Component
  fields = '__all__'

class ComponentUpdate(UpdateView):
  model = Component
  fields = ['name', 'cost']

class ComponentDelete(DeleteView):
  model = Component
  success_url = '/toys/'