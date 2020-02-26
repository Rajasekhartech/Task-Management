from django.db import models
from django.contrib.auth.models import User
from employees.models import Profile

# Create your models here.

class tasks(models.Model):
    title = models.TextField(null=False, blank=False)
    description = models.TextField(null= True, blank = True)
    status = models.CharField(default='inactive', max_length=20)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class dept_assign_task(models.Model):
    user = models.ForeignKey(Profile,null=False, blank=False, on_delete=models.CASCADE)
    task = models.ForeignKey(tasks, null= False, blank= False, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now=True)
    status = models.CharField( max_length=20)

    def __str__(self):
        return self.task.title