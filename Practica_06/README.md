Diseño de Aplicaciones para Internet (2019-2020)
 Guión de Prácticas 6: Más Django
------------------------------------------------

#### Introducción

En esta práctica pretendemos profundizar en un par de aspectos de Django: el uso de sus **Modelos** y el uso de **plugins** o complementos que ya existen para determinadas tareas.

#### Los modelos de Django

Lo modelos en `Django` son un tipo especial de objeto que se guarda en la BD. Los modelos definen cada tipo de dato que debe almacenarse en la BD y sus restricciones. En esta práctica vamos a familiarizarnos con la definición y uso de modelos. Siguiendo el [tutorial de Django Girls](https://tutorial.djangogirls.org/es/django_models/) se pide que desarrollemos en nuestra aplicación algunos modelos con restricciones (validadores). Por centrar el ejercicio vamos a pedir al menos 3 modelos:

-   **Grupo Musical:** Que deberá tener alguna información como por ejemplo: nombre, fecha de fundación, estilo músical...
-   **Músico:** Que alamcenará alguna información como: nombre, fecha de nacimiento, instrumento principal...
-   **Álbum:** Que contendrá información como: título, distribuidora, fecha de lanzamiento...

Está claro que esos tres modelos están relacionados y por tanto se pide que se establezcan las relaciones pertinentes entre ellas. Por ejemplo: Entre *Grupo* y *Músico* hay una relación *1 a muchos* y entre *Grupo* y *Álbum* también hay una relación *1 a muchos*.

Una vez creados los modelos se deben aplicar los cambios en la base de datos de Django, se deben importar para que puedan ser accesibles desde el administrador (mira como hacerlo en el tutorial de Django Girls) y se debe probar a introducir, editar y borrar objetos de cada uno de los modelos prestando especial atención en como el sistema asegura que las restricciones (validadores) que se hayan puesto se cumplan.

**Para Nota:** Alguien con una mínima cultura musical se habrá dado cuenta que la relación entre *Grupo* y *Músico* no es necesariamente *1 a muchos* sino *muchos a muchos*, porque hay músicos que han formado parte de varios grupos: Dave Mustaine en Metallica y Megadeth, Dave Grohl en Nirvana y Foo Fighters o Melendi con sus múltiples colaboraciones con otros músicos (aunque en este último caso es discutible su inclusión en el modelo *Músico*). Adapte la relación entre esos dos modelos para conseguir que sea *muchos a muchos*.

#### Formularios

Django incorpora un mecanismo para manejar los formularios de manera eficiente. En este apartado se pide crear los formularios que permitan añadir, editar y borrar los modelos creados anteriormente desde nuestra página web. Por supuesto el formulario debe realizar todas las validaciones pertinantes (evitar campos en blanco, valores incorrectos, etc).

#### Autenticación

Ya que Django trae un mecanismo de usuarios y existen plugins para facilitar la creación, autenticación, etc de los mismos, en este apartado se pide adaptar nuestra aplicación para que deje de usar el mecanismo de autenticación que teníamos desarrollado (probablemente era bastante simple) e implemente el plugin `django-allauth` ([documentación de django-allauth](https://django-allauth.readthedocs.io/en/latest/)).

Adapta los templates que viene por defecto para que la página de login / registro... se integre bien en tu sitio web. En [este foro](https://stackoverflow.com/questions/9437545/overriding-default-templates-of-django-allauth) dan algunas pistas sobre como hacerlo.

**Nota:** En las transparencias de teoría hay varios enlaces con tutoriales para instsalar allauth así como algunos templates que usan bootstrap 4 para incorporar los formularios de autenticación.


