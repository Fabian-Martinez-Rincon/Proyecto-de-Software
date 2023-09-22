

<div align="center"> 

<img src='https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat'>
<img src='https://img.shields.io/github/stars/Fabian-Martinez-Rincon/Proyecto-de-Software'><img src='https://img.shields.io/github/repo-size/Fabian-Martinez-Rincon/Proyecto-de-Software'>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=30&duration=1200&pause=1000&color=F78E23&center=true&width=435&lines=Proyecto-de-Software"/></div>

---




- [All The Tags](https://allthetags.com/)
- [Web Primera Entrega](https://fabian-martinez-rincon.github.io/Proyecto-de-Software/ACT1-TEORIA/index.html)
- [Enunciado Primera Entrega](/Documentos/enunciado1raEntrega.md)
- [Autoevaluacion de Conceptos Basicos](/practica/Actividad%201%20-%20Conceptos%20generales%20Git.pdf)
- Vamos a usar python 3.8.10



---

### Clase 0 Presentacion + Python

En la primera parte explicamos la modalidad de la materia en general.
Las fechas de las entregas practicas serian las siguientes

- Entrega Parte 1: 20/10

En la segunda parte de la clase vimos un poco de python y hicimos una calculadora basica



- **1)** **Marca de Paquete:** \
   El archivo `__init__.py` en un directorio es una marca que indica que el directorio debe tratarse como un paquete de Python. Sin este archivo, el directorio no se considerará un paquete y no se podrán importar sus módulos desde otros lugares del código.
- **2)** **Inicialización de Paquete:** \
   Puedes colocar código de inicialización en el archivo `__init__.py`. Esto puede incluir importaciones de módulos, definición de variables o cualquier otra inicialización necesaria para el paquete.
- **3)** **Contenido Opcional:**\
   El archivo `__init__.py` puede estar vacío si no es necesario realizar ninguna inicialización específica para el paquete. A menudo, este archivo está presente simplemente para marcar el directorio como un paquete.
- **4)** **Importaciones Automáticas:**\
   Si defines importaciones en el archivo `__init__.py`, esas importaciones se ejecutarán automáticamente cada vez que importes el paquete. Esto puede ser útil para organizar y centralizar las importaciones en un solo lugar.

Hicimos una calculadora media pedorra pero tuve algunos incovenientes con python porque  no me acordaba mucho xd


> **Nota:** \Esto no lo podemos usar si estamos en el main
```python
import operations
```

Por lo que tenemos que hacer

> **Nota:** \Esto no lo podemos usar si estamos en el main 
```python
from src import operations
```


[Codigo Practica 1](/practica/explicacionPracticaUno/)

---


### Clase 1 Git

[Vemos la actividad 1](/practica/Actividad%201%20-%20Conceptos%20generales%20Git.pdf)

El profe empieza a explicar la practica del pdf asi por encima

- **Clave SSH**: (Secure Shell) es una forma de autenticación segura que se utiliza para establecer conexiones seguras entre dispositivos en una red, como por ejemplo, entre tu computadora y un servidor remoto. Se utiliza principalmente para autenticarse en servidores remotos de forma segura y cifrada.

Hablamos de la rama origin, hacemos referencia al repositorio remoto

```shell
git remote -v
```

Tambien usamos el comando

```shell
git push origin main
```

El comando `git push origin main` es un comando de Git que permite enviar los cambios realizados en el repositorio local al repositorio remoto.

En este comando, `origin` se refiere al repositorio remoto donde se están enviando los cambios, y `main` se refiere a la rama del repositorio local que se está enviando al repositorio remoto.

Ahora si queremos crear una rama podemos hacer git branch y el nombre de la rama

```shell
git branch nombreRama
```

y para subir los cambios 

```shell
git push origin nombreRama
```


Tambien usamos el git rebase


> Parece que ya no vemos nada importante, solo vemos como el profe va creando y fucionando las ramas, lo que si, podemos tener conflictos(o por lo menos yo) a la hora de hacer un pull en una rama que no es la main, por lo que tenemos que hacer un git pull origin main y despues un git push origin nombreRama



---

### Clase 2 Aplicacion Base + Deploy

Vamos a levantar la aplicacion base para despues continuar con el trabajo integrador

- [Enunciado de la actividad 2](/Otros/Actividad%202%20-%20Aplicación%20base.pdf)


***Explicamos la infra***

Cada uno trabaja en su rama, y despues hace un merge a main, y con esto, se ejecuta el 'ci' que es un script que nos permite hacer integracion continua.

Con este script de CI, cada vez que hagas un push en la rama principal, GitHub Actions construirá tu aplicación, instalará las dependencias, ejecutará las pruebas y te notificará si hay algún error. Asegúrate de ajustar las versiones y configuraciones según tu proyecto.


> Como vamos a usar python 3.8.10, tenemos que instalarlo con pyenv para no tener problemas

```shell
pyenv install 3.8.10  # Instala Python 3.8.10 (por ejemplo)
```


---

### Clase 3 MVC + BluePrints

---

### Clase 4 Database + Configs + ORM