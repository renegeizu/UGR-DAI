#!/bin/bash

# Directorios

sitioWeb=web/sitio_web
aplicacion=web/aplicacion
backup=backup

# Construccion de la Aplicacion

sudo make build
sudo make django-startproject
sudo make django-startapp

# Creacion de Directorios

sudo mkdir $aplicacion/static
sudo mkdir web/static

sudo mv -f $backup/sitio_web-settings.py $sitioWeb/settings.py

# Migracion

sudo make django-migrate

# Superusuario

sudo make django-createsuperuser

sudo mv -f $backup/sitio_web-urls.py $sitioWeb/urls.py
sudo mv -f $backup/sitio_web-wsgi.py $sitioWeb/wsgi.py
sudo mv -f $backup/aplicacion-views.py $aplicacion/views.py
sudo mv -f $backup/aplicacion-urls.py $aplicacion/urls.py

sudo mv -f $backup/aplicacion-forms.py $aplicacion/forms.py
sudo mv -f $backup/aplicacion-models.py $aplicacion/models.py
sudo mv -f $backup/aplicacion-admin.py $aplicacion/admin.py

sudo mv $backup/app_templates/templates $aplicacion
sudo mv $backup/web_templates/templates web

sudo mv -f $backup/test.html $aplicacion/templates/test.html

# Eliminar Archivos Temporales

sudo rm -rfv $backup

# Agregar Modelo y Migrar

sudo docker-compose run web python manage.py makemigrations aplicacion
sudo make django-migrate
sudo docker-compose run web python manage.py collectstatic

# Cambiar Permisos

sudo chmod -R 777  ../Practica_09

# Lanzar Servidor

sudo make all
