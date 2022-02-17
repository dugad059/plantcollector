from django.db import models
from django.urls import reverse


# Create your models here.

"""
=============================
      PLANTS Models
=============================

"""

class Plant(models.Model):
    name = models.CharField(max_length=100)
    waterings =  models.CharField(max_length=100)
    sunlight = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail_plants', kwargs={'plant_id': self.id})

    