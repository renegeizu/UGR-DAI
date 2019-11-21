Desarrollo de Aplicaciones para Internet (2019-2020)
 Guión de Prácticas 5: Django
----------------------------------------------------

#### Resumen

`Django` es un framework web completo ampliamente usado. Cuenta con un motor de plantillas propio (muy similar a `Jinja 2`) así una arquitectura muy similar a `Modelo / Vista / Controlador`. En esta práctica vamos a instalar dicho framework y adaptar nuestra aplicación desarrollada en `Flask` a este nuevo framework.

#### Instalación y puesta en marcha de `Django`

Para empezar a funcionar con `Django` partiremos de un esqueleto básico que contiene los ficheros de `Docker` y las dependencias mínimas de nuestra aplicación. Podéis descargar dicho esqueleto de la carpeta `materiales` de `SWAD`. Los ficheros `Docker` para esta práctica están basado en los que se pueden encontrar en: [Quickstart: Compose and Django](https://docs.docker.com/compose/django/).

En general en esta práctica seguiremos los pasos de [este tutorial](http://drksephy.github.io/2015/07/16/django/). Ejecutaremos el siguiente comando DENTRO de nuestro docker para crear la estructura de directorios y archivos para nuestras aplicaciones:

``` {.language-bash}
$ django-admin startproject sitio_web
```

Podemos compropbar que funciona iniciando el servidor de desarrollo:

``` {.language-bash}
$ cd sitio_web
$ python3 manage.py runserver 0.0.0.0:5000
```

Creamos ahora una aplicación dentro del projecto:

``` {.language-bash}
$ python3 manage.py startapp miaplicacion
```

Creamos un directorios para los templates y para los archivos estáticos

``` {.language-bash}
$ mkdir templates
$ mkdir static
```

y los apuntamos en el archivo `sitio_web/settings.py`

``` {.language-python}
TEMPLATES = [
{
'DIRS':[os.path.join(BASE_DIR, 'templates')]
...
```

``` {.language-python}
# al final del archivo settings.py
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```

y apuntamos también nuesta aplicación:

``` {.language-python}
INSTALLED_APPS = (
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'miaplicacion',
)
```

Ahora podemos iniciar la bases de datos SQL (lite) que usa django para los datos de los usuarios (registro, autentificación y autorización), que usaremos más adelante.

``` {.language-bash}
$ python3 manage.py migrate
```

Esto habrá que hacerlo cada vez que hagamos cambios en la BD SQL

Creamos ahora un administrador de la BD (SQL)

``` {.language-bash}
$ python3 manage.py createsuperuser
```

y tendremos acceso a la aplicación de administración de la BD en:

     http://localhost:8000/admin

8000 es el puerto por defecto, también se puede lanzar desde otro puerto:

``` {.language-bash}
 $ python3 manage.py runserver 0.0.0.0:5000
```

Y podemos ahora hacer una aplicación siguiendo los pasos desde el *Step 3: Your first view* del tutorial y los templates de las tareas anteriores:

Solo tendremos que cambiar, el enrutador (ahora en dos archivos aparte) `sitio_web/urls.py`:

``` {.language-python}
# sitio_web/urls.py

   from django.conf.urls import include, url
   from django.contrib import admin

   urlpatterns = [
     url(r'^miaplicacion/', include('miaplicacions.urls')),
     url(r'^admin/', admin.site.urls),
   ]
```

y en un nuevo archivo donde especificamos las rutas que comiencen por **/miaplicacion/**, `miaplicacion/urls.py`

``` {.language-python}
# miaplicacion/urls.py

from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^test_template/$', views.test_template, name='test_template'),
]
```

El código del controlador lo pondremos en el archivo `miaplicacion/views.py`

``` {.language-python}
# miaplicacion/views.py

from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Hello World!')

def test_template(request):
    context = {}   # Aquí van la las variables para la plantilla
    return render(request,'test.html', context)
```

`Django` utiliza una [libreria de templates](https://docs.djangoproject.com/en/1.11/ref/templates/), muy parecida al `Jinja2` de `Flask`: solo cambian las instrucciones para cargar los archivos estaticos y los nombres de los enlaces

``` {.language-markup}
   {% load static %}
   ...
  <link  href="{% static 'css/style.css' %}" rel="stylesheet" media="screen">
  ...
  <a href="{% url 'name para la url' %}"> </a>
```

El archivo `miaplicacion/models.py` está para poner todo lo relativo a los datos (modelo), de manera que las funciones de BDs estén en un arhivo separado para seguir el módelo [MVC](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller). En esta práctica todavía no trabajaremos con los modelos de `Django`, por lo que aún no habrá que cambiar nada.

**Nota:** Recomendamos la consulta del tutorial: [Tutorial de Django Girls](https://tutorial.djangogirls.org/es/).

**Nota 2:** Los comandos que usamos para los diversos comandos de `Django` (iniciar base de datos, crear administrador, etc) podemos lanzarlos haciendo uso de un script. Mira el fichero `Makefile` del esqueleto de la aplicación.


