# TAREA 62: Convertir una computadora tonta en algo más inteligente: bash scripting

## Requerimientos

Acceso al shell de Linux

## Resumen

En esta tarea se han desarrollado tres scripts de Shell. A nivel general, primero los scripts comprueban si los argumentos son correctos, y muetran la ayuda si no lo son. Luego el script describe su función y pregunta antes de continuar (si se integrasen en un cron habría que comentar esta funcionalidad). Los script muestran un mensaje de finalizado al concluir. Cada script tiene comentarios que explican detalles de los mismos

### Comprobar si hay tareas nuevas en TheEgg (nueva_tarea.sh)

Este script se loguea en la cuenta de TheEgg y mira si hay nuevas tareas. Para ello, cada vez que se ejecuta guarda las tareas existentes en el fichero tareas_previas.txt. Cada vez que se ejecuta se compara contra este fichero.

El funcionamiento general es el siguiente. El script usa los ficheros /tmp/egg_user, /tmp/egg_password y /tmp/egg_cookie. Los dos primeros guardan en usuario y su contraseña. Si los ficheros no existen se piden al usuario, si existen se leen.
Luego, se usa curl para hacer un login y guardar la cookie (PHPSESSION). Se analiza el texto devuelto por curl para ver si el login ha sido correcto o incorrecto.
Usando esta cookie se accede a la página en la que se listan las tareas disponibles. Se ha visto en el html que el tag del id de las tareas es <small>#ID</small>. Se usa grep para obtener este id mediante una expresión regular, y se almacenan en un fichero temporal las tareas del listado
Luego se compara mediante diff este listado con el listado anterior de tareas y la comparación se guarda en un fichero. Si el fichero está vació es que no hay nuevas tareas desde la última ejecución
Si el fichero tiene contenido, se excluye la primera línea (que la mete diff) para contar cuentas tareas nuevas hay y se sacan por pantalla.
Por último, se borran los ficheros temporales y se actualiza el contenido del fichero con las tareas previas

### Backup

Este script está pensado para agilizar la generación de backups. Dada una carpeta de origen y destino, crea un backup en el destino en el formato tar y nombre YYYYMMDD_HHMMSS_egg_backup.tar.
Por último, busca en la carpeta de backup los ficheros de más de N días (argumento -d) y los borra

### Renombrar fotos

Este script renombra las fotos usando la fecha de creación de sus datos EXIF. Está pensado para guardar las fotos con esta nomenclatura. Tiene un parámetro para indicar la carpeta en la que están los fotos. Luego busca las fotos y renombra cada una de ellas mediante el comando exiftool

## TODO

Los scripts tienen multitud de puntos de mejora, si alguien los encuentra útiles puede evolucionarlos todo lo que quiera
