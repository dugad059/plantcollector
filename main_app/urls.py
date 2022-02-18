from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('plants/', views.plants_index, name='index_plants'),
    path('plants/<int:plant_id>/', views.plants_detail, name='detail_plants'),
    path('plants/create/', views.PlantCreate.as_view(), name='create_plants'),
    path('plants/<int:pk>/update/', views.PlantUpdate.as_view(), name='update_plants'),
    path('plants/<int:pk>/delete/', views.PlantDelete.as_view(), name='delete_plants'),
    path('plants/<int:plant_id>/add_watering', views.add_watering, name='add_watering'),
]   