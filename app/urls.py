from django.urls import path
from app import views
urlpatterns = [
    path('login/', views.LoginView),
    path('logout/',views.LogoutView)    ,
    path('projects/new',views.NewProjectView),
    path('projects/construction/<int:project_id>/add',views.AddPolygonPointsView),
    path('projects/maintenance/<int:project_id>/add',views.AddRectangleView),
    path('projects/<int:project_id>/timeline',views.ShowHeatMapsByTime),
    path('test/', views.TestView),
    path('datapoints/',views.ShowNearestImage),
]
