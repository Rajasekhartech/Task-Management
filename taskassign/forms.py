from django import forms
from .models import tasks
from .models import dept_assign_task
from employees.models import Profile
from django.db.models import Q
from django.contrib.auth.models import User


class TaskForm(forms.ModelForm):
    title = forms.CharField(max_length=255, label='task')

    class Meta:
        model = tasks
        fields = ['title','description']

class task_asign_dept1(forms.ModelForm):
    a = Q(status__contains = "inactive")
    b = Q(status__contains = "in_process_dept1")
    task = forms.ModelChoiceField(queryset= tasks.objects.filter(a|b))
    user = forms.ModelChoiceField(queryset=Profile.objects.all().filter(department = 'dept1'))


    class Meta:
        model = dept_assign_task
        fields = ['user','task']

class task_asign_dept2(forms.ModelForm):
    a = Q(status__contains = "compleated_dept1")
    b = Q(status__contains = "in_process_dept2")
    task = forms.ModelChoiceField(queryset= tasks.objects.filter(a|b))
    user = forms.ModelChoiceField(queryset=Profile.objects.all().filter(department = 'dept2'))


    class Meta:
        model = dept_assign_task
        fields = ['user','task']