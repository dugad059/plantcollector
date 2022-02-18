from django.db import models
from django.urls import reverse


# Create your models here.

WATERINGS = (
    ('C', 'Cup'),
    ('D', 'Drain-out')
)

"""
=============================
      ADDITIVES MODELS
=============================

"""
class Additive(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail_additives', kwargs={'additive_id': self.id})

"""
=============================
      PLANTS MODELS
=============================

"""

class Plant(models.Model):
    name = models.CharField(max_length=100)
    waterings =  models.CharField(max_length=100)
    sunlight = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    additives = models.ManyToManyField(Additive)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail_plants', kwargs={'plant_id': self.id})

"""
=============================
      WATERING MODELS
=============================

"""

class Watering(models.Model):
    date = models.DateField('Watering Date')
    amount = models.CharField(max_length=1, choices=WATERINGS, default=WATERINGS[0][0])

    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_amount_display()} on {self.date}"


    