from django.contrib import admin

from .models import Musico, Grupo, Album

admin.site.register(Musico)
admin.site.register(Grupo)
admin.site.register(Album)