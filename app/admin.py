from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Project)
admin.site.register(PolygonPoints)
admin.site.register(Cluster)
admin.site.register(DataPoint)