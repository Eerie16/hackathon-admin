from django.db import models

# Create your models here.


class Project(models.Model):
    type_choices = [('construction','construction'), ('maintenance', 'maintenance')]
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    type = models.CharField(choices=type_choices,max_length=100)
    city = models.CharField(max_length=100)
    date_started = models.DateField()

    def __str__(self):
        return f'{self.name}  -- {self.type}'


class PolygonPoints(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()
    order = models.IntegerField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)    

    def __str__(self):
        return f'{self.order} -- {self.project}'


class Cluster(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date_formed = models.DateField()

    def __str__(self):
        return f'{self.lat} {self.lng} -- {self.project}'


class DataPoint(models.Model):
    cluster = models.ForeignKey('Cluster', on_delete=models.CASCADE)
    image_url = models.URLField()
    lat = models.FloatField()
    lng = models.FloatField()
    date_uploaded = models.DateField()
    is_verified = models.BooleanField()

    def __str__(self):
        return f'{self.lat} {self.lng} -- {self.cluster}'
