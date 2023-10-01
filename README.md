

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

Creamos el entorno virtual

El comando `pyenv virtualenv 3.8.10 myenv` que ejecutaste ha creado un entorno virtual de Python llamado "myenv" basado en la versión 3.8.10 de Python. Te proporcionaré algunos detalles adicionales sobre lo que hiciste y cómo puedes activar y desactivar este entorno virtual.

1. **Creación del Entorno Virtual:**
   - `pyenv virtualenv 3.8.10 myenv` crea un entorno virtual llamado "myenv" basado en la versión de Python 3.8.10.

2. **Activación del Entorno Virtual:**
   - Para activar este entorno virtual y utilizarlo, puedes usar el siguiente comando:
     ```bash
     pyenv activate myenv
     ```
   - Esto te cambiará al entorno virtual "myenv" y usarás la versión de Python 3.8.10 asociada a este entorno.

3. **Desactivación del Entorno Virtual:**
   - Para salir del entorno virtual y volver al entorno global, puedes usar:
     ```bash
     pyenv deactivate
     ```

4. **Eliminación del Entorno Virtual:**
   - Si deseas eliminar el entorno virtual "myenv", puedes usar el siguiente comando:
     ```bash
     pyenv virtualenv-delete myenv
     ```

Recuerda que, dentro de un entorno virtual, puedes instalar paquetes y dependencias específicos de ese proyecto sin afectar al entorno global de Python. Esto es útil para mantener la separación y la organización entre diferentes proyectos y sus dependencias.


***Explicamos la infra***

Cada uno trabaja en su rama, y despues hace un merge a main, y con esto, se ejecuta el 'ci' que es un script que nos permite hacer integracion continua.

Con este script de CI, cada vez que hagas un push en la rama principal, GitHub Actions construirá tu aplicación, instalará las dependencias, ejecutará las pruebas y te notificará si hay algún error. Asegúrate de ajustar las versiones y configuraciones según tu proyecto.


> Como vamos a usar python 3.8.10, tenemos que instalarlo con pyenv para no tener problemas

```shell
pyenv install 3.8.10  # Instala Python 3.8.10 (por ejemplo)
```

```
pyenv local myenv
```

Bien, una vez que tenemos nuestra aplicación base, vamos a hacer un deploy en Heroku

---

##### Explicacion

```
poetry new --name web --src admin
```

Agregamos el [.gitignore](https://github.com/github/gitignore/blob/main/Python.gitignore)


```
❯ poetry --version
Poetry version 1.1.12
```

myenv seria el nombre del entorno virtual con la version de python que queremos usar


```
pyenv local myenv
```

```
poetry add flask@latest
```

```
poetry add --dev pytest@latest
```

Si abrimos el pyproject.toml, podemos ver que tenemos las dependencias que instalamos. En la seccion

[tool.poetry.dev-dependencies]
pytest = "^7.4.2"

tenemos las dependencias de desarrollo

Como el trabajo es grupal, podemos clonar el repo y hacer

```
poetry install
```

Podemos cambiar la version de python de nuestro entorno con

```
poetry env use 3.8.10
```
Antes de esto tenia la 3.10

Y hacemos un, Para actualizar todo

```
poetry install
```

Usamos el siguiente comando para activar el entorno virtual

```
poetry shell
```

Para ver las versiones instaladas

```
flask --version
Python 3.8.10
Flask 2.3.3
Werkzeug 2.3.7
```
Esto me lo detecto porque tengo flask instalado en mi entorno virtual

Si quiero ejecutar estos comandos sin la necesidad de usar el poetry shell, puedo hacer

```
poetry run flask --version
```

Una vez que tenemos todo instalado, hacemos nuestra pequeña app en el directorio src/web en el archivo __init__.py

```python
from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.get('/')
    def home():
        return 'Hello, World!'
    
    return app
```

Y despues creamos un entrypoint en el directorio src/admin en el archivo app.py

> En el contexto de Python y las aplicaciones que se distribuyen usando herramientas como setuptools o Poetry, un "entry point" (punto de entrada) se refiere a un punto específico en tu código donde la ejecución de tu programa comienza.

```python
from src.web import create_app

app = create_app()

if __name__ == '__main__':
    app.run()
```

Una vez que tenemos nuestra app, podemos ejecutar 

```
flask run
```

Y me tira la ip http://127.0.0.1:5000/

El decorador

```python
@app.get('/')
```

Encierra una funcion que se ejecuta cuando se hace un get a la ruta `/`

Podemos ejecutar el modo debug para no tener que actualizar el servidor cada vez que hacemos un cambio

```
flask run --debuug
```

Ya que tenemos el pytest instalado, vamos a hacer un mini test en la carpeta tests

```python
from web import create_app

app = create_app()

app.testing = True

cliente = app.test_client()

def test_home():
    response = cliente.get('/')
    assert response.status_code == 200
    assert "Hello, World!" in response.data.decode('utf-8')
```

Este test lo podemos ejecutar con

```
pytest
```

Una vez que tenemos los test, creamos una carpeta dentro de /src/web llamada template que pondremos los archivos `html` y tambien creamos la carpeta `static` en el /src/ para los archivos estaticos que en este caso son los archivos `css` para todas las paginas

El archivo __init__.py quedaria asi

```python
from flask import Flask, render_template

def create_app(env='development', static_folder='../../static'):
    app = Flask(__name__, static_folder=static_folder)

    @app.get('/')
    def home():
        return render_template('home.html')
        
    @app.get('/about')
    def about():
        return render_template('about.html')
    
    @app.get('/contact')
    def contact():
        return render_template('contact.html')
    
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('error.html', error_code='404', error_message='Página no encontrada'), 404

    return app
```

Por ultimo lo subimos a produccion 

```
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin
```

---

### Clase 3 MVC + BluePrints

- [Entrega Parte 1](https://docs.google.com/document/d/e/2PACX-1vQgex-ZEYq-4aHqAbWABMRoZ21I4zZDlHJy0tTwwjLZ3ub70rScHLEq5Ix0MymgB3Ce2GZbwrVRgqqB/pub)


Agregamos un controlador para mostrar en nuestra pagina una lista de issues(consultas/tickets). En `core` creamos un archivo `board` (tablero) en el que harcodeamos nuestras consultas ya que de momento no tenemos acceso a una base de datos. 

> Datos generados con chat-gpt

```python
def list_issues():
    """List all issues."""
    issues = [
        {
            'id': 1,
            'email': 'john.doe@example.com',
            'description': 'Unable to log in to the application.',
            'status': 'new'
        },
        {
            'id': 2,
            'email': 'sara.jones@example.com',
            'description': 'App crashes when navigating to the settings page.',
            'status': 'in-progress'
        },
        {
            'id': 3,
            'email': 'mark.smith@example.com',
            'description': 'Feature request: Add dark mode to the application.',
            'status': 'resolved'
        },
        {
            'id': 4,
            'email': 'lisa.johnson@example.com',
            'description': 'Error 404 when trying to access a specific URL.',
            'status': 'new'
        },
        {
            'id': 5,
            'email': 'peter.wilson@example.com',
            'description': 'Performance issue: Application takes too long to load.',
            'status': 'in-progress'
        },
        {
            'id': 6,
            'email': 'mary.brown@example.com',
            'description': 'Bug: Incorrect data displayed in the user profile.',
            'status': 'resolved'
        },
        {
            'id': 7,
            'email': 'alex.miller@example.com',
            'description': 'Feature request: Integrate with third-party API for weather information.',
            'status': 'new'
        },
        {
            'id': 8,
            'email': 'chris.white@example.com',
            'description': 'App freezes when attempting to upload large files.',
            'status': 'in-progress'
        },
        {
            'id': 9,
            'email': 'emily.jones@example.com',
            'description': 'Bug: Unable to delete account from profile settings.',
            'status': 'resolved'
        },
        {
            'id': 10,
            'email': 'david.taylor@example.com',
            'description': 'Feature request: Implement a chat feature within the application.',
            'status': 'new'
        }
    ]
    return issues
```

> Esto en el futuro lo cambiamos por las consultas a la base de datos

Dentro de web creamos la carpeta `controllers` con el archivo `issues.py`

> El Blueprint es una forma de organizar las rutas

```python
from flask import render_template
from src.core import board
from flask import Blueprint

issues_bp = Blueprint('issues', __name__, url_prefix='/consultas')

@issues_bp.get('/')
def index():
    issues = board.list_issues()

    return render_template('issues/index.html', issues=issues)
```

Despues de esto, tenemos que crear una carpeta en `templates` con el nombre `issues` y dentro un archivo `index.html`

```html
{% extends 'layout.html' %}

{% block head %}<link rel="stylesheet" href="{{ url_for('static', filename='issues.css') }}"> {% endblock %}

{% block title %}Consultas{% endblock %}

{% block header %}
    {{ super() }}
{% endblock %}

{% block content %}
    <h1>Issues</h1>
    <table class="index-table box">
        <thead>
            <tr>
                <th>ID</th>
                <th>Email</th>
                <th>Description</th>
                <th>Status</th>
            </tr>
        </thead>
        <tbody>
            {% for issue in issues %}
                <tr>
                    <td>{{ issue.id }}</td>
                    <td>{{ issue.email }}</td>
                    <td>{{ issue.description }}</td>
                    <td>{{ issue.status }}</td>
                </tr>
            {% endfor %}
    </table>
{% endblock %}
```

---

### Clase 4 Database + Configs + ORM