from django import forms
from .models import tasks
from .models import dept_assign_task
from employees.models import Profile
from django.contrib.auth.models import User


class TaskForm(forms.ModelForm):
    title = forms.CharField(max_length=255, label='task')

    class Meta:
        model = tasks
        fields = ['title','description']

class task_asign_dept1(forms.ModelForm):
    task = forms.ModelChoiceField(queryset= tasks.objects.all().filter(status = 'inactive'))
    user = forms.ModelChoiceField(queryset=Profile.objects.all().filter(department = 'dept1'))


    class Meta:
        model = dept_assign_task
        fields = ['user','task']