from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Task, Project


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'priority', 'deadline_date', 'completed']



class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name']
        

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
