from django.urls import path, include
from . import views

urlpatterns = [
    path('graficador/', views.vista_graficador, name='graficador'),
    #Calculos
    path('graficador/graficar/', views.mostrar_grafico, name="graficar"),
    
]
