import django_filters
from django_filters import DateFilter
from .models import Task

class TaskFilter(django_filters.FilterSet):
    date = DateFilter(field_name='deadline_date', lookup_expr='gte')
    class Meta:
        model = Task
        fields = ['deadline_date']
        exclude = ['task', 'deadline_date']