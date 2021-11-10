from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista_derivadas, name="derivadas"),
    path('derivada_numerica/', views.vista_derivada_numerica, name="derivada_numerica"),
    path('derivada_simbolica/', views.vista_derivada_simbolica, name="derivada_simbolica"),
    #Calculos
    path('derivada_numerica/calcular/', views.mostrar_calculo_derivada_numerica, name="calcular_derivada_numerica"),
    path('derivada_simbolica/calcular/', views.mostrar_calculo_derivada_simbolica, name="calcular_derivada_simbolica"),

]
