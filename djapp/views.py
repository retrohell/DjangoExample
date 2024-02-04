from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Users
from django.shortcuts import get_object_or_404, render, redirect
from .forms import UsersForm

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
    return render(request, 'users.html', {
        'users': users
    })

def usersById(request, id):
    user = get_object_or_404(Users, id=id)
    return HttpResponse('User: %s  ' % user.name)

def usersCreate(request):
    if request.method == 'GET':
        return render(request, 'create_user.html', {
        'form': UsersForm()
        })
    else:
        Users.objects.create(name=request.POST['name'], description=request.POST['description'])
        return redirect('/users/')
    
