from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^$', views.landing_page),
    url(r'^dashboard', views.dashboard_view),
    url(r'^login', views.LoginView, name='login'),
    url(r'^logout',views.LogoutView),
    url(r'^projects/new',views.NewProjectView),
    url(r'^projects/construction/<int:project_id>/add',views.AddPolygonPointsView),
    url(r'^projects/maintenance/<int:project_id>/add',views.AddRectangleView),
    url(r'^projects/<int:project_id>/timeline',views.ShowHeatMapsByTime),
]
