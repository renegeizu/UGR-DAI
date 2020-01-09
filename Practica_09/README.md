`D`esarrollo de `A`plicaciones para `I`nternet    (2019-2020)
-------------------------------------------------------------

#### Guión de Prácticas 9: Despliegue

La última práctica consiste en tener una aplicación web desplegada en un ambiente de 'producción', es decir funcionando con la depuración en 'OFF' y conectada a un servidor web como [ngix](https://www.nginx.com/) o [apache](http://httpd.apache.org/) en el puerto 80.

Puede ser alguna que se haya hecho en las prácticas con flask o django, u `otra que se haya hecho en la asignatura de Infraestructura Virtual`.

El despliuege puede ser como [IAAS](https://stackoverflow.com/questions/16820336/what-is-saas-paas-and-iaas-with-examples) en una maquina virtual, o como [PAAS](https://stackoverflow.com/questions/16820336/what-is-saas-paas-and-iaas-with-examples) en un serivdor como [heroku](https://www.heroku.com/), o incluso con [contenedores](https://medium.com/@Alibaba_Cloud/how-to-deploy-a-django-application-with-docker-9514be542909) [docker](https://en.wikipedia.org/wiki/Docker_(software))

##### Despliegue en la maquina virtual con docker-compose

El despliegue de una aplicación con django, está explicado en las transparencias de clase.

Básicamente consiste en poner la configuración de producción, es decir en el archivo **settings.py** estarán las variables:

``` {.language-python}
DEBUG = False

ALLOWED_HOSTS = ['*']
```

Con esto dejará de funciona el servidor de desarrollo, y de servir los contenidos de **/static**, que tendrán que pasar a servirse desde el servidor web de producción. Django tiene un script: [collectstatic](https://docs.djangoproject.com/en/2.2/ref/contrib/staticfiles/) para facilitar pasar los contenidos a otro directorio.

Después habrá que poner funcionar la aplicación desde un servidor web [wsgi](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface), (p.e. [gunicorn](http://gunicorn.org/)), y conectar la aplicación y el resto de servicios que pudiera haber (p.e. servir los archivos static) a un servidor web que también funcione como [proxy inverso](https://en.wikipedia.org/wiki/Reverse_proxy) (p.e. [nginx](https://www.nginx.com/)) en el puerto 80.

Instalamos también en el contenedor de la aplicación [supervisord](http://supervisord.org/), para asegurar que nuestra aplicación esté siempre activada (ver transparencias de clase). La instalación de [supervisord](http://supervisord.org/) la hacemos con `apt-get` (o `apk` en el caso de versiones alpine de la imagen docker). La instalación de [gunicorn](http://gunicorn.org/) la hacemos con [pip](https://es.wikipedia.org/wiki/Pip_(administrador_de_paquetes)).

Usamos entonces dos contenedores, uno para nginx y otro para la aplicación:
 ![](DAI%20Pr%C3%A1ctica%209%20-%20Despliegue_files/nginx-reverse-proxy.png)

**docker-compose.yml**:

``` {.language-yaml}
version: '3.7'
   services:
      nginx:
         image: nginx:alpine
         ports:
            - 80:80
            - 443:443
         volumes:
            - ./conf:/etc/nginx/conf.d:ro      # dir para archivo configuración de nginx
            - ./web/static:/var/www/static     # para los archivos static
         depends_on:
            - web
      web:
         build: web
         restart: always
         command: gunicorn sitio_web.wsgi:application --bind 0.0.0.0:8000
         # command: python manage.py runserver 0.0.0.0:8000
         volumes:
           - ./web:/web
```

El archivo configuración de [nginx](https://www.nginx.com/): en  **./conf/default**

``` {.language-bash}
server {
   listen 80 default_server;

      # servidor web para archivos en  /static
      location /static/ {
            alias /var/www/static/;
      }

      # proxy inverso, se pasa a la aplicación wsgi
      location / {
           proxy_pass http://web:8000;
           proxy_set_header X-Forwarded-Host $server_name;
           proxy_set_header X-Real-IP $remote_addr;
      }
   }
```

La configuración de [supervisord](http://supervisord.org/) sería:   **gunicorn.ini**

``` {.language-bash}
[program:gunicorn]
command=/usr/local/bin/gunicorn sitio_web.wsgi:application  --bind 0.0.0.0:8000
directory=/web
user=root
autostart=true
autorestart=true
redirect_stderr=true
```

Este archivo debe estar en */etc/supervidor.d/*, por lo que el **Dockerfile** quedaría:

``` {.language-bash}
FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1

RUN apk add supervisor
# Creating working directory inside container
RUN mkdir /web
COPY . /web
COPY gunicorn.ini /etc/supervisor.d/

WORKDIR /web
RUN pip3 install -r requirements.txt
```

Algunos enlaces:

[Docker-compose Nginx + Django + Gunicorn](https://gist.github.com/emmettna/b78f54a6683b06a2a2da21db7580a8d6)

[Primeros pasos con Django](https://cloud.google.com/python/django/?hl=es) (google cloud)

[Docker + Django + Heroku sin morir en el intento](https://medium.com/@asinox/docker-django-heroku-sin-morir-en-el-intento-2486a2478ea7) (heroku)

[Implementación de una aplicación de Django en Elastic Beanstalk](https://docs.aws.amazon.com/es_es/elasticbeanstalk/latest/dg/create-deploy-python-django.html) (aws)


