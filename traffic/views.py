from django.shortcuts import render
from django.http import HttpResponse
import matplotlib.pyplot as plt
from rest_framework import viewsets
import io, base64
from rest_framework import viewsets
from .models import Traffic, Road, Light
from .serializers import TrafficSerializer, RoadSerializer, LightSerializer

# Create your views here.
def index(request):

    # Draw a figure for tests
    fig, ax = plt.subplots()
    ax.plot([1,2,3,4], [4,2,1,4])
    # ax.set_title("Test plots from dummy data")
    
    flike = io.BytesIO()
    fig.savefig(flike)
    b64 = base64.b64encode(flike.getvalue()).decode()

    flike = io.BytesIO()
    ch, jf = plt.subplots()
    students = [22,33,12]
    langs = ["C++", "Java", "Python"]
    jf.pie(students, labels=langs)
    ch.savefig(flike)
    pie = base64.b64encode(flike.getvalue()).decode()

    context = {'chart': b64, 'pie': pie}

    return render(request, 'index.html', context=context)

def camera(request):
    return render(request, 'camera.html')

def profile(request):
    return render(request, 'profile.html')

class TrafficViewSet(viewsets.ModelViewSet):
    queryset = Traffic.objects.all()
    serializer_class = TrafficSerializer

class RoadViewSet(viewsets.ModelViewSet):
    queryset = Road.objects.all()
    serializer_class = RoadSerializer

class LightViewSet(viewsets.ModelViewSet):
    queryset = Light.objects.all()
    serializer_class = LightSerializer