from django.urls import path
from app import views
from django.urls import path

urlpatterns = [
    url(r'^$', views.landing_page),
    url(r'^dashboard', views.dashboard_view),
    url(r'^login', views.LoginView, name='login'),
    url(r'^logout',views.LogoutView),
    url(r'^projects/construction/new',views.NewConstructionProjectView),
    url(r'^projects/maintenance/new',views.NewMaintenanceProjectView),
    url(r'^projects/construction/<int:project_id>/add',views.AddPolygonPointsView),
    url(r'^projects/maintenance/<int:project_id>/add',views.AddRectangleView),
    path('projects/<int:project_id>/timeline',views.ShowHeatMapsByTime),
]
