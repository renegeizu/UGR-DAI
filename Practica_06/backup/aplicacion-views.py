from django.shortcuts import render, HttpResponse, redirect

from .forms import MusicoForm, GrupoForm, AlbumForm

from .models import Musico, Grupo, Album

def index(request):
    return render(request, "index.html", {})

def musicos(request):
    musicos = Musico.objects.all()
    return render(request, "musico/list.html", {'musicos': musicos})

def grupos(request):
    grupos = Grupo.objects.all()
    return render(request, "grupo/list.html", {'grupos': grupos})

def albums(request):
    albums = Album.objects.all()
    return render(request, "album/list.html", {'albums': albums})

def test_template(request):
    context = {}
    return render(request,'test.html', context)

def add_musico(request):
    form = MusicoForm()
    if request.method == "POST":
        form = MusicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/aplicacion/musicos')
    return render(request, "musico/add.html", {'form': form})

def add_grupo(request):
    form = GrupoForm()
    if request.method == "POST":
        form = GrupoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/aplicacion/grupos')
    return render(request, "grupo/add.html", {'form': form})

def add_album(request):
    form = AlbumForm()
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/aplicacion/albums')
    return render(request, "album/add.html", {'form': form})

def update_musico(request, pk):
    instancia = Musico.objects.get(id=pk)
    form = MusicoForm(instance=instancia)
    if request.method == "POST":
        form = MusicoForm(request.POST, instance=instancia)
        if form.is_valid():
            form.save()
    return render(request, "musico/update.html", {'form': form})

def update_grupo(request, pk):
    instancia = Grupo.objects.get(id=pk)
    form = GrupoForm(instance=instancia)
    if request.method == "POST":
        form = GrupoForm(request.POST, instance=instancia)
        if form.is_valid():
            form.save()
    return render(request, "grupo/update.html", {'form': form})

def update_album(request, pk):
    instancia = Album.objects.get(id=pk)
    form = AlbumForm(instance=instancia)
    if request.method == "POST":
        form = AlbumForm(request.POST, instance=instancia)
        if form.is_valid():
            form.save()
    return render(request, "album/update.html", {'form': form})

def delete_musico(request, pk):
    instancia = Musico.objects.get(id=pk)
    instancia.delete()
    return redirect('/aplicaciones/musicos')

def delete_grupo(request, pk):
    instancia = Grupo.objects.get(id=pk)
    instancia.delete()
    return redirect('/aplicaciones/grupos')

def delete_album(request, pk):
    instancia = Album.objects.get(id=pk)
    instancia.delete()
    return redirect('/aplicaciones/albums')