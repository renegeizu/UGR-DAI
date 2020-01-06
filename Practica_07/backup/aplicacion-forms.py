from django import forms

from .models import Musico, Grupo, Album

class MusicoForm(forms.ModelForm):
    class Meta:
        model = Musico
        fields = ('nombre', 'apellidos', 'fecha_nacimiento', 'instrumento',)

class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = ('nombre', 'fecha_fundacion', 'estilo_musical', 'componentes',)

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('titulo', 'distribuidora', 'fecha_lanzamiento', 'grupo',)