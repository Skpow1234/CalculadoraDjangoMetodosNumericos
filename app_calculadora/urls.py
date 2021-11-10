from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.vista_inicio, name='inicio'),
    path('conversion/', include('app_conversion.urls'), name="app_conversion"),
    #path('sistema_ieee/', include('app_sistema_ieee.urls'), name="app_sistema_ieee"),
    path('raices/', include('app_raices.urls'), name="app_raices"),
    path('derivadas/', include('app_derivadas.urls'), name="app_derivadas"),
    #path('graficador/', include('graficador.urls'), name="graficador"),
    path('evaluador', include('app_evaluador.urls'), name='evaluador'),
    path('integrales/', include('app_integrales.urls'), name="integrales"),
    path('matrices/', include('app_matrices.urls'), name="matrices"),
    path('', include('graficador.urls'), name="graficador")
]
