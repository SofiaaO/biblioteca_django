from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *

# Create your views here.
def inicio(request):
    return render (request, 'inicio.html')

def lista_autores(request):
    autores = Autor.objects.all()  
    for i in autores:
        print(i) 
    return render(request, 'autores/listado_autores', {'autores': autores})

def crear_autores(request):
    if request.method=='POST':
        form=AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_autores")
    else:
        form = AutorForm()
    return render(request, 'autores/crear_autores.html', {'form':form})


def modificar_autores(request, pk):
    try:
        autor = Autor.objects.get(pk=pk)
    except Autor.DoesNotExist:
        return redirect('404')

    if request.method == "POST":
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('lista_autores')
    else:
        form = AutorForm(instance=autor)

    return render(request, 'autores/modificar_autores.html', {'form': form})


def eliminar_autores(request,pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == "POST":
        autor.delete()
        return redirect('lista_autores')
    return render(request, 'autores/eliminar_autores.html', {'autor': autor})
    
def lista_libros(request):
    libros = Libro.objects.all()
    for i in libros:
        print(i)
        return render (request, 'libros/listado_libros', {
            'libros': libros
        })
def crear_libros(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_libros")  # Ajusta esto al nombre de tu URL
    else:
        form = LibroForm()

    # Obtener autores para pasarlos al contexto del template
    autores = Autor.objects.all()
    return render(request, 'libros/crear_libros.html', {'form': form, 'autores': autores})

def modificar_libros(request, pk):
    try:
        libro = Libro.objects.get(pk=pk)
    except Libro.DoesNotExist:
        return redirect('404')

    # Obtener todos los autores para pasarlos al contexto
    autores = Autor.objects.all()

    if request.method == "POST":
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm(instance=libro)

    return render(request, 'libros/modificar_libros.html', {'form': form, 'autores': autores})


def eliminar_libros(request,pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == "POST":
        libro.delete()
        return redirect('lista_libros')
    return render(request, 'libros/eliminar_libros.html', {'libro': libro})
    