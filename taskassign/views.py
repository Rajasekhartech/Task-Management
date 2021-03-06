from django.shortcuts import render
from .models import tasks, dept_assign_task
from django.contrib.auth.models import User
from django.http import Http404 , HttpResponseRedirect, HttpResponse
from django.views.generic import View
from .forms import TaskForm , task_asign_dept1 , task_asign_dept2
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from employees.models import Profile

# Create your views here.
def home(request):
    return render(request,"base_home.html")

@login_required
def dashboard(request):
     if request.user.profile.designation == "Admin":
         context = {}
         task = dept_assign_task.objects.all()
         users = User.objects.all()
         context['task'] = task
         context['a'] = users
         return render(request, 'home.html', context)
     else:
         return render(request,"task/tasks.html")

@login_required()
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
        a = Q(status__contains="in_process_dept1")
        b = Q(status__contains="in_process_dept2")
        c = Q(user_id__contains = request.user.id)
        if request.user.profile.department == "dept1":
            assign = dept_assign_task.objects.filter((a))
        elif request.user.profile.department =="dept2":
            assign = dept_assign_task.objects.filter((b))
        context['task'] = task
        context['assign'] = assign
        context['title'] = 'tasks'
        return render(request,"task/tasks.html", context)


@login_required()
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
            return HttpResponseRedirect("/task")
        context = {"task_form" : task_form}
        return render(request, 'task/new_task.html', context)


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
            assign = dept_assign_task.objects.get(task_id=new_task.task_id)
            assign.status = "in_process_dept1"
            assign.save()
            print(status.status)
            print(assign.status)
            print(new_task.task_id)
            return HttpResponseRedirect("/task")
        context = {"task_form": task_form}
        return render(request, 'task/new_task.html', context)


class assign_task_dept2(View):
    def get(self,request):
        task_form = task_asign_dept2()
        template ="task/assign_task_dept2.html"
        context ={'task_form' : task_form}
        return render(request,template,context)

    def post(self, request):
        task_form = task_asign_dept2(request.POST)
        if task_form.is_valid():
            new_task = task_form.save(commit=False)
            new_task.created_by = request.user
            new_task.save()
            status = tasks.objects.get(pk=new_task.task_id)
            status.status = "in_process_dept2"
            status.save()
            user = User.objects.all()
            for users in user:
                if new_task.user_id == users.id:
                    print(users.id)
                    dept_assign_task.objects.filter(user_id=new_task.user_id).update(status="in_process_dept2")
                else:
                    pass
            return HttpResponseRedirect("/task")
        context = {"task_form": task_form}
        return render(request, 'task/new_task.html', context)


@login_required()
def department(request):
    context = {}
    context['title'] = "depatments"
    return render(request, "task/departments.html", context)

@login_required()
def task_progress(request ,id = None):
    try:
        task = tasks.objects.get(id = id)
        if request.user.profile.department == "dept1":
            tasks.objects.filter(pk=task.id).update(status='compleated_dept1')
        elif request.user.profile.department == "dept2":
            tasks.objects.filter(pk=task.id).update(status='compleated_dept2')

        if request.user.profile.department == "dept1":
            dept_assign_task.objects.filter(user_id=request.user.id).update(status='compleated_dept1')
        else:
            dept_assign_task.objects.filter(user_id=request.user.id).update(status='compleated_dept2')
    except:
        raise Http404

    return HttpResponseRedirect("/task")




