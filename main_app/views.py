from dataclasses import field
from django.shortcuts import render
from .models import Plant
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


"""
=============================
      PLANTS ROUTES
=============================

"""

def plants_index(request):
    plants = Plant.objects.all()
    return render(request, 'plants/index.html', {'plants' : plants})

def plants_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    return render(request, 'plants/detail.html', { 'plant' : plant })

class PlantCreate(CreateView):
    model = Plant
    fields = '__all__'

class PlantUpdate(UpdateView):
    model = Plant
    fields = ('name', 'waterings', 'sunlight', 'description')

class PlantDelete(DeleteView):
    model = Plant
    success_url = '/plants/'