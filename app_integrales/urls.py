from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista_integrales, name="integrales"),
    path('rectangulos/', views.vista_integracion_numerica_rectangulos, name="rectangulos"),
    path('trapecios/', views.vista_integracion_numerica_trapecios, name="trapecios"),
    path('simpson1_3/', views.vista_integracion_numerica_simpson1_3, name="simpson1_3"),
    path('simpson3_8/', views.vista_integracion_numerica_simpson3_8, name="simpson3_8"),
    path('montecarlo/', views.vista_integracion_numerica_montecarlo, name="montecarlo"),
    #CALCULOS
    path('rectangulos/calcular/', views.mostrar_calculo_integracion_numerica_rectangulos, name="calcular_integral_numerica_rectangulos"),
    path('trapecios/calcular/', views.mostrar_calculo_integracion_numerica_trapecios, name="calcular_integral_numerica_trapecios"),
    path('simpson1_3/calcular/', views.mostrar_calculo_integracion_numerica_simpson1_3, name="calcular_integral_numerica_simpson1_3"),
    path('simpson3_8/calcular/', views.mostrar_calculo_integracion_numerica_simpson3_8, name="calcular_integral_numerica_simpson3_8"),
    path('montecarlo/calcular/', views.mostrar_calculo_integracion_numerica_montecarlo, name="calcular_integral_numerica_montecarlo")
]
