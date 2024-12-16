from django.shortcuts import render,redirect
from ArtistaApp.models import Artista,Musica,   Album
from ArtistaApp.forms import FormArtista,FormMusica,FormAlbum

def index(request):
    return render(request,'ArtistaApp/index.html')

def listaAlbum(request):
    albumes = Album.objects.all()
    data = {'albumes': albumes}
    return render(request, 'ArtistaApp/listaAlbum.html', data)
def registrarAlbum(request):
    form2 = FormAlbum()
    if request.method == 'POST':
        form2 = FormAlbum(request.POST)
        if form2.is_valid():
            form2.save()
            return redirect('../')
        else:
            data = {'form2':form2}
            return render(request,'ArtistaApp/agregaAlbum.html',data)
    else:
        data = {'form2':form2}
        return render(request,'ArtistaApp/agregaAlbum.html',data)
    
def actualizaAlbum(request,id):
    albumes = Album.objects.get(id = id)
    form2 = FormAlbum(instance=albumes)
    if request.method == 'POST':
        form2 = FormAlbum(request.POST,instance=albumes)
        if form2.is_valid():
            form2.save()
        return index(request)
    data = {'form2' : form2}
    return render(request,'ArtistaApp/agregaAlbum.html',data)

def eliminarAlbum(request,id):
    albumes = Album.objects.get(id = id)
    albumes.delete()
    return redirect('../lista3')

def lista(request):
    artistas = Artista.objects.all()
    data = {'artistas' : artistas}
    return render(request,'ArtistaApp/lista.html',data)

def registrarArtista(request):
    form = FormArtista()
    if request.method == 'POST':
        form = FormArtista(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../')
        else:
            data = {'form': form}
            return render(request, 'ArtistaApp/registrar.html', data)
    else:
        data = {'form': form}
        return render(request, 'ArtistaApp/registrar.html', data)

def actualizarArtista(request,id):
    artistas = Artista.objects.get(id = id)
    form = FormArtista (instance=artistas)
    if request.method == 'POST':
        form = FormArtista(request.POST , instance=artistas)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form':form}
    return render(request,'ArtistaApp/registrar.html',data)


def eliminarArtista(request,id):
    artistas = Artista.objects.get(id = id)
    artistas.delete()
    return redirect('../lista')


def listaMusica(request):
    musicas = Musica.objects.all() 
    data = {'musicas': musicas} 
    return render(request, 'ArtistaApp/Musicalista.html', data)

def registrarMusica(request):
    form1 = FormMusica()
    if request.method == 'POST':
        form1 = FormMusica(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('../')
        else:
            data = {'form1' : form1}
            return render(request,'ArtistaApp/registraMusica.html',data)
    else:
        data = {'form1' : form1}
        return render(request,'ArtistaApp/registraMusica.html',data)
    
def actualizarMusica(request,id):
    musica = Musica.objects.get(id = id)
    form1 = FormMusica (instance=musica)
    if request.method == 'POST':
        form1 = FormMusica(request.POST , instance=musica)
        if form1.is_valid():
            form1.save()
        return index(request)
    data = {'form1' : form1}
    return render(request,'ArtistaApp/registraMusica.html',data)

def eliminaMusica(request,id):
    musica = Musica.objects.get(id = id)
    musica.delete()
    return redirect('../lista2')

        
# Create your views here.
