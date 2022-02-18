from django.shortcuts import render, redirect
from .models import Plant, Additive
from .forms import WateringForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def add_watering(request, plant_id):
    form = WateringForm(request.POST)
    if form.is_valid():
        new_watering = form.save(commit=False)
        new_watering.plant_id = plant_id
        new_watering.save()
    return redirect('detail_plants', plant_id=plant_id)

def assoc_additive(request, plant_id, additive_id):
  Plant.objects.get(id=plant_id).additives.add(additive_id)
  return redirect('detail_plants', plant_id=plant_id)


"""
=============================
      PLANTS ROUTES
=============================

"""


def plants_index(request):
    plants = Plant.objects.all()
    return render(request, 'plants/index.html', {'plants': plants})


def plants_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    additives_toy_doesnt_have = Additive.objects.exclude(id__in = plant.additives.all().values_list('id'))
    watering_form = WateringForm()
    return render(request, 'plants/detail.html',
                  {'plant': plant,
                  'watering_form': watering_form,
                  'additives' : additives_toy_doesnt_have
                  })


class PlantCreate(CreateView):
    model = Plant
    fields = ('name', 'waterings', 'sunlight', 'description')


class PlantUpdate(UpdateView):
    model = Plant
    fields = ('name', 'waterings', 'sunlight', 'description')


class PlantDelete(DeleteView):
    model = Plant
    success_url = '/plants/'

"""
=============================
      ADDITIVES ROUTES
=============================

"""
def additives_index(request):
    additives = Additive.objects.all()
    return render(request, 'additives/index.html', {'additives': additives})

def additives_detail(request, additive_id):
    additive = Additive.objects.get(id=additive_id)
    return render(request, 'additives/detail.html', {'additive': additive})

class AdditiveCreate(CreateView):
    model = Additive
    fields = '__all__'

class AdditiveUpdate(UpdateView):
    model = Additive
    fields = ['name']


class AdditiveDelete(DeleteView):
    model = Additive
    success_url = '/additives/'


