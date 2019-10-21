Desarrollo de Aplicaciones para Internet (2019-2020)
 Guión de Prácticas 4: Frameworks CSS, Persistencia: Bases de Datos NoSQL
-------------------------------------------------------------------------

### S. Alonso ([zerjioi@ugr.es](mailto:zerjioi@ugr.es)) y J.M. Guirao ([jmguirao@ugr.es](mailto:jmguirao@ugr.es))

#### Resumen

En esta práctica incorporaremos algún framework `CSS` que nos ayude a que nuestra app sea *"adaptable"*. Asímismo veremos como utilizar una base de datos `NoSQL`, que pueden ser de gran utilidad en una aplicación web.

#### Herencia en Plantillas

El mecanismo de herencia proporciona una herramienta potente para reutilizar todas las partes comunes de las distintas plantillas de nuestra página. Asegúrate que usas dicho mecanismo en las plantillas de tu sitio para no repetir el código `HTML` de la cabecera, barras laterales, pie de página...

#### Frameworks CSS

En la actualidad existen múltiples [Frameworks CSS](https://en.wikipedia.org/wiki/CSS_frameworks) que nos permiten fácilmente conseguir que el diseño de nuestra página web sea ["adaptable"](https://es.wikipedia.org/wiki/Dise\%C3\%B1o_web_adaptable) a distintos tipos de pantalla (móvil, tablet, portátil, sobremesa...), así como que tenga una mejor apariencia. Dentro de dichos frameworks, uno de los más extendidos es [Bootstrap](http://getbootstrap.com/).

En esta práctica debe adaptar la plantilla que haya utilizado previamente para incorporar Bootstrap (u otro framework CSS) y conseguir que presente un diseño adaptable. Para ello se puede partir de uno de algún [template básico](https://getbootstrap.com/docs/4.0/examples/), o bien adaptar alguno de los templates gratuitos de Bootstrap que se pueden encontrar en Internet.

**Nota:** Es posible que si has utilizado alguna plantilla bajada de Internet esa plantilla ya use Bootstrap u otro framework CSS. En ese caso es interesante entender completamente las estrategias de posicionamiento que usa dicho framework (por ejemplo el diseño en columnas).

#### Persistencia: Bases de Datos NO-SQL: `mongoDB`

[`MongoDB`](http://www.mongodb.org/) es una base de datos NO-SQL potente que nos permitirá almacenar cualquier información que nuestra aplicación web necesite. Desde Python podemos acceder a la base de datos `MongoDB` usando el cliente [`Pymongo`](http://altons.github.io/python/2013/01/21/gentle-introduction-to-mongodb-using-pymongo/).

En esta práctica vamos a usar alguno datos de prueba para `mongoDB` (ver siguiente apartado). La idea es crear varias páginas web que nos permitan consultar información sobre algunos de estos datos, hacer alguna búsqueda sencilla, insertar nuevos elementos, modificarlos, etc.

#### Instalación del servicio `mongoDB` y de bases de datos de prueba

Usaremos una imagen de [mongo](https://hub.docker.com/_/mongo) para montar nuestro servicio de base de datos, de manera que el archivo **docker-compose.yml** queda como:

    # docker-compose.yml

    version: '3.7'

    services:
          flask:
             build: .
             depends_on:
                - mongo
             ports:
                - 5000:5000
             volumes:
                - ./flask:/flask

          mongo:
             image: mongo:latest
             ports:
                - 27017:27017
             volumes:
                - ./dump:/dump              # los datos de prueba
                - ./datos_db:/data/db       # almacenamiento en el host

Crearemos los directorios **dump**, para los datos de prueba, y **datos\_db**, para el almacenamiento en el host de los datos de la DB en el host, ya que si no la hecmos así, los perderiamos en cada build

Además tenemos que añadir un nuevo requisito(`pymongo`) a `requirementsFlask.txt`:

    # requirementFlask.txt

    Pillow
    Flask
    pymongo

Nos aseguramos que la imagen de `Flask` se reconstruye con los nuevos requisitos:

    > docker-compose build

En este punto ya podríamos manejar la base de datos desde nuestra aplicación `Flask` usando `pymongo`. Sin embargo no tenemos ningún dato sobre el que trabajar. Vamos a alimentar la base de datos con unas [colecciones descargadas de Internet](https://github.com/SouthbankSoftware/dbkoda-data).

Para esto ponemos a funcionar los servicios:

    > docker-compose up

y en otra terminal, abrimos una sesión de bash en el contenedor de mongo:

    #> docker-compose exec mongo /bin/bash

y en la terminal del contenedor:

    #> mongorestore --drop dump

Aqui podemos comprobar que los datos están usando el [shell de mongo](https://docs.mongodb.com/manual/mongo/). En [http://www.diegocalvo.es/tutorial-de-mongodb-con-ejemplos/](http://www.diegocalvo.es/tutorial-de-mongodb-con-ejemplos/) tenemos una chuletas para usarlo.

Si todo ha ido bien ya podríamos hacer que nuestra aplicación web muestre información de nuestra base de datos. Por ejemplo: el título de un capítulo de la serie Friends:

    #./flask/app.py
    ...

    from pymongo import MongoClient

    client = MongoClient("mongo", 27017) # Conectar al servicio (docker) "mongo" en su puerto estandar
    db = client.SampleCollections        # Elegimos la base de datos de ejemplo

    ...

    @app.route('/mongo')
    def mongo():
        val = db.samples_friends.find()  # Encontramos los documentos de la coleccion "samples_friends"

        return val[0]['name']


