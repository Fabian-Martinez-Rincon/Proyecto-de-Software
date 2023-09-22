## Enunciado

![image](https://github.com/Fabian-Martinez-Rincon/Proyecto-de-Software/assets/55964635/40660e6f-f0c3-42bf-940c-c0446e096b18)

![image](https://github.com/Fabian-Martinez-Rincon/Proyecto-de-Software/assets/55964635/f8d0381e-f1c9-4183-9652-f4aad42653b1)

<img src= 'https://i.gifer.com/origin/8c/8cd3f1898255c045143e1da97fbabf10_w200.gif' height="20" width="100%">

# Problema sacado de la teoria

### ¿De qué color se muestra el texto "Mi color favorito"?

```html

    <!DOCTYPE html>
    <html lang="es">

    <head>
        <title>Jugando con estilos</title>
        <style>
             h1 {color:orange}
                h1.verde {color: green}
                 .azul {color: blue}
             #amarillo {color: yellow}
        </style>
    </head>

    <body>
        <h1 class="verde" id="amarillo" style="color:red"> Mi color favorito</h1>
    </body>

    </html>
```

El texto "Mi color favorito" se mostrará en color **rojo**.

Aunque hay múltiples reglas de estilo que podrían afectar al elemento `<h1>`, la prioridad de aplicación de estilos en CSS se determina por la especificidad y el orden en el que se definen. Además, cualquier estilo definido directamente en un elemento HTML usando el atributo `style` tiene la máxima prioridad.

Por lo tanto, debido a la prioridad del estilo inline, el texto "Mi color favorito" se mostrará en color rojo.
