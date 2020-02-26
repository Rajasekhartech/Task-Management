from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.contrib.auth import authenticate,logout,login
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import UserForm
# Create your views here.
from django.contrib.auth.decorators import login_required
@login_required()
def employee_list(request):
    context = {}
    context['users'] = User.objects.all()
    context['title'] = 'Employees'
    return render(request, 'employees/index.html',context)

@login_required()
def employee_details(request, id=None):
     context = {}
     context['user'] = get_object_or_404(User, id = id)
     return render(request,'employees/details.html',context)

@login_required()
def employee_add(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.designation = form.cleaned_data.get('designation')
            user.profile.department = form.cleaned_data.get('depatments_in_organization')
            user.save()
            return redirect('employee_list')
    else:
        form = UserForm()
        return render(request, 'employees/add.html', {'form': form})

@login_required()
def employee_delete(request , id = None):
    user = get_object_or_404(User, id = id)
    if request.method == "POST":
        user.delete()
        return HttpResponseRedirect(reverse('employee_list'))
    else:
        context={}
        context['user'] = user
        return render(request, 'employees/delete.html', context)


class MyProfile(DetailView):
    template_name = 'profile.html'
    def get_object(self, queryset=None):
        return self.request.user.profile

def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user:
            login(request, user)
            if request.GET.get('next', None):
                return HttpResponseRedirect(request.GET['next'])
            return HttpResponseRedirect(reverse('task_page'))



        else:
            context['error'] = "Provide valid credentials !!!"
            return render(request, "auth/login.html", context)
    else:
        return render(request, "auth/login.html", context)

@login_required()
def user_logout(request):
    if request.method=="POST":
        logout(request)
        return HttpResponseRedirect(reverse('user_login'))
