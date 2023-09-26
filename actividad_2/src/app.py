from flask import Flask

# Crea una aplicación Flask
app = Flask(__name__)

# Define la ruta para '/'
@app.route('/')
def hello_world():
    return 'Hola mundo'

# Si se ejecuta este script, inicia la aplicación
if __name__ == '__main__':
    app.run()


