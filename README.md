# Calcul8 — Calculadora Django de Métodos Numéricos

Aplicación web desarrollada en **Django** que implementa una calculadora integral de **Métodos Numéricos**. Permite realizar conversiones entre sistemas numéricos, encontrar raíces de funciones, calcular derivadas e integrales, operar con matrices, evaluar y graficar funciones; todo desde una interfaz web amigable.

> Proyecto académico — Universidad de San Buenaventura, Cali (USB Cali) — 2021.

---

## Tecnologías

[![Python](https://img.shields.io/badge/Python-3.9.5-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-3.2.6-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.21.2-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![SciPy](https://img.shields.io/badge/SciPy-1.7.1-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white)](https://scipy.org/)
[![SymPy](https://img.shields.io/badge/SymPy-1.8-3B5526?style=for-the-badge&logo=sympy&logoColor=white)](https://www.sympy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.4.3-11557C?style=for-the-badge&logo=python&logoColor=white)](https://matplotlib.org/)
[![Pillow](https://img.shields.io/badge/Pillow-8.3.1-8A2BE2?style=for-the-badge&logo=python&logoColor=white)](https://python-pillow.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-4-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![Font Awesome](https://img.shields.io/badge/Font_Awesome-5.15.3-528DD7?style=for-the-badge&logo=fontawesome&logoColor=white)](https://fontawesome.com/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/docs/Web/JavaScript)
[![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)](https://git-scm.com/)

---

## Tabla de contenidos

- [Características](#características)
- [Stack tecnológico](#stack-tecnológico)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Requisitos previos](#requisitos-previos)
- [Instalación](#instalación)
- [Ejecución](#ejecución)
- [Módulos y métodos disponibles](#módulos-y-métodos-disponibles)
- [Mapa de URLs](#mapa-de-urls)
- [Librería interna (`static/lib/`)](#librería-interna-staticlib)
- [Notas de seguridad y despliegue](#notas-de-seguridad-y-despliegue)
- [Licencia](#licencia)

---

## Características

- Evaluador de expresiones matemáticas en un punto.
- Conversión entre sistemas numéricos (binario, octal, decimal, hexadecimal) y estándar **IEEE 754** (32 y 64 bits).
- Búsqueda de raíces de funciones por **Bisección**, **Falsa Posición (Regla Falsa)**, **Newton-Raphson**, **Secante** y raíces de **polinomios**.
- Cálculo de **derivadas numéricas** y **simbólicas** (cualquier orden).
- **Integración numérica**: Rectángulos (izquierda, derecha, punto medio), Trapecios, Simpson 1/3, Simpson 3/8 y Monte Carlo.
- Operaciones con **matrices**: suma, resta, multiplicación, división, escalar, elevación, transpuesta, determinante, inversa, rango, matriz triangular, **factorización LU**, **Gauss-Jordan** y **ajuste de curvas**.
- **Graficador** de funciones con `matplotlib`.
- UI responsive basada en **Bootstrap** y **Font Awesome**, con tablas de iteraciones, gráficos y teoría asociada por cada método.

---

## Stack tecnológico

- **Lenguaje**: Python 3.9.5
- **Framework web**: Django 3.2.6
- **Cómputo simbólico/numérico**: `sympy`, `numpy`, `scipy`, `mpmath`
- **Gráficos**: `matplotlib`
- **Base de datos**: SQLite (incluida por defecto en `db.sqlite3`)
- **Frontend**: HTML5, CSS3, Bootstrap 4, Font Awesome 5

---

## Estructura del proyecto

```
CalculadoraDjangoMetodosNumericos/
├── manage.py
├── requerimientos.txt
├── db.sqlite3
├── calculadora/              # Configuración del proyecto Django (settings, urls, wsgi, asgi)
├── app_calculadora/          # App principal: página de inicio y enrutado de las demás apps
├── app_evaluador/            # Evaluador de funciones en un punto
├── app_conversion/           # Conversión entre sistemas numéricos e IEEE 754
├── app_raices/               # Métodos de búsqueda de raíces
├── app_derivadas/            # Derivadas numéricas y simbólicas
├── app_integrales/           # Integración numérica
├── app_matrices/             # Operaciones con matrices
├── graficador/               # Graficador de funciones
├── templates/                # Plantillas HTML organizadas por módulo
│   ├── inicio/
│   ├── evaluador/
│   ├── conversion/
│   ├── raices/
│   ├── derivadas/
│   ├── integrales/
│   ├── matrices/
│   └── graficador/
└── static/
    ├── css/                  # Bootstrap + estilos propios
    ├── js/                   # Bootstrap, Popper, scripts propios (Display.js, scripts.js, script_matrices.js)
    ├── img/                  # Imágenes generadas (p.ej. grafico.png)
    ├── fontawesome-free-5.15.3-web/
    └── lib/                  # Núcleo de cálculo numérico (clases Python)
        ├── Calculadora.py    # Fachada que orquesta los demás módulos
        ├── Conversion.py     # Conversión entre bases e IEEE 754
        ├── Raiz.py           # Métodos de raíces
        ├── Derivada.py       # Derivación numérica/simbólica
        ├── Integral.py       # Integración numérica
        ├── Matriz.py         # Operaciones matriciales
        ├── Utilidad.py       # Utilidades comunes (formateo y evaluación)
        └── calculo.py
```

---

## Requisitos previos

- **Python 3.9.5** (recomendado, según commit del proyecto).
- `pip` y `venv` disponibles.
- Sistema con soporte para `matplotlib` (en Linux puede requerir paquetes como `python3-tk`).

---

## Instalación

1. Clonar el repositorio.

```bash
git clone https://github.com/Skpow1234/CalculadoraDjangoMetodosNumericos.git
cd CalculadoraDjangoMetodosNumericos
```

2. Crear y activar un entorno virtual.

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate
```

3. Instalar las dependencias.

```bash
pip install -r requerimientos.txt
```

4. Aplicar migraciones (la base SQLite ya está incluida, pero conviene asegurar el estado).

```bash
python manage.py migrate
```

5. (Opcional) Crear un superusuario para acceder al panel de administración.

```bash
python manage.py createsuperuser
```

---

## Ejecución

Levantar el servidor de desarrollo:

```bash
python manage.py runserver
```

Luego abrir en el navegador: <http://127.0.0.1:8000/>

El panel de administración de Django está disponible en: <http://127.0.0.1:8000/admin/>

---

## Módulos y métodos disponibles

### Evaluador
Evalúa una función `f(x)` en un punto específico.

### Conversión de sistemas numéricos
- Binario ↔ Octal / Decimal / Hexadecimal
- Octal ↔ Binario / Decimal / Hexadecimal
- Decimal ↔ Binario / Octal / Hexadecimal
- Hexadecimal ↔ Binario / Octal / Decimal
- **IEEE 754** (32 y 64 bits) ↔ Decimal

### Raíces de funciones
- Bisección
- Falsa Posición (Regla Falsa)
- Newton-Raphson
- Secante
- Raíces de polinomios

Cada método devuelve una **tabla de iteraciones** (límites, raíz aproximada, errores) y el **gráfico** de la función.

### Derivadas
- Derivada **numérica** (evaluada en un punto).
- Derivada **simbólica** (cualquier orden).

### Integrales (área bajo la curva)
- Rectángulos: extremo izquierdo, extremo derecho, punto medio
- Trapecios
- Simpson 1/3
- Simpson 3/8
- Monte Carlo

### Matrices
- Operaciones binarias: suma, resta, multiplicación, división, Gauss-Jordan
- Operaciones unarias: transpuesta, determinante, inversa, rango, triangular, factorización LU, ajuste de curvas
- Por escalar: multiplicación por escalar y elevación a una potencia

### Graficador
Generación gráfica de funciones matemáticas usando `matplotlib`. La imagen resultante se guarda en `static/img/grafico.png` y se sirve desde la plantilla.

---

## Mapa de URLs

| Sección              | Ruta base                                |
|----------------------|------------------------------------------|
| Inicio               | `/`                                      |
| Evaluador            | `/evaluador`                             |
| Conversión           | `/conversion/` (`binario`, `octal`, `decimal`, `hexadecimal`, `ieee754`) |
| Raíces               | `/raices/` (`biseccion`, `falsa_posicion`, `newthon_raphson`, `secante`, `polinomio`) |
| Derivadas            | `/derivadas/` (`derivada_numerica`, `derivada_simbolica`) |
| Integrales           | `/integrales/` (`rectangulos`, `trapecios`, `simpson1_3`, `simpson3_8`, `montecarlo`) |
| Matrices             | `/matrices/`                             |
| Graficador           | `/graficador/`                           |
| Admin de Django      | `/admin/`                                |

Cada submódulo expone además una ruta `…/calcular/` (POST) que recibe los parámetros del formulario y renderiza la vista con los resultados.

---

## Librería interna (`static/lib/`)

El núcleo de cálculo está implementado en clases Python desacopladas de Django, lo que facilita su reutilización y testing:

- **`Calculadora`** — Fachada que centraliza las operaciones (`convertir_bases`, `calcular_raices`, `calcular_derivada_*`, `calcular_integral_numerica`, `calcular_matriz`, `generar_grafico`).
- **`Conversion`** — Conversión entre bases numéricas y representación IEEE 754.
- **`Raiz`** — Algoritmos de búsqueda de raíces, devuelve tablas de iteraciones listas para renderizar.
- **`Derivada`** — Derivación numérica y simbólica (basadas en `sympy`).
- **`Integral`** — Métodos de integración numérica (incluye Monte Carlo).
- **`Matriz`** — Operaciones matriciales sobre `numpy.ndarray` (apoyado por `scipy.linalg`).
- **`Utilidad`** — Funciones auxiliares para formatear y evaluar expresiones de forma segura.

Las vistas Django solo se encargan de recibir el formulario, invocar a estas clases y renderizar la plantilla con los resultados.

---

## Notas de seguridad y despliegue

Este proyecto está configurado como un entorno **de desarrollo / académico**. Antes de exponerlo a producción se recomienda:

- Reemplazar `SECRET_KEY` en `calculadora/settings.py` por una clave segura (preferiblemente vía variable de entorno).
- Cambiar `DEBUG = True` a `DEBUG = False`.
- Definir `ALLOWED_HOSTS` con los dominios o IPs correspondientes.
- Migrar de SQLite a un motor de base de datos productivo (PostgreSQL, MySQL).
- Servir los archivos estáticos con `collectstatic` y un servidor adecuado (nginx, WhiteNoise, etc.).
- Validar/sanitizar las expresiones recibidas en los formularios antes de evaluarlas.


---

## Licencia

Proyecto académico sin licencia explícita definida. Si vas a reutilizar el código para fines distintos al educativo, contacta a los autores o agrega un archivo `LICENSE` con la licencia que prefieras (por ejemplo, MIT).

---

**Repositorio**: <https://github.com/Skpow1234/CalculadoraDjangoMetodosNumericos>
