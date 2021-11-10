from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista_raices, name='raices'),
    path('biseccion/', views.vista_raices_biseccion, name="biseccion"),
    path('falsa_posicion/', views.vista_raices_falsa_posicion, name="falsa_posicion"),
    path('newthon_raphson/', views.vista_raices_newthon_raphson, name="newton_raphson"),
    path('secante/', views.vista_raices_secante, name="secante"),
    path('polinomio/', views.vista_raices_polinomio, name="polinomio"),
    #Calculo
    path('biseccion/calcular/', views.mostrar_calculo_biseccion, name="calcular_biseccion"),
    path('falsa_posicion/calcular/', views.mostrar_calculo_falsa_posicion, name="calcular_falsa_posicion"),
    path('newthon_raphson/calcular/', views.mostrar_calculo_newthon_raphson, name="calcular_newton_raphson"),
    path('secante/calcular/', views.mostrar_calculo_secante, name="calcular_secante"),
    path('polinomio/calcular/', views.mostrar_calculo_polinomio, name="calcular_polinomio")
]
