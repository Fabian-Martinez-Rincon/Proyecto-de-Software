## Consulta 1 Proyecto

Josu creo la rama develop

Primero nos posicionamos en la rama develop

```bash
git checkout develop
```

Despus tenemos que crear una rama feature con su operacion correspondiente

```bash
git checkout -b feature/operacion
```

Subimos todo con git add nombre-archivo
    
```bash
git add nombre-archivo

git commit -m "mensaje"
```


Una vez que tenemos los cambios necesarios, subimos la rama con los cambios a github

```bash
git push origin feature/operacion
```
Una vez que todos los integrantes subieron sus cambios, se procede a hacer el merge de las ramas feature a develop

```bash
git checkout develop
git pull origin develop
```

Despues de hacer el pull, cada uno agrego su parte del codigo a calculadora y despues de eso, se procede a hacer el merge de la rama feature a develop

```bash
git merge feature/suma
```

Una vez que se hizo el merge, se sube la rama develop a github

```bash
git push origin develop
```