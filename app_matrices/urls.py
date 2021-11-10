from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista_matrices, name='matrices'),

    #Calculo
    path('guardar/', views.guardar_matrices, name="guardar_matrices"),
    path('calcular/', views.mostrar_calculo_matrices, name="calcular_matrices"),
]