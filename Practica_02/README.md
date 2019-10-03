Desarrollo de Aplicaciones para Internet (2019-2020)
Guión de Prácticas 2: Micro Framework Web para Python: `Flask`
---------------------------------------------------------------

#### Resumen

[`Flask`](https://palletsprojects.com/p/flask/) es un micro framework web para Python de uso sencillo pero suficientemente potente que permite desarrollar una aplicación web en poco tiempo.

En esta sesión trataremos de construir algunas pequeñas aplicaciones web usando las opciones más básicas de `Flask`. De hecho en esta sesión no prestaremos aún atención a buenas prácticas de desarrollo (como el uso del patrón [MVC](https://es.wikipedia.org/wiki/Modelo%E2%80%93vista%E2%80%93controlador)). En futuras sesiones se practicarán otros conceptos como el manejo de sesiones, templates, el acceso a bases de datos, etc.

#### Un `Hola Mundo!` en `Flask`

En la [página web oficial de `Flask`]() podemos encontrar un [ejemplo minimalista ("Hola Mundo")](https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application) en el que se utiliza el framework para crear un aplicación web extremadamente sencilla que saluda al usuario. Copie dicho código, ejecútelo, compruebe que funciona e intente entender cada parte de dicho programa. Es posible que necesite consultar la [`API`](https://flask.palletsprojects.com/en/1.1.x/#api-reference) o el ["Libro de Recetas"](https://flask.palletsprojects.com/en/1.1.x/) de la biblioteca.

Tenga en cuenta que para que funcione `Flask` en nuestro contenedor necesitamos instalarlo (no viene de serie en las instalaciones básicas de `Python`). Para ello vamos a crear un nuevo servicio de `Docker` tal y como sigue:

    # añadir el servicio en docker-compose.yml

    ...

    services:  # No repetir esta línea. Añadir debajo de los servicios existentes
        flask:
            build: 
              context: .
              dockerfile: flask_dockerfile
            ports:
              - "8080:5000"
            volumes:
              - ./flask:/flask
            working_dir: /flask

    # flask_dockerfile

    FROM python:3.7
    WORKDIR /ejer

    ENV FLASK_APP app.py
    ENV FLASK_RUN_HOST 0.0.0.0
    ENV FLASK_ENV development

    RUN apt-get install libjpeg-dev \
                           zlib1g-dev \
                           libfreetype6-dev \
                           liblcms2-dev 
                          
                           
    COPY requirementsFlask.txt requirementsFlask.txt
    RUN pip install -r requirementsFlask.txt
    COPY . .

    CMD ["flask", "run"]

    # requirementFlask.txt

    Pillow 
    Flask

    #./flask/app.py

    from flask import Flask
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello, World!'

Recuerde que si en algún momento cambia la configuración de uno de sus contenedores es posible que tenga que reconstruirlos con `docker-compose build`.

**Nota:** investigue que significa poner la aplicación en modo `debug` para facilitar el desarrollo (por ejemplo, evitando tener que relanzar la aplicación cada vez que el codigo cambie). Para ello averigüe que significan las líneas de `flask_dockerfile`.

**Nota 2:** La aplicación `Flask` por defecto escucha en el puerto `5000` y en el interfaz `loop` (`127.0.0.1`), esto es, solo podrá ser visible desde el mismo contenedor. Para poder cargar la aplicación desde fuera del `guest` se hace necesario hacr un `forward` de nuestra máquina `host` al `guest` con el uso de la directiva `ports` en el `docker-compose.yml`. En nuestro caso se redirecciona el puerto `8080` de nuestra máquina al puerto `5000` del contenedor, con lo que para ver nuestra aplicación tendremos que cargar [http://127.0.0.1:8080](http://127.0.0.1:8080).

**Nota 3:** Para lanzar el contenedor y que la redirección de puerto hay que hacerlo debemos hacerlo con el comando `up` de `docker-compose`:

    > docker-compose up flask

#### Sirviendo contenidos estáticos (imágenes, hojas de estilo, etc)

Averigüe el mecanismo más habitual que ofrece `Flask` para servir contenidos **estáticos** tales como imágenes u hojas de estilo. Añada algunas imágenes estáticas a su aplicación y compruebe que el cliente es capaz de acceder a ellas directamente a través de una `URL`.

Aunque el método habitual para servir páginas web de `Flask` es el uso de `templates`, modifique el ejemplo original del punto anterior para generar en vez de simplemente el código `¡Hola Mundo!`, generar código `HTML` correcto en el que se incluya, entre los demás elementos necesarios, una página de estilo `CSS` y alguna imagen estática.

#### Manejo de URLs

Averigüe el mecanismo de `Flask` para el análisis y manejo de distintas `URLs`. Cree una nueva aplicación para servir páginas distintas dependiendo de la `URL` introducida. Asimismo, sería conveniente ser capaces de obtener los parámetros de una llamada `GET`. Compruebe que puede utilizar variables en parte de la `URL` (por ejemplo, mostrar contenidos distintos para las siguientes urls:

-   `http:///user/pepe`
-   `http:///user/zerjillo`
-   `http:///user/[cualquierUsuario]`

Por último, defina una página para el caso en que una URL no esté definida (error [`HTTP 404, not found`](http://en.wikipedia.org/wiki/HTTP_404)).

#### **Para Nota:** Creando Imágenes Dinámicas [binarias]

A estas alturas debemos ser capaces de hacer un sitio web dinámico sencillo (probablemente no muy bonito hasta que no utilicemos templates). Pese a que muchísimos sitios dinámicos solo cambian su código `HTML` dependiendo de las entradas de los usuarios, en este último apartado vamos a ir un paso más allá: se creará contenido gráfico dinámico.

La idea de este ejercicio es crear una aplicación web dinámica que a partir de ciertos parámetros sea capaz de generar en directo una imagen fractal. Para esta tarea podemos reutilizar el código de los ejercicios de la primera sesión de prácticas (ejercicio sobre el fractal de Mandelbrot). La aplicación web debe contar con al menos estas características:

-   Mediante parametros `GET` debemos poder definir al menos los siguientes parámetros para calcular el fractal: recuadro del plano complejo sobre el que se calculará el fractal `(x1, y1)` - `(x2, y2)` y anchura de la imagen resultante (en píxeles).
-   Una vez obtenidos dichos datos debe calcularse y dibujarse el fractal. Se podrá usar alguna función similar a las del guión de prácticas 1.
-   La imagen completamente creada debe mostrarse al usuario usando el formato PNG.

Adicionalmente, si se quiere mejorar la aplicación, se puede:

-   Añadir algunos parámetros `GET` para cambiar la paleta de color a utilizar cuando se dibuje el fractal y el número máximo de iteraciones a ejecutar cuando se calcula el fractal.
-   Implementar algún tipo de caché de la aplicación que evite recalcular el mismo fractal en caso de que se hagan dos peticiones idénticas (ahorrando ciclos de cómputo). Para conseguirlo, por ejemplo, se pueden guardar en disco los fractales con un nombre que identifiquen los parámetro utilizados para el cálculo. Cada vez que se solicite un nuevo fractal lo primero que realizará la aplicación será comprobar si el fichero con dichos parámetros ya ha sido creado. En caso afirmativo se servirá tal cual. En caso negativo, se realizarán los cálculos del fractal oportunos.
-   Mejorar el sistema de caché propuesto para que las imágenes de más de un día se borren para evitar colapsar el disco duro del servidor en caso de que se soliciten muchas imágenes fractales.

#### **Para Nota 2:** Creando Imágenes Dinámicas [Vectoriales]}

Desarrolle una aplicación web sencilla que nos permita crear una imagen [`SVG`](http://es.wikipedia.org/wiki/Scalable_Vector_Graphics) dinámica (que cambie cada vez que visitemos la página) y aleatoria. Por ejemplo, que cada vez que se visite la página dibuje elipses, rectángulos, etc. de colores y posiciones distintas.


