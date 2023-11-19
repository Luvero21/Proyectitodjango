from django.shortcuts import render, get_object_or_404, redirect, reverse

from inicio.models import Producto, Cliente, Usuario

from inicio.forms import ActualizarProductoFormulario, actualizarUsuarioFormulario, UsuarioForm, ClienteForm, actualizarClienteFormulario

from inicio.formulaire import formulaireProducto

from django.contrib.auth.decorators import login_required


def inicio(request):
    
    return render(request,'inicio.html',{})

def nosotros(request):
    return render(request, 'nosotros.html')

#Vista para crear un cliente
def formulario_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('confirmacion_registro')
    form= ClienteForm()

    return render(request, 'formulario_cliente.html',{'form':form})

#Vista para eliminar un cliente
@login_required
def eliminar_cliente(request,cliente_id):
    cliente_a_eliminar= Cliente.objects.get(id=cliente_id)
    cliente_a_eliminar.delete()
    
    return redirect('lista_clientes')

@login_required
def actualizar_cliente(request,cliente_id):
    cliente_a_actualizar = Cliente.objects.get(id=cliente_id)
    
    if request.method == 'POST':
        formulario=actualizarClienteFormulario(request.POST)
        if formulario.is_valid():
            info_nueva = formulario.cleaned_data
            
            cliente_a_actualizar.nombre = info_nueva.get('nombre')
            cliente_a_actualizar.direccion = info_nueva.get('direccion')
            cliente_a_actualizar.telefono = info_nueva.get('telefono')
            cliente_a_actualizar.email = info_nueva.get('email')
            
            cliente_a_actualizar.save()
            return redirect('lista_clientes')
        else:
            return render(request, 'actualizar_cliente.html', {'formulario':formulario})
    
    formulario = actualizarClienteFormulario()
    return render (request, 'actualizar_cliente.html',{'formulario':formulario} )
    
   
#Vista Crear Producto
@login_required
def crearProducto(request):
    if request.method =='POST':
        formulaire=formulaireProducto(request.POST)
        if formulaire.is_valid():
            info_clean= formulaire.cleaned_data
            
            nombre= info_clean.get('nombre')
            descripcion= info_clean.get('descripcion')
            precio= info_clean.get('precio')
            stock=info_clean.get('stock')
            imagen=info_clean.get('imagen')
            
            producto=Producto(nombre=nombre,descripcion=descripcion,precio=precio,stock=stock,imagen=imagen)
            producto.save()
            
            return redirect('lista_productos')
        else:
            return render(request,'crear_producto.html',{'formulaire':formulaire})
            
    formulaire=formulaireProducto()
    return render(request,'crear_producto.html',{'formulaire':formulaire})

#Vista para eliminar un producto
@login_required
def eliminar_producto (request, producto_id):
    producto_a_eliminar=Producto.objects.get(id=producto_id)
    producto_a_eliminar.delete()
    
    return redirect('lista_productos')

@login_required
def actualizar_producto(request,producto_id):
    producto_a_actualizar= Producto.objects.get(id=producto_id)
    
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        formulario=ActualizarProductoFormulario(request.POST,request.FILES, instance=producto_a_actualizar)
        if formulario.is_valid():
           formulario.save()
           return redirect('lista_productos')
        else:
           print(formulario.errors)
           return render(request, 'actualizar_producto.html', {'formulario': formulario, 'producto': producto_a_actualizar})
    else:
        formulario= ActualizarProductoFormulario(instance=producto_a_actualizar)
        return render ( request, 'actualizar_producto.html',{'formulario':formulario,'producto': producto_a_actualizar})


def formulario_usuario(request):
    mensaje=''
    context={}
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            mensaje='¡Gracias por registrarse!'
           

    context['form'] = UsuarioForm()
    context['mensaje']=mensaje
    
    return render(request,'formulario_usuario.html', context)

@login_required
def eliminar_usuario(request, usuario_id):
    usuario_a_eliminar= Usuario.objects.get(id=usuario_id)
    usuario_a_eliminar.delete()
    return redirect('lista_usuarios')

@login_required
def actualizar_usuario(request, usuario_id):
    usuario_a_actualizar = Usuario.objects.get(id = usuario_id)
    
    if request.method == 'POST':
        formulario=actualizarUsuarioFormulario(request.POST)
        if formulario.is_valid():
            info_nueva=formulario.cleaned_data
            
            usuario_a_actualizar.nombre_usuario = info_nueva.get('nombre_usuario')
            usuario_a_actualizar.nombre = info_nueva.get('nombre')
            usuario_a_actualizar.email = info_nueva.get('email')
            usuario_a_actualizar.edad = info_nueva.get('edad')
            usuario_a_actualizar.password = info_nueva.get('password')
            
            usuario_a_actualizar.save()
            return redirect('lista_usuarios')
        else:
            return render(request, 'actualizar_usuario.html', {'formulario': formulario})
    formulario= actualizarUsuarioFormulario()
    return render ( request, 'actualizar_usuario.html',{'formulario':formulario})      

@login_required
def detalle_usuario(request,usuario_id):
    usuario=get_object_or_404(Usuario,id=usuario_id,)
    return render(request, 'detalle_usuario.html',{'usuario':usuario})

@login_required
def lista_usuario(request):
    usuario_a_buscar = request.GET.get('nombre_usuario')
    if usuario_a_buscar:
        usuarios= Usuario.objects.filter(nombre_usuario=usuario_a_buscar)
    else:
        usuarios=Usuario.objects.all()
        
    return render(request, 'lista_usuarios.html', {'usuarios': usuarios})



def confirmacion_registro(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('confirmacion_registro')
    else:
        form = ClienteForm()
    ultimos_clientes = Cliente.objects.order_by('-id')[:1]

    return render(request, 'confirmacion_registro.html', {'ultimos_clientes': ultimos_clientes, 'form': form})


def lista_productos(request):
    nombre_a_buscar=request.GET.get('nombre')
    if nombre_a_buscar:
        productos = Producto.objects.filter(nombre=nombre_a_buscar)
    else:
        productos = Producto.objects.all()
    
    return render(request, 'lista_productos.html', {'productos': productos})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'detalle_producto.html', {'producto': producto})


@login_required
def lista_clientes(request):
    cliente_a_buscar = request.GET.get('nombre')
    if cliente_a_buscar:
        clientes= Cliente.objects.filter(nombre=cliente_a_buscar)
    else:
        clientes=Cliente.objects.all()
        
    return render(request, 'lista_clientes.html', {'clientes': clientes})

@login_required
def detalle_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, 'detalle_cliente.html', {'cliente': cliente})

@login_required
def agregarcliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()

    return render(request, 'agregar_cliente.html', {'form': form})




    
    
            

    








