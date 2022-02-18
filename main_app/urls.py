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
    path('plants/<int:plant_id>/assoc_additive/<int:additive_id>', views.assoc_additive, name='assoc_additive'),
    path('additives/', views.additives_index, name='index_additives'),
    path('additives/<int:additive_id>/', views.additives_detail, name='detail_additives'),
    path('additives/create/', views.AdditiveCreate.as_view(), name='create_additives'),
    path('additives/<int:pk>/update/', views.AdditiveUpdate.as_view(), name='update_additives'),
    path('additives/<int:pk>/delete/', views.AdditiveDelete.as_view(), name='delete_additives'),
]   