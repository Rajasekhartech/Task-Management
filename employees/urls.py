from django.urls import path
from .views import *

urlpatterns = [
    path('', employee_list, name= 'employee_list'),
    path('add/', employee_add, name = 'employee_add'),
    path('<int:id>/delete/', employee_delete, name = 'employee_delete'),
    path('<int:id>/detail/', employee_details, name = 'employee_details'),
    ]