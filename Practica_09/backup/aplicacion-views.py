from django.shortcuts import render, HttpResponse, redirect

from .forms import MusicoForm, GrupoForm, AlbumForm

from .models import Musico, Grupo, Album

def index(request):
    return render(request, "index.html", {})

def musicos(request):
    if request.user.is_authenticated:
        musicos = Musico.objects.all()
        return render(request, "musico/list.html", {'musicos': musicos})
    else:
        return redirect('/accounts/login')

def grupos(request):
    if request.user.is_authenticated:
        grupos = Grupo.objects.all()
        return render(request, "grupo/list.html", {'grupos': grupos})
    else:
        return redirect('/accounts/login')

def albums(request):
    if request.user.is_authenticated:
        albums = Album.objects.all()
        return render(request, "album/list.html", {'albums': albums})
    else:
        return redirect('/accounts/login')

def test_template(request):
    context = {}
    return render(request,'test.html', context)

def add_musico(request):
    if request.user.is_authenticated:
        form = MusicoForm()
        if request.method == "POST":
            form = MusicoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/aplicacion/musicos')
        return render(request, "musico/add.html", {'form': form})
    else:
        return redirect('/accounts/login')

def add_grupo(request):
    if request.user.is_authenticated:
        form = GrupoForm()
        if request.method == "POST":
            form = GrupoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/aplicacion/grupos')
        return render(request, "grupo/add.html", {'form': form})
    else:
        return redirect('/accounts/login')

def add_album(request):
    if request.user.is_authenticated:
        form = AlbumForm()
        if request.method == "POST":
            form = AlbumForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/aplicacion/albums')
        return render(request, "album/add.html", {'form': form})
    else:
        return redirect('/accounts/login')

def update_musico(request, pk):
    if request.user.is_authenticated:
        instancia = Musico.objects.get(id=pk)
        form = MusicoForm(instance=instancia)
        if request.method == "POST":
            form = MusicoForm(request.POST, instance=instancia)
            if form.is_valid():
                form.save()
                return redirect('/aplicacion/musicos')
        return render(request, "musico/update.html", {'form': form})
    else:
        return redirect('/accounts/login')

def update_grupo(request, pk):
    if request.user.is_authenticated:
        instancia = Grupo.objects.get(id=pk)
        form = GrupoForm(instance=instancia)
        if request.method == "POST":
            form = GrupoForm(request.POST, instance=instancia)
            if form.is_valid():
                form.save()
                return redirect('/aplicacion/grupos')
        return render(request, "grupo/update.html", {'form': form})
    else:
        return redirect('/accounts/login')

def update_album(request, pk):
    if request.user.is_authenticated:
        instancia = Album.objects.get(id=pk)
        form = AlbumForm(instance=instancia)
        if request.method == "POST":
            form = AlbumForm(request.POST, instance=instancia)
            if form.is_valid():
                form.save()
                return redirect('/aplicacion/albums')
        return render(request, "album/update.html", {'form': form})
    else:
        return redirect('/accounts/login')

def delete_musico(request, pk):
    if request.user.is_authenticated:
        instancia = Musico.objects.get(id=pk)
        instancia.delete()
        return redirect('/aplicaciones/musicos')
    else:
        return redirect('/accounts/login')

def delete_grupo(request, pk):
    if request.user.is_authenticated:
        instancia = Grupo.objects.get(id=pk)
        instancia.delete()
        return redirect('/aplicaciones/grupos')
    else:
        return redirect('/accounts/login')

def delete_album(request, pk):
    if request.user.is_authenticated:
        instancia = Album.objects.get(id=pk)
        instancia.delete()
        return redirect('/aplicaciones/albums')
    else:
        return redirect('/accounts/login')