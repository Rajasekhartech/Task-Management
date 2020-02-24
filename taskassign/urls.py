from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name = "home_page"),
    path('task/', task_page, name = "task_page"),
    path('add/', TaskView.as_view(), name = 'task_add'),
    path('assign/', assign_task.as_view(), name = 'assign_task'),
    path('<int:id>/detail/', task_detail, name = "task_detail"),
    # path('<int:id>/dept1/', dept1, name = "dept1"),
    path('department/',department, name = "department"),
    path('<int:id>/progress/', task_progress, name = "task_progress"),
]