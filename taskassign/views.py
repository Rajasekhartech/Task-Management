from django.shortcuts import render
from .models import tasks
from django.http import Http404 , HttpResponseRedirect
from django.views.generic import View
from .forms import TaskForm , task_asign_dept1
from employees.models import Profile

# Create your views here.
def home(request):
    return render(request, 'home.html')

def task_page(request):
    context ={}
    task = tasks.objects.all()
    context['task'] = task
    context['title'] = 'tasks'
    return render(request, "task/tasks.html", context)



def task_detail(request, id = None):
    context = {}
    try:
        task = tasks.objects.get(id = id)
    except:
        raise Http404
    context['task'] = task
    return render(request, "task/task_detail.html" , context)

class TaskView(View):
    def get(self,request):
        task_form = TaskForm(instance=tasks())
        template ="task/new_task.html"
        context ={'task_form' : task_form}
        return render(request,template,context)

    def post(self,request):
        task_form = TaskForm(request.POST ,instance=tasks())
        if task_form.is_valid():
            new_task = task_form.save(commit=False)
            new_task.created_by = request.user
            new_task.save()
            return HttpResponseRedirect("/")
        context = {"task_form" : task_form}
        return render(request, 'task/new_task.html', context)

def dept1(request, id = None):
   if request.method == "GET":
       context = {}
       try:
           task = tasks.objects.get(id=id)
       except:
           raise Http404
       context['task'] = task
       dept_users = Profile.objects.all().filter(department = 'dept1')
       context['dept_users'] = dept_users
       context['title'] = "Employees in department 1"
       return render(request,'task/dept1.html', context)
   elif request.method=="POST":
       context = {}
       return render(request,'task/tasks.html', context)

class assign_task(View):
    def get(self,request):
        task_form = task_asign_dept1()
        template ="task/assign_task.html"
        context ={'task_form' : task_form}
        return render(request,template,context)

    def post(self,request):
        pass




