from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista_evaluador, name="evaluador"),
    #Calculos
    path('calcular/', views.mostrar_calculo_evaluador, name="evaluador_calcular"),
]