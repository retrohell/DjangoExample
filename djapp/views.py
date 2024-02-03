from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Users
from django.shortcuts import get_object_or_404, render
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
    Users.objects.create(name=request.GET['name'], description=request.GET['description'])
    return render(request, 'create_user.html', {
        'form': UsersForm()
    })
