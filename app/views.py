from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import *
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
# Create your views here.


def LoginView(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')

    template_name = 'login.html'
    if request.method == "POST":
        post = request.POST
        username = post['username']
        password = post['password']
        print(post)
        print (username,password)
        user = authenticate( username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard/')
        else:
            return render(request,template_name,{})
    else:
        return render(request,template_name,{})


@login_required()
def NewProjectView(request):
    template_name = 'add_project.html'
    if request.method == "POST":
        post = request.POST
        type = post['type']
        name = post['name']
        city = post['city']
        new_project = Project(name=name, city=city, type=type, date_started=datetime.now())
        new_project.save()
        if type == "construction":
            return redirect('/projects/construction/'+str(new_project.id)+"/add")
        else:
            return redirect('/projects/maintenance/'+str(new_project.id)+"/add")
    else:
        return render(request, template_name) 


@csrf_exempt
def AddPolygonPointsView(request, project_id):
    template_name = 'add_polygon_points.html'
    if request.method == 'POST':
        post = request.POST
        print(post)
        points = post.getlist('coords')   
        print(points)
        return HttpResponse('Stay Cool')
    return render(request, template_name)


@csrf_exempt
def AddRectangleView(request, project_id):
    template_name = 'add_rectangle.html'
    if request.method == 'POST':
        post = request.POST
        print(post)
        return HttpResponse("cool")
    return render(request, template_name)


def TestView(request):
    return render(request, 'index.html')