<div align="center"> 

<style>
   body {
      background-color: white;
      color: black;
      transition: background-color 0.5s, color 0.5s; /* Esto añade una suave transición al cambiar los colores */
   }

   body.dark-mode {
      background-color: #1E2021;
      color: white;
   }
   body.dark-mode strong ,body.dark-mode h1, body.dark-mode h2, body.dark-mode h3, body.dark-mode h4, body.dark-mode h5, body.dark-mode h6{
   color: white;
   }
   body.dark-mode blockquote{
      filter: invert(1);
   }
   button{
      font-family: 'Roboto', sans-serif;
      font-size: 14px;
      font-weight: bolt;
      background: #1e90FF;
      width: 100px;
      padding: 7px;
      text-align: center;
      text-decoration: none;
      text-transform: uppercase;
      color: #fff;
      border-radius: 6px;
      cursor: pointer;
      box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
   }
</style>



<script>
    function toggleDarkMode() {
        const body = document.body;
        if (body.classList.contains('dark-mode')) {
            body.classList.remove('dark-mode');
        } else {
            body.classList.add('dark-mode');
        }
    }
</script>

<img src='https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat'>

<img src='https://img.shields.io/github/stars/Fabian-Martinez-Rincon/Proyecto-de-Software'>
<img src='https://img.shields.io/github/repo-size/Fabian-Martinez-Rincon/Proyecto-de-Software'>



<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=30&duration=1200&pause=1000&color=1e90FF&center=true&width=635&lines=Proyecto-de-Software"/>



<a title="" href="https://cafecito.app/ei-materias"><img src="/Documentos/Cafecito.png" alt="" /></a>

</div>



<div align='center'>
<button onclick="toggleDarkMode()">Oscuro</button>
<a href='https://github.com/Fabian-Martinez-Rincon/Proyecto-de-Software/tree/main'><button style='background: #ecec00'> ⭐ </button></a>
<a href='https://github.com/Fabian-Martinez-Rincon'><button style='background: #000000'>Github</button></a>

<img src= 'https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/23277383-db80-4d02-bbc7-114d835518d1
' height="20" width="100%"></div>

<table><tr><td>Actividades</td><td>Calendario</td></tr>

<tr><td>


- [All The Tags](https://allthetags.com/)

</td><td>


- **01/09/2023** Actividad Teorica 1
- **06/10/2023** Actividad Teorica 2
- **03/11/2023** Actividad Teorica 3
- **01/12/2023** Actividad Teorica 4
- **01/09/2023** Actividad Practica 1
- **15/09/2023** Actividad Practica 2
- **20/10/2023** Entrega Practica Primera Parte
- **24/11/2023** Entrega Practica Segunda Parte

</td></tr>
</table>

<img src= 'https://github.com/Fabian-Martinez-Rincon/Fabian-Martinez-Rincon/assets/55964635/23277383-db80-4d02-bbc7-114d835518d1
' height="20" width="100%"></div>


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