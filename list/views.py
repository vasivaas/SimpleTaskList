from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .filters import TaskFilter
from .forms import CreateUserForm, TaskForm
from .models import Project, Task



# Create your views here.

def index(request):
    projects = Project.objects.all()
    total_project = projects.count()
    return render(request, 'projects/index.html', context= {
        'projects': projects,
        'total_project': total_project,
    })


def view_project_info(request, pk):
    project = Project.objects.get(id=pk)
    task_for_this_project =  project.task_set.all().order_by('-priority')
    total_tasks = task_for_this_project.count()
    myFilter = TaskFilter(request.GET, queryset=task_for_this_project)
    task_for_this_project = myFilter.qs
    return render(request, 'projects/project_info.html', context= {
        'project_info': project,
        'tasks': task_for_this_project,
        'total_tasks': total_tasks,
        'filter': myFilter,
    })


class ProjectCreate(CreateView):
    model = Project
    fields = ['name']
    initial = {'name':'Project name',}
    success_url = reverse_lazy('index')
    template_name_suffix = '_create'


class ProjectUpdate(UpdateView):
    model = Project
    fields = ['name']
    template_name_suffix = '_update'


class ProjectDelete(DeleteView):
    model = Project
    success_url = reverse_lazy('index')
    template_name_suffix = '_delete'


def task_create(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'task/task_create.html', context={
        'form': form
    })


def task_update(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('project/{id}'.format(id=task.project.id))
    return render(request, 'task/task_update.html', context={
        'form': form
    })


def task_delete(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('project/{id}'.format(id=task.project.id))
    return render(request, 'task/task_delete.html', context={
        'task': task
    })


def registerUser(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Акаунт створив ' + user)
                return redirect('login')
        context = {'form': form, }
        return render(request, 'list/register.html', context)


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'list/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')
