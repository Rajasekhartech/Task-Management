from django.contrib import admin
from .models import tasks, dept_assign_task
# Register your models here.

admin.site.register(tasks)
admin.site.register(dept_assign_task)
