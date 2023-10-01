## Trabajo Integrador

<details><summary>Enunciado </summary>

CIDEPINT es el Centro de Investigación y Desarrollo en Tecnología de Pinturas de Argentina, nacido en los años 70 a partir de una colaboración entre varias instituciones. Su objetivo principal es promover la competitividad de los productos de pintura argentinos a nivel nacional e internacional mediante investigaciones y desarrollos en tecnología de recubrimientos. Además, se dedica a la formación de profesionales especializados y a la creación de normas en la industria. Con el tiempo, ha ampliado sus áreas de enfoque para incluir temas como el tratamiento de aceros, la protección contra la corrosión y soluciones ecológicas. Sus objetivos incluyen investigar, formar recursos humanos, difundir resultados, organizar cursos y colaborar con instituciones afines.

CIDEPINT plantea la necesidad de que exista una plataforma para mostrar y ofrecer los servicios que prestan las diferentes Instituciones.

La aplicación tendrá un aplicación interna de administración (para usuarios y administradores) en Python y Flask, y un portal web en Vue.js que será donde se podrán buscar los servicios ofrecidos por las instituciones registradas. Utilizaremos una base de datos PostgreSQL y se implementarán las API necesarias para las consultas.

</details>

#### Objetivo general

El objetivo de este trabajo integrador es desarrollar una aplicación web que permita registrar y gestionar los servicios ofrecidos por las instituciones o centros de Investigación y Desarrollo en Tecnología de Pinturas. Estos centros contarán con un conjunto de características como nombre, descripción, contacto, página web, redes sociales y ubicación geográfica.

#### Funcionalidad de la aplicación

- **Implementar un buscador de servicios:** se debe proporcionar a los usuarios un buscador que les permita encontrar servicios ofrecidos por las distintas instituciones.
- Permitir a entidades/personas puedan **dar de alta su organización** y **publicar los servicios** que ofrecen.
- **Realizar un pedido de servicio:** los usuarios podrán solicitar un servicio, que puede incluir la reserva de un turno para utilizar algún equipamiento o simplemente dejar un mensaje para establecer el contacto.
- **Seguimiento del pedido**
- **Obtener reportes estadísticos:** la aplicación debe generar reportes estadísticos que muestren los servicios más requeridos, las zonas más demandadas y los turnos no cumplidos.

#### Componentes de la aplicacion 

- **Aplicación de administración en Python y Flask:** desarrollar una aplicación que permita la administración de altas, bajas y modificaciones de los recursos necesarios para el sistema. También se deberá implementar un registro de usuarios y un sistema de autenticación para operar con la aplicación.
- **Portal en Vue.js:** crear una interfaz de usuario interactiva que permita acceder al mapa con las ubicaciones de los centros, utilizar el buscador de servicios y realizar pedidos de servicio.
- **Base de datos PostgreSQL:** diseñar la estructura de la base de datos para almacenar la información de las instituciones, servicios y usuarios de la aplicación.
- API para consultas: implementar API que permitan realizar las consultas necesarias para obtener la información de los centros y servicios.

---


# Tareas para la Etapa 1

### Aplicación Privada

Esta aplicación será utilizada tanto por los administradores del sistema que tienen el acceso a la administración de los usuarios y también por usuarios asociados a cada una de las instituciones para que puedan administrar las mismas agregando los servicios que ofrecen.

- [Layout]()
- [Registro de usuarios]()
- [Login y manejo de sesiones]()
- [Módulo de usuarios]()
- [Módulo de administración de Instituciones]()
- [Módulo de administración de usuarios de la institución]()
- [Módulo de administración de servicios]()
- [Módulo de gestión de solicitud de servicio]()
- [Módulo de configuración]()
- [10 API]()


---

## Layout

Se deberá implementar el layout de la aplicación que es la base para todas las vistas de la aplicación privada. El resto de las vistas estarán contenidas en este layout sobreescribiendo el contenido central.

La aplicación deberá contar con un menú de navegación que tenga los enlaces a todos los módulos del sistema y esté visible en aquellas vistas del sistema que se consideren necesarias.

Se debe incluir una barra superior en la aplicación que nos permita acceder a las operaciones principales de nuestra aplicación, Ejemplo en Figura 1.

![Figura 1](https://lh4.googleusercontent.com/gKIAsess-THLR1HbDb5Prm7tfKhntp5YIeTmNdi8Uu-scBKqH2wF7XEFhf2M6z3W-0ABwo3Qf0-Hv1YyfCFzMg4jyg-6O4fLv9IX4PG-Zq7Nwe4xVQaJix_RyGOxoFAlTQhhySDc87SJxkJV-ULh3qw)

En la Figura 1 se pueden ver las siguiente opciones de derecha a izquierda:

- **Dropdown de usuario/cuenta**. Permite realizar operaciones sobre la cuenta de usuarios y la sesión.
- **Botón de acceso a los seguimientos**. En este ejemplo dejamos un indicador de los seguimientos que están en curso.
- Botón que nos permite **modificar la información de la institución** seleccionada actualmente.
- **Dropdown que nos permite cambiar de institución** (si es que el usuario pertenece a más de una)

> Aclaración: No es necesario seguir este boceto a la perfección. El objetivo del mismo es sólo mostrarles la funcionalidad que debería estar fácilmente disponible para el usuario en la barra superior, menú o submenú.

También pueden crear un logo para la aplicación y mostrar el mismo en forma coherente  en todas las secciones de la aplicación.

---

## Registro de usuarios

La aplicación de administración debe permitir el registro de 2 formas: un registro simple, que permite al usuario registrarse de la forma convenciona

#### Registro simple

Implementar las páginas necesarias para realizar el flujo de registro de usuario al sistema. El registro de usuario deberá ser público, permitiendo que cualquier persona pueda crear una cuenta.

Es necesario que estén registrados en el sistema tanto los usuarios que van utilizar la parte administrativa del sistema como los que realicen las solicitudes de servicios que se ofrecen en el sistema.

El formulario de registro debe solicitar los siguientes datos:

- Nombre
- Apellido
- Correo electrónico

Una vez cargados los datos en el formulario de registro, se enviará un correo de confirmación que el usuario deberá aceptar y será redirigido a la aplicación obligando a que complete usuario y contraseña para terminar el proceso.  El usuario no podrá realizar ninguna operación en la plataforma hasta tanto se le asigne el rol correspondiente que se lo permita.

---

## Login y manejo de sesiones

El sistema deberá contar con un **formulario de login** que permita a los usuarios iniciar sesión en el sistema. Además del inicio de sesión convencional (con correo electrónico y clave), deberá existir la opción de poder iniciar sesión con Google (se trabajará en la Etapa 2).

Deberá implementarse un manejo de sesiones adecuado, verificando la sesión y permisos cuando corresponda. Para cada módulo se indicará si requiere autenticación o no y los permisos necesarios.

Tener en cuenta que un usuario puede tener distintos roles en distintas instituciones.

Atención: No está permitido el uso de ninguna librería externa que simplifique el proceso de login (ejemplo: flask-login). Deberán realizar la implementación completa de esta funcionalidad sin el uso de librerías que podrían ocultar comportamiento importante que queremos que aprendan y fijen en esta materia.

---

## Módulo de usuarios

Desarrollar el **módulo de usuarios** que debe permitir al **Super Administrador** (no pertenece a ningúna institución) realizar distintas operaciones sobre los usuarios del sistema, ya sea personal administrativo o usuario común.

El módulo debe permitir el **CRUD** de usuarios. Deben validar que no existan  dos usuarios con el mismo nombre de usuario (mismo email).

Se considerarán al menos los siguientes datos para cada usuario:

- **Nombre**
- **Apellido**
- **Email**
- **Nombre de usuario**
- **Password**
- **Activo:** SI | NO
- **Roles por Institución:** Operador/a | Administrador/a

Se deben poder realizar búsquedas sobre los usuarios, **al menos** por los siguientes campos:

- Email
- Activo/Bloqueado

El resultado de la búsqueda debe estar paginado en base a la configuración del sistema (ver **módulo de configuración**). La paginación deberá realizarse del lado del servidor, es decir, la cantidad de registros retornados debe ser la indicada en el módulo de configuración, por ej. 25 registros por página.

Se debe desarrollar la funcionalidad para activar o bloquear un usuario: un usuario bloqueado no podrá acceder al sistema. Se deberá validar que los únicos usuarios que no puedan ser bloqueados, sean aquellos con el rol **Super Administrador**.

Además se debe poder asignar o desasignar roles de un usuario para una institución. En principio se proponen los roles **Dueño/a, Administrador/a y Operador/a** pero pueden agregarse más si se lo cree conveniente.

En referencia a los roles anteriormente mencionados podemos decir que Super Administrador es el rol con menos restricciones del sistema y que no pertenece a ningúna institución. En contrapunto los roles Dueño/a, Administrador/a y Operador/a son los roles que se pueden asignar a los usuarios que trabajan para las distintas instituciones.

Para el desarrollo del TI no será obligatorio desarrollar el CRUD de los roles y permisos, podrán administrarse desde la base de datos. Los usuarios, roles y permisos sólo podrán ser administrados por un usuario con rol de Super Administrador para esta sección.

Los permisos necesarios asociados a cada rol deberán deducirse del enunciado, ante la duda pueden consultar a su ayudante.

El nombre de los permisos deberá respetar el patrón modulo_accion, por ejemplo, el módulo de gestión de usuarios deberá contemplar los siguientes permisos:

- **user_index:** permite acceder al index (listado) del módulo.
- **user_new:** permite crear un usuario.
- **user_destroy:** permite eliminar un usuario.
- **user_update:** permite actualizar los datos de un usuario.
- **user_show:** permite visualizar la información de un usuario.

> Nota: Es importante entender el porqué del uso de esta solución para implementar la autorización y seguir el esquema de forma correcta. Este tema será explicado oportunamente en los horarios de práctica. 

La Figura 2 muestra un posible modelo de usuarios, roles y permisos, que pueden utilizar en el trabajo.

<img alt="" src="https://lh3.googleusercontent.com/heDavtgGAijj4mrPJg3l_HSanOSRNTz_I9oUooG0wVZCDtMplDipXGWwxFLbCsQP2gXyGzFx4RnYuZMdM0M6bUm_uAs2XM2VqtE7cF2oMYPll5EwzqhdjghnHZcRqI7LH3CnNCRgKeXX1vLe0dQs7g8" >