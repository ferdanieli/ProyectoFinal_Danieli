Nombre: Instituto Aprender Haciendo

Descripción y Uso: esta página contiene 3 blogs (apps), los cuales son: 
   1) Carreras: donde se puede consultar las carreras que ofrece el instituto,
   (nombre de la carrera, breve descripción y número de comisión). 
   ![blog de las carreras (http://127.0.0.1:8000/blog/carreras/)]
   2) Accounts: donde puedes loguearte con nombre de usuario y contraseña, si ya estás registrado.
   ![login (http://127.0.0.1:8000/accounts/login/)]
   Caso contrario, encontrarás un botón para registrarte si eres un usuario nuevo.
   ![registro (http://127.0.0.1:8000/accounts/register/)]; también encontrarás un botón
   para salir de la página, luego de haberte logueado ![logout (http://127.0.0.1:8000/accounts/logout/)].
   3) Comentarios: donde puedes dejar un comentario respecto a las carreras.
   ![comentarios (http://127.0.0.1:8000/mensajes/comentarios/)]
  De todas maneras, estos funcionalidades están en la página principal y puedes acceder
  a ellas haciendo click en los botones correspondientes, como se muestra en el video
  explicativo adjunto. 

Luego, se puedo observar un mensaje de bienvenida al Instituto, un detalle
respecto al diseño de la plataforma estudiantil, los textos de estudio y la modalidad de cursado
a distancia.
Al finalizar, se pueden observar 3 testimonios de estudiantes actuales.


Instalación: los requisitos para acceder son los siguientes:

1) Tener una cuenta de GitHub, que puedes crearla en este link ![(https://github.com/)]
2) Instalar git [(https://git-scm.com/download/win)]
3) Instalar pyenv [(https://github.com/pyenv-win/pyenv-win/blob/master/docs/installation.md#git-commands)]
4) Instalar IDE [(https://www.jetbrains.com/pycharm/download/?section=windows)], [(https://www.jetbrains.com/shop/eform/students)]

Una vez realizada la instalación, puedes clonar el proyecto realizando los siguientes pasos:

1) Abrir GitBash y escirbir: cd y nombre de la carpeta en la que deseas guardar el proyecto y das enter.
2) Luego escribes el siguiente comando: git clone https://github.com/ferdanieli/ProyectoFinal_Danieli.git y das enter.
3) Ingresar a PyCharm, abrir un proyecto, hacer click derecho en el menú, hacer click en "Open", buscar
la carpeta en donde elegiste clonar el proyecto, buscar y seleccionar el proyecto clonado y hacer click en "OK".
4) De esta manera, se abrirá el proyecto de la App en tu computadora. 
5) Crear el entorno virtual.
6) Tener instalado django, puedes hacerlo con el siguiente comando: pip install django
7) Realizar las migraciones con este comando: python manage.py makemigrations
8) Luego ingresas este comando para aplicar los cambios: python manage.py migrate
9) Crear un usuario inicial utilizando este comando: python manage.py createsuperuser
Aquí debes crear un nombre usuario, una dirección de correo y una contraseña (estos datos pueden no ser reales)
10) Ejecutar el proyecto, en este caso tienes dos opociones:
a) Desde el botón de ejecución del proyecto.
b) Utilizando el siguiente comando: python manage.py runserver
11) Luego, te aparecerá una url en la terminal en la que debes hacer click y, de esa manera,
accederás a la App.
En este link, podrás acceder a un tutorial de youtube en el cual podrás observar de manera dinámica
la aplicación de los pasos detallados anteriormente: [(https://youtu.be/sh4MuVRSHxQ)]
12) Recuerda activar la base de datos. 
