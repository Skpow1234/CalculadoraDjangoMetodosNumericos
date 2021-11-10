from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.vista_conversion, name='conversion'),
    path('binario/', views.vista_conversion_binario, name="conversion_binario"),
    path('octal/', views.vista_conversion_octal, name="conversion_octal"),
    path('decimal/', views.vista_conversion_decimal, name="conversion_decimal"),
    path('hexadecimal/', views.vista_conversion_hexadecimal, name="conversion_hexadecimal"),
    path('ieee754/', views.vista_conversion_ieee754, name="conversion_ieee754"),
    #Calculo
    path('binario/calcular/', views.mostrar_calculo_binario, name='convertir_binario'),
    path('octal/calcular/', views.mostrar_calculo_octal, name='convertir_octal'),
    path('decimal/calcular/', views.mostrar_calculo_decimal, name='convertir_decimal'),
    path('hexadecimal/calcular/', views.mostrar_calculo_hexadecimal, name='convertir_hexadecimal'),
    path('ieee754/calcular/', views.mostrar_calculo_ieee754, name="convertir_ieee754"),
    path('ieee754/calcular_32bits/', views.mostrar_calculo_ieee754_32Bits_a_decimal, name="convertir_ieee754_32bits"),
    path('ieee754/calcular_64bits/', views.mostrar_calculo_ieee754_64Bits_a_decimal, name="convertir_ieee754_64bits")
]
