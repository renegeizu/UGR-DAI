from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.core import serializers

from .forms import MusicoForm, GrupoForm, AlbumForm

from .models import Musico, Grupo, Album

def index(request):
    return render(request, "index.html", {})

def musicos(request):
    if request.user.is_authenticated:
        musicos = Musico.objects.all()[:5]
        return render(request, "musico/list.html", {'musicos': musicos})
    else:
        return redirect('/accounts/login')

@csrf_exempt
def info_musicos(request):
    page = request.POST.get('page')
    musicos = Musico.objects.all()
    results_per_page = 5
    paginator = Paginator(musicos, results_per_page)
    try:
        musicos = paginator.page(page)
        page = int(page) + 1
    except PageNotAnInteger:
        page = 2
        musicos = paginator.page(1)
    except EmptyPage:
        page = paginator.num_pages
        musicos = paginator.page(pages)
    musicos_html = loader.render_to_string('musico/tabla.html', {'musicos': musicos})
    output_data = {
        'musicos_html': musicos_html,
        'has_next': musicos.has_next(),
        'has_prev': musicos.has_previous(),
        'num_page': page
    }
    return JsonResponse(output_data, safe=False)

def grupos(request):
    if request.user.is_authenticated:
        grupos = Grupo.objects.all()[:5]
        return render(request, "grupo/list.html", {'grupos': grupos})
    else:
        return redirect('/accounts/login')

@csrf_exempt
def info_grupos(request):
    page = request.POST.get('page')
    grupos = Grupo.objects.all()
    results_per_page = 5
    paginator = Paginator(grupos, results_per_page)
    try:
        grupos = paginator.page(page)
        page = int(page) + 1
    except PageNotAnInteger:
        page = 2
        grupos = paginator.page(1)
    except EmptyPage:
        page = paginator.num_pages
        grupos = paginator.page(pages)
    grupos_html = loader.render_to_string('grupo/tabla.html', {'grupos': grupos})
    output_data = {
        'grupos_html': grupos_html,
        'has_next': grupos.has_next(),
        'has_prev': grupos.has_previous(),
        'num_page': page
    }
    return JsonResponse(output_data, safe=False)

def albums(request):
    if request.user.is_authenticated:
        albums = Album.objects.all()[:5]
        return render(request, "album/list.html", {'albums': albums})
    else:
        return redirect('/accounts/login')

@csrf_exempt
def info_albums(request):
    page = request.POST.get('page')
    albums = Album.objects.all()
    results_per_page = 5
    paginator = Paginator(albums, results_per_page)
    try:
        albums = paginator.page(page)
        page = int(page) + 1
    except PageNotAnInteger:
        page = 2
        albums = paginator.page(1)
    except EmptyPage:
        page = paginator.num_pages
        albums = paginator.page(pages)
    albums_html = loader.render_to_string('album/tabla.html', {'albums': albums})
    output_data = {
        'albums_html': albums_html,
        'has_next': albums.has_next(),
        'has_prev': albums.has_previous(),
        'num_page': page
    }
    return JsonResponse(output_data, safe=False)

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

def detail_musico(request, pk):
    if request.user.is_authenticated:
        grupos = Grupo.objects.get(id=pk)
        localizations = serializers.serialize('json', list(grupos.componentes.all()))
        return render(request, "musico/detail.html", {'grupos': grupos, 'localizations': localizations})
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
                return redirect("/aplicacion/grupos")
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
                return redirect("/aplicacion/albums")
        return render(request, "album/update.html", {'form': form})
    else:
        return redirect('/accounts/login')

def delete_musico(request, pk):
    if request.user.is_authenticated:
        instancia = Musico.objects.get(id=pk)
        instancia.delete()
        return redirect('/aplicacion/musicos')
    else:
        return redirect('/accounts/login')

def delete_grupo(request, pk):
    if request.user.is_authenticated:
        instancia = Grupo.objects.get(id=pk)
        instancia.delete()
        return redirect('/aplicacion/grupos')
    else:
        return redirect('/accounts/login')

def delete_album(request, pk):
    if request.user.is_authenticated:
        instancia = Album.objects.get(id=pk)
        instancia.delete()
        return redirect('/aplicacion/albums')
    else:
        return redirect('/accounts/login')
