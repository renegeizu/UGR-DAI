Desarrollo de Aplicaciones para Internet (2019-2020)
 Guión de Prácticas 7: `jQuery` y `AJAX`
----------------------------------------------------

En esta práctica usaremos la librería `JQuery` para completar nuestra aplicación:

#### Cambiar el CSS de la página de manera dinámica

Se pide que usando algunos botones se cambie el aspecto visual de la página modificando de manera dinámica el [CSS](http://api.jquery.com/css/) de la página. Por ejemplo (pero no tenemos que limitarnos solo a estos ejemplos):

-   Cambiar el tamaño de letra de la página (grande, normal, pequeña, absurda...).
-   Modificar los colores de nuestra página. Por ejemplo, podríamos crear un modo "nocturno", con colores y/o imágenes de fondo oscuros y colores de letra claros.
-   Con algún botón ocultar y mostrar alternatiamente (mejor si es con una animación) algún elemento de la página como es el menú, alguna imagen...

 

#### Crear un páginador (sin `AJAX`)

Cuando queremos mostrar muchos resultados se suele utilizar un paginador que "trocea" dichos resultados y los va mostrando poco a poco. Por ejemplo, al listar los grupos musicales en nuestra aplicación podemos hacer que los muestre de 5 en 5 y tenga controles de "página siguiente" y "página anterior" (e incluso enlaces a las páginas intermedias). Algo por el estilo a:

|Nombre Grupo|Albumes|Músicos|
|:-----------|:------|:------|
|Grupo 6|[Enlace a albumes grupo 6](javascript:;)|Enlace a músicos grupo 6|
|Grupo 7|[Enlace a albumes grupo 7](javascript:;)|[Enlace a músicos grupo 7](javascript:;)|
|Grupo 8|[Enlace a albumes grupo 8](javascript:;)|[Enlace a músicos grupo 8](javascript:;)|
|Grupo 9|[Enlace a albumes grupo 9](javascript:;)|[Enlace a músicos grupo 9](javascript:;)|
|Grupo 10|[Enlace a albumes grupo 10](javascript:;)|[Enlace a músicos grupo 10](javascript:;)|

[\<\<](javascript:; "Primera página") [\<](javascript:; "Página anterior") [1](javascript:;) 2 [3](javascript:;) [4](javascript:;) [\>](javascript:; "Página siguiente") [\>\>](javascript:; "Última página")

Se pide crear un páginador de este estilo SIN USAR NINGUNA BIBLIOTECA NI FUNCIÓN ESPECÍFICA para estos menesteres (y por ahora sin `AJAX`)

 

#### Adaptar el paginador para que use `AJAX`

Recargar toda la página para "simplemente" cambiar el contenido de unas cuantas celdas de la tabla de nuestro paginador es ineficiente (se tiene que generar la página completa y mandar toda esa información del servidor al cliente). Mediante `AJAX` se puede mejorar la carga de los datos del paginador para que solo se mande del cliente al servidor la información pertinente e los restaurantes de cada página (sin recargar el resto de elementos como cabeceras, menús, etc). `jQuery` cuenta con [funciones para facilitarnos la vida con `AJAX`](http://api.jquery.com/jquery.ajax/).

De manera simplificada podemos decir que en la parte del cliente (la plantilla) hacemos la petición `AJAX` y mostramos la respuesta:


    $(function(){  # de  jquery, se ejecuta cuando se carga la página    
         $.ajax({
            url: "{% url 'reclama_datos' %}",
            type: 'get',                        
            success: function(datos) {
                Visualiza_datos (datos);  
            },
            failure: function(datos) { 
                alert('esto no vá');
            }
        });
        
        function Visualiza_datos (datos) {
            ...  # Aqui quitamos los datos antiguos de la página y ponemos los nuevos
        };
    });

Y en el servidor mandamos los datos con la función `JsonResponse` con el parámetro `safe=False`:

    from django.http import JsonResponse

    def reclama_datos (request):

        ...
        
        return JsonResponse(datos, safe=False)

En este apartado se pide modificar el paginador del punto anterior para usar `AJAX` y no recargar la página completa en cada petición al paginador.


