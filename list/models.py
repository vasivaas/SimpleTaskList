from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.
class Project(models.Model):
    name = models.CharField("Project name", max_length=100)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, unique=False)

    def get_absolute_url(self):
        return reverse('project_info', args=[str(self.id)])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Project'
        verbose_name_plural='Projects'


class Task(models.Model):
    name = models.CharField("Task name", max_length=100)
    created_date = models.DateTimeField("Create date", auto_now_add=True)
    deadline_date = models.DateField("Deadline date", null=True, blank=True, default=datetime.today)
    TASK_PRIORITY = (
        ('1', 'low priority'),
        ('2', 'below average priority'),
        ('3', 'average priority'),
        ('4', 'above average priority'),
        ('5', 'high priority'),
    )
    priority = models.CharField(max_length=1, choices=TASK_PRIORITY, blank=True, default='1', help_text='Select a task priority (1-low and 5-high)')
    completed = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, unique=False)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Task'
        verbose_name_plural='Tasks'
