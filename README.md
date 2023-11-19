# Proyecto Django

Es un proyecto web desarrollado en Django que se encarga de gestionar usuarios, clientes y productos. El proyecto incluye un buscador de productos y clientes.
La app principal es proyectonumero1, y luego cuenta con dos aplicaciones mas inicio y accounts.
Inicio, gestiona clientes y productos.
Accounts gestiona login, logout , cambios de contraseña, edicion de usuarios.


### Cliente

El modelo de Cliente representa a los clientes de la empresa. Contiene campos como nombre, dirección, teléfono y correo electrónico. Los clientes se pueden registrar en el sistema a través de un formulario y los lleva a una confirmacion si se registraron exitosamente.

### Producto

El modelo de Producto se utiliza para cargar los mismos en la base de  datos, contiene detalles sobre cada producto, como nombre, descripción ,precio , stock e imagen. 

## Buscador de Producto

Se incluye un buscador de productos que permite a los usuarios buscar productos por nombre. Los resultados de la búsqueda se muestran en una lista, lo que facilita a los usuarios encontrar los productos que necesitan, en caso de no encontrarse lo menciona con un mensaje.

## Accounts
En esta seccion, se gestiona el login de las personas, si estas estan logueadas, se habilita para realizar algunas acciones , tambien se puede modificar la contraseña, y tiene un perfil de usuarios.


## Requisitos

asgiref==3.7.2
Django==4.2.6
sqlparse==0.4.4
tzdata==2023.3

¡Gracias ! Luciana
