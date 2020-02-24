from django.shortcuts import render
from .models import tasks, dept_assign_task
from django.contrib.auth.models import User
from django.http import Http404 , HttpResponseRedirect, HttpResponse
from django.views.generic import View
from .forms import TaskForm , task_asign_dept1

from employees.models import Profile

# Create your views here.
def home(request):
    if request.user.profile.designation == "Admin":
        context = {}
        task = dept_assign_task.objects.all()
        user = User.objects.all()
        status = tasks.objects.all()
        context['task'] = task
        context['user'] = user
        context['status'] = status
        return render(request, 'home.html', context)
    else:
        return HttpResponseRedirect("task/")
"""

"""
def task_page(request):
    if request.user.profile.designation == "Admin":
        context ={}
        task = tasks.objects.all()
        context['task'] = task
        context['title'] = 'tasks'
        return render(request, "task/tasks.html", context)
    else:
        context = {}
        task = tasks.objects.all()
        assign = dept_assign_task.objects.filter(user_id = request.user.id )
#        assign =dept_assign_task.objects.all()
        print(request.user.id)
        for i in assign:
            print(i)
#        if request.user.id == a
        print("AAAAAAAAAAAAAA.....",assign)
        context['task'] = task
        context['assign'] = assign
        context['title'] = 'tasks'
        return render(request,"task/tasks.html", context)



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

# def dept1(request, id = None):
#    if request.method == "GET":
#        context = {}
#        try:
#            task = tasks.objects.get(id=id)
#        except:
#            raise Http404
#        context['task'] = task
#        dept_users = Profile.objects.all().filter(department = 'dept1')
#        context['dept_users'] = dept_users
#        context['title'] = "Employees in department 1"
#        return render(request,'task/dept1.html', context)
#    elif request.method=="POST":
#        context = {}
#        return render(request,'task/tasks.html', context)

class assign_task(View):
    def get(self,request):
        task_form = task_asign_dept1()
        template ="task/assign_task.html"
        context ={'task_form' : task_form}
        return render(request,template,context)

    def post(self, request):
        task_form = task_asign_dept1(request.POST)
        if task_form.is_valid():
            new_task = task_form.save(commit=False)
            new_task.created_by = request.user
            new_task.save()
            status = tasks.objects.get(pk=new_task.task_id)
            status.status = "in_process_dept1"
            status.save()
            print(status.status)
            print(new_task.task_id)
            return HttpResponseRedirect("/")
        context = {"task_form": task_form}
        return render(request, 'task/new_task.html', context)
def department(request):
    context = {}
    context['title'] = "depatments"
    return render(request, "task/departments.html", context)


def task_progress(request ,id = None):
    context = {}

    try:
        task = tasks.objects.get(id = id)
        assign = dept_assign_task.objects.all()
        print("TASKKKKKKKKKKKKKid ",task.id)
        print("CCCCCCCCCCCCCCCCCCCCCCCCCC", assign)
        tasks.objects.filter(pk=task.id).update(status='compleated_dept1')

        if (assign.user_id == request.user.id) and (assign.task_id == task.id):
            print("CCCCCCCCCCCCCCCCCCCCCCCCCC",assign.task_id,task.id)
            dept_assign_task.objects.filter(task_id=task.id).update(status='compleated_dept1')
    except:
        raise Http404
    return HttpResponseRedirect("/")




