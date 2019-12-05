Desarrollo de Aplicaciones para Internet (2019-2020)
 Guión de Prácticas 8: Servicios y bibliotecas de `JS`
------------------------------------------------------

En esta práctica queremos usar algas bibliotecas existentes para crear servicios "complejos" como puedan ser incorporación de mapas y geolocalización a nuestra aplicación web o gráficas estadísticas.

#### Mapas y geolocalización

Existen varias bibliotecas para incorporar mapas a nuestra página web. Por ejemplo Google ofrece [Google Maps JavaScript API](https://developers.google.com/maps/documentation/javascript/?hl=es) y [Google Street View Image API](https://developers.google.com/maps/documentation/streetview/?hl=es) y también es bastante usada `OpenStreetMap` (mucho más abierta que la de Google) sobre la que se han montado [varias bibliotecas o frameworks](https://wiki.openstreetmap.org/wiki/Frameworks#Webmaps).

En esta práctica se pide incorporar alguno de los servicios de mapas anteriormente citados a nuestra página web. Dicho mapa puede mostrar nuestra posición actual, el lugar de nacimiento de los músicos de nuestra aplicación (habrá que añadir los campos de `latitud` y `longitud` al modelo correspondiente, graficar el área de distintos barrios, calcular rutas para ir de un punto a otro, etc. (cuantas más opciones use nuestro mapa mejor se considerará la práctica).

 

#### Gráficas estadísticas (con `Highcharts`)

`Highcharts` un librería de `JavaScript` que nos permite integrar gráficas estadísticas (y de otros tipos) en nuestra página web, entre las que encontramos gráficas de tarta, ditribución de puntos, gráficas de barras, tablas dinámicas, gráficas de líneas, líneas temporales, etc.

La manera más habitual de usarla es introduciendo un trozo de código `JavaScript` en nuestra página. Dicho `JavaScript` carga algunas bibliotecas, define las series de datos a mostrar, selecciona las opciones para configurar la gráfica y crea un objeto gráfica con un identificador determinado. En el cuerpo de la página web se definirá un objeto `<div>` con el identificador de la gráfica donde se mostrará la misma.

La biblioteca es bastante sencilla de utilizar y tiene una [documentación](https://www.highcharts.com/docs) bastante clara.

En este ejercicio vamos a intentar integrar dicha biblioteca en nuestro sitio web. Para ello crearemos alguna página que nos permita visualizar una gráfica con datos de nuestros modelos, p.e., número de álbumes de cada grupo (o cualquier otra cosa que se nos ocurra).

 

#### Para nota

Hacer el ejercicio anterior pero obieniendo los datos a través de una llamada AJAX, como en esta [demostración](https://www.highcharts.com/demo/line-ajax).


