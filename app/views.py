from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from datetime import datetime,timedelta
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse


global toast_data

def LoginView(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')

    template_name = 'login.html'
    if request.method == "POST":
        # TODO uncomment
        # post = request.POST
        # username = post.get('username','dummy')
        # password = post.get('password', 'pass')
        # user = authenticate( username=username, password=password)
        # print(user)
        # if user is not None:
        #     login(request,user)
        return redirect('/dashboard')
        # else:
        #     return render(request,template_name,{})
    else:
        return render(request,template_name,{})


def LogoutView(request):
    logout(request)
    return redirect('/login/')


# TODO uncomment
# @login_required()
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
        return redirect('/dashboard')
    return render(request, template_name)


@csrf_exempt
def AddRectangleView(request, project_id):
    template_name = 'add_rectangle.html'
    if request.method == 'POST':
        post = request.POST
        print(post)
        return redirect('/dashboard')
    return render(request, template_name)


def ShowHeatMapsByTime(request,project_id):
    template_name = 'heatmaps_time.html'
    clusters = Cluster.objects.filter(project=project_id).order_by('date_formed')
    counts = []
    start_date = Project.objects.get(id = project_id).date_started
    print(start_date)
    delta = datetime.now() - start_date
    days = delta.days
    points = []
    for day in range(days):
        temp_arr= [{'lat': x.lat, 'lng': x.lng, 'count': 0} for x in clusters]
        for cluster_number in range(len(clusters)):
            gt_time = start_date + timedelta(days=(day-5)) 
            lt_time = start_date + timedelta(days=(day+5))
            temp_arr[cluster_number]['count'] = DataPoint.objects.filter(cluster= clusters[cluster_number], date_uploaded__gt=gt_time, date_uploaded__lt= lt_time).count()
        points.append(temp_arr)
    context = {
        'points': points
    }
    print(context)
    return render(request, template_name, context=context)


def landing_page(request):
    return render(request, 'blank.html')


# TODO uncomment
# @login_required(login_url="/login")
def dashboard_view(request):
    return render(request, 'index.html',{'contracts':Project.objects.all()})


@csrf_exempt
def ShowNearestImage(request):
    template_name = "nearest_image.html"
    if request.method == "POST":
        post = request.POST
        lat = float(post['lat'])
        lng = float(post['lng'])
        datapoints = DataPoint.objects.filter(is_verified=True)
        datapoints = sorted(datapoints, key= lambda i: abs(lat - i.lat)+abs(lng - i.lng))
        return JsonResponse({'image':datapoints[0].image_url})
    else:
        return render(request, template_name)
