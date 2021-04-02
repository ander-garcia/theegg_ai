#!/usr/bin/bash

# Lee nombre de usuario de un fichero
FILE=/tmp/egg_user
if ! test -f "$FILE"; then
     read  -p "User: " USER
     echo $USER > /tmp/egg_user
fi
USER=$(</tmp/egg_user)

FILE=/tmp/egg_password
if ! test -f "$FILE"; then
     read -s -p "Password: " PASSWORD
     echo $PASSWORD > /tmp/egg_password
fi
PASSWORD=$(</tmp/egg_password)
echo "Buscando nuevas tareas de The Egg para $USER"

# se asegura que existe el fichero de tareas previas
touch tareas_previas.txt
# login a TheEgg guardando la cookie y silenciando salida curl
curl  -sc  "/tmp/cookie" 'https://theegg.ai/plataforma/php/auth/login_internal.php' --data-raw "usuario=${USER}&password=${PASSWORD}" > /dev/null
# Recupera listado de tareas cargando la cooike y extrae su id
# el id está en un html <small>XX</small>
# el listado de ids de tareas pendientes se guarda en un fichero
curl -sb "/tmp/cookie" https://theegg.ai/plataforma/u_listar_tarea | grep -Po  "small>#(\K\d{2})" > tareas_pendientes.txt
# se comparan los listados para ver si hay diferencias
diff tareas_pendientes.txt tareas_previas.txt |sed 1,1d > nuevas_tareas.txt
# comprueba si el fichero tiene datos
if [ -s nuevas_tareas.txt ]
then
        NUM_TAREAS=$(cat nuevas_tareas.txt |wc -l)
        echo "HAY  ${NUM_TAREAS} NUEVAS TAREAS"
        cat nuevas_tareas.txt
else
        echo "No hay nuevas tareas."
fi

# elimina ficheros temporales y actualiza las tareas previas
cp tareas_pendientes.txt tareas_previas.txt
rm tareas_pendientes.txt
rm nuevas_tareas.txt