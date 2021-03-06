from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from farmacia.forms import ProductoForm, UsuarioForm, LoginForm
from farmacia.models import Producto, Factura,Usuario
from django.contrib import messages
from django.core.mail import EmailMessage

logeo=0

def index(request):
    return render(request,'farmacia/index.html')

def productos(request):
    if request.method =='POST':
        form=ProductoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('productos_all')
    else:
        form=ProductoForm()
    return render(request, 'admin/producto_form.html', {'form':form})

def productos_all(request):
    if logeo!=0:
        usuario=Usuario.objects.get(username=logeo)
        if usuario.admin:
            producto=Producto.objects.all()
            contexto={'productos':producto}
            return render(request, 'admin/productos_list.html', contexto)
    return render(request, 'cliente/mensaje.html', {'mensaje': 'Error no haz iniciado sesion'})


def producto_cambiar(request, folio):
    producto=Producto.objects.get(folio=folio)
    if request.method=='GET':
        form=ProductoForm(instance=producto)
    else:
        form=ProductoForm(request.POST,instance=producto)
        form.folio=producto.folio
        form.nombre=producto.nombre
        form.descripcion=producto.descripcion
        form.clasificacion=producto.clasificacion
        print(form.errors)
        if form.is_valid():
            form.save()
        return redirect('productos_all')
    return render(request, 'admin/producto_form.html', {'form':form})

def producto_eliminar(request,folio):
    producto=Producto.objects.get(folio=folio)
    if request.method=='POST':
        producto.delete()
        return redirect('productos_all')
    return render(request, 'admin/producto_eliminar.html', {'producto':producto})

def factura(request):
    factura=Factura.objects.all()
    contexto={'productos':factura}
    return render(request, 'admin/historial.html', contexto)

def registro(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['username']
            if Usuario.objects.filter(username=nombre).exists():
                messages.add_message(request, messages.INFO, 'El nombre de usuario ya existe')
            else:
                form.save()
                return redirect('productos_all')
    else:
        form = UsuarioForm()
    return render(request, 'cliente/crearUsuario.html', {'form': form})


def sesion(request):
    global logeo
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            nombre=form.cleaned_data['username']
            if Usuario.objects.filter(username=nombre).exists():
                contra=form.cleaned_data['password']
                if Usuario.objects.filter(password=contra).exists():
                    logeo=nombre
                    return redirect('inicio')
                else:
                    messages.add_message(request, messages.INFO, 'Contraseña incorrecta')
            else:
                messages.add_message(request, messages.INFO, 'Usuario Incorrecto')
    else:
        form = LoginForm()
    return render(request, 'cliente/login.html', {'form': form})

def administrador(request):
    return HttpResponse("Administrador")

def contacto(request):
    return render(request,'farmacia/contacto.html')

def promocion(request):
    return render(request,'farmacia/promociones.html')