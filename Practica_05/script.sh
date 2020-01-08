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

sudo mkdir $aplicacion/templates
sudo mkdir $aplicacion/static

sudo mv -f $backup/sitio_web-settings.py $sitioWeb/settings.py

# Migracion

sudo make django-migrate

# Superusuario

sudo make django-createsuperuser

sudo mv -f $backup/sitio_web-urls.py $sitioWeb/urls.py
sudo mv -f $backup/aplicacion-views.py $aplicacion/views.py
sudo mv -f $backup/aplicacion-urls.py $aplicacion/urls.py
sudo mv -f $backup/test.html $aplicacion/templates/test.html

# Cambiar Permisos

sudo chmod -R 777  ../Practica_05

# Eliminar Archivos Temporales

sudo rm -rfv $backup

# Lanzar Servidor

sudo make all
