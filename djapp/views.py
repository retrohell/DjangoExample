from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Users, Projects
from django.shortcuts import get_object_or_404, render, redirect
from .forms import UsersForm, ProjectsForm

# Create your views here.
def index(request):
    title = 'Django Example'
    return render(request, 'index.html', {
        'title': title
    })
# Path: djexample/djapp/urls.py

def about(request):
    username = 'John Doe'
    return render(request, 'about.html', {
        'username': username
    })

def users(request):
    users = Users.objects.all()
    #data = {
    #    'users': list(users.values())
    #}
    return render(request, 'users/users.html', {
        'users': users
    })

def usersById(request, id):
    user = get_object_or_404(Users, id=id)
    return HttpResponse('User: %s  ' % user.name)

def usersCreate(request):
    if request.method == 'GET':
        return render(request, 'users/create_user.html', {
        'form': UsersForm()
        })
    else:
        Users.objects.create(name=request.POST['name'], description=request.POST['description'])
        return redirect('/users/')
    
def projects(request):
    project = Projects.objects.all()
    return render(request, 'projects/projects.html', {
        'projects': project
    })

def projectsCreate(request):
    if request.method == 'GET':
        return render(request, 'projects/create_projects.html', {
            'form': ProjectsForm()
        })
    elif request.method == 'POST':
        """
        if request.POST['status'] == "on": 
            x = 'True'
        else:
            x = 'False'
        """
        Projects.objects.create(name=request.POST['name'], description=request.POST['description'])
        return redirect('/projects/')
