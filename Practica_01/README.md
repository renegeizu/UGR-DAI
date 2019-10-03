Desarrollo de Aplicaciones para Internet (2019-2020)
Guión de Prácticas 1: Python y entorno de trabajo
----------------------------------------------------

#### Resumen

Durante las prácticas de la asignatura *Desarrollo de Aplicaciones para Internet* (DAI) vamos a hacer uso intensivo de diversos lenguajes de programación. Entre otros, utilizaremos *Python*, un lenguaje de alto nivel sencillo, potente, libre, "fácil de aprender", interpretado y multiplataforma (entre otras características). En esta primera práctica trataremos de resolver algunos problemas genéricos de programación usando dicho lenguaje para familiarizarnos con sus tipos de datos, estructuras de control, etc. Por otra parte haremos un primer uso de contenedores (Docker) para familiarizarnos con la gestión del "servidor".

Para aquellos que no tengan conocimientos sobre este lenguaje, existen numerosos manuales en Internet que permiten acercarse a la programación Python de manera sencilla y amena como por ejemplo: [A Byte of Python](http://swaroopch.com/notes/python/) o el [manual de Google sobre Python](https://developers.google.com/edu/python/).

#### Preparación del entorno

Para las prácticas del curso, utilizaremos contenedores [Docker](https://www.docker.com/). De esta manera conseguimos:

-   Aislar nuestro código del resto del ordenador, sin que interfiera lo que pueda instalarse antes o después.
-   Conseguir un entorno **idéntico** para todos los participantes del curso.
-   Tener nuestra aplicación lista para subirla a la nube.

Un primer paso será instalar tanto el [motor de Docker](https://docs.docker.com/install/) como [Docker Compose](https://docs.docker.com/compose/install/). En este guión no se darán instrucciones concretas para la instalación puesto que depende del sistema operativo anfitrión donde desarrollaremos nuestras prácticas. Consulta los enlaces anteriores para instalarlos en tu sistema operativo. También puedes consultar el siguiente tutorial: [What is Docker and How to Use it With Python](https://djangostars.com/blog/what-is-docker-and-how-to-use-it-with-python/).

Una vez instalados Docker y Docker compose podemos construir un primer fichero `docker-compose.yml` para ejecutar los ejercicios de este guión. Una pista: para este fichero de Docker compose especificamos que se monte una carpeta `ejer` que debe encontrarse en el mismo directorio que el fichero `docker-compose.yml`:

    # docker-compose.yml

    version: '3.7'

    services:
       ejercicios:
          image: python:3.7
          volumes:
            - ./ejer:/ejer
          working_dir: /ejer

    # ejer/hola.py

    print("Hola mundo!")

Si todo va bien podemos ejecutar el fichero `ejer/hola.py` dentro del contenedor `ejercicios` con la siguiente orden:

     > docker-compose run ejercicios python hola.py

#### Problemas "Sencillos"

1.  Programe un mini-juego de "adivinar" un número (entre 1 y 100) que el ordenador establezca al azar. El usuario puede ir introduciendo números y el ordenador le responderá con mensajes del estilo *"El número buscado el mayor / menor"*. El programa debe finalizar cuando el usuario adivine el número (con su correspondiente mensaje de felicitación) o bien cuando el usuario haya realizado 10 intentos incorrectos de adivinación.
2.  Programe un par de funciones de ordenación de matrices (UNIDIMENSIONALES) de números distintas (burbuja, selección, inserción, mezcla, montículos...) ([Wikipedia: Algoritmo de ordenamiento](http://es.wikipedia.org/wiki/Algoritmo_de_ordenamiento)). Realice un programa que genere aleatoriamente matrices de números aleatorios y use dicho métodos para comparar el tiempo que tardan en ejecutarse.
3.  La [Criba de Eratóstenes](http://es.wikipedia.org/wiki/Criba_de_Erat\%C3\%B3stenes) es un sencillo algoritmo que permite encontrar todos los números primos menores de un número natural dado. Prográmelo.
4.  Cree un programa que lea de un fichero de texto un número entero `n` y escriba en otro fichero de texto el `n-ésimo` número de la [sucesión de Fibonacci](http://es.wikipedia.org/wiki/Sucesi\%C3\%B3n_de_Fibonacci).
5.  Cree un programa que:
    -   Genere aleatoriamente una cadena de `[` y `]`.
    -   Compruebe mediante una función si dicha secuencia está *balanceada*, es decir, que se componga de parejas de corchetes de apertura y cierre correctamente anidados. Por ejemplo:
        -   `[]` -\> Correcto
        -   `[[][[]]]` -\> Correcto
        -   `[][]` -\> Correcto
        -   `][` -\> Incorrecto
        -   `[[][[` -\> Incorrecto
        -   `[]][[]` -\> Incorrecto

#### Problemas "Complejos"

1.  Implemente el [Juego de la Vida](http://es.wikipedia.org/wiki/Juego_de_la_vida). La salida de cada iteración debe guardarse en ficheros de texto con nombre consecutivo.
2.  Realice un programa que cree un fichero de imagen que contenga una representación del [Conjunto de Mandelbrot](http://es.wikipedia.org/wiki/Conjunto_de_Mandelbrot) entre unas coordenadas `(x1, y1)` y `(x2, y2)` que se le preguntarán al inicio del programa al usuario. **Nota:** Es muy probable que para este ejercicio quioeras utilizar alguna biblioteca gráfica que te permita manejar y grabar imágenes (por ejemplo [Pillow](https://pillow.readthedocs.io/en/stable/). Es un buen momento para jugar con `Docker` y `Docker compose` para añadir las bibliotecas que necesites en tu contenedor.
3.  Utilizando [expresiones regulares](http://docs.python.org/3.4/library/re.html) realice funciones para:
    -   Identificar cualquier palabra seguida de un espacio y una única letra mayúscula (por ejemplo: `Apellido N`).
    -   Identificar correos electrónicos válidos (empieza por una expresión genérica y ve refinándola todo lo posible).
    -   Identificar números de tarjeta de crédito cuyos dígitos estén separados por `-` o espacios en blanco cada paquete de cuatro dígitos: `1234-5678-9012-3456` ó `1234 5678 9012 3456`.


