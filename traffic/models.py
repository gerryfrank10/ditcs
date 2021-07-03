from django.contrib.gis.db import models
from django.urls import reverse

class Light(models.Model):
    state_choice = (
        ('A', 'ON'),
        ('B', 'OFF'),
    )

    name = models.CharField(max_length=20, help_text="The light on the road")
    state = models.CharField(max_length=2, choices=state_choice)

    def __str__(self):
        return self.name

class Road(models.Model):
    direction_choice = (
        ('R', 'Right to left'),
        ('L', 'Left to right'),
        ('U', 'Up to down'),
        ('D', 'down to up'),
    )
    road_status = (
        ('A', 'Available'),
        ('M', 'Maintenance'),
        ('R', 'Restricted'),
    )
    name = models.CharField(max_length=20, help_text="The road name")
    distance = models.FloatField(help_text="The distance of the road")
    light = models.ForeignKey('Light', null=True, blank=True, on_delete=models.SET_NULL)
    direction = models.CharField(max_length=2, help_text="The direction of the road",choices=direction_choice)
    status = models.CharField(max_length=2, blank=True, null=True, help_text="Road status availability", default='A')

    def __str__(self):
        return f"{self.name}, {self.distance} km"

    def get_absolute_url(self):
        return reverse('road-detail', args=[str(self.id)])

class Traffic(models.Model):
    traffic_status = (
        ('hp', 'High Populoated'),
        ('lp', 'Low Populoated'),
        ('mp', 'Medium Populoated'),
    )

    time = models.DateTimeField(auto_now_add=True,)
    count = models.IntegerField(help_text="The total number of cars on the road")
    road = models.ForeignKey('Road', on_delete=models.CASCADE)
    status = models.CharField(max_length=2, default='mp',)

    def __str__(self):
        return f"{self.time} and {self.count}"

    def get_absolute_url(self):
        return reverse('traffic-detail', args=[str(self.id)])

