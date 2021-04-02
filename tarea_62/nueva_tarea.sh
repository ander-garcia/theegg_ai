#!/usr/bin/bash

# pregunta para continuar
# https://askubuntu.com/questions/1705/how-can-i-create-a-select-menu-in-a-shell-script
read -n 1 -p "Este script busca nuevas tareas en la plataforma TheEgg. Es necesario contar con un usuario. Para continuar pulsa s, para salir cualquier otra tecla " ans;

case $ans in
    s|S)
        echo "Iniciando ejecución del script";;
    *)
        exit;;
esac

# Lee nombre de usuario de un fichero
# o lo pregunta por consola
FILE=/tmp/egg_user
if ! test -f "$FILE"; then
     read  -p "User: " USER
     echo $USER > /tmp/egg_user
else
        echo "Nombre de usuario leido desde fichero /tmp/egg_user. Si desea actualizarlo elimine el fichero"
fi
USER=$(</tmp/egg_user)

# Lee password de usuario de un fichero
# o lo pregunta por consola
FILE=/tmp/egg_password
if ! test -f "$FILE"; then
     read -s -p "Password: " PASSWORD
     echo $PASSWORD > /tmp/egg_password
else
        echo "Password de usuario leido desde fichero /tmp/egg_password. Si desea actualizarlo elimine el fichero"
fi
PASSWORD=$(</tmp/egg_password)

echo "Buscando nuevas tareas de The Egg para $USER"

# se asegura que existe el fichero de tareas previas
touch tareas_previas.txt
# login a TheEgg guardando la cookie y silenciando salida curl
curl  -sc  "/tmp/egg_cookie" 'https://theegg.ai/plataforma/php/auth/login_internal.php' --data-raw "usuario=${USER}&password=${PASSWORD}" > tmp_login.txt
if grep -q "Datos incorrectos" "tmp_login.txt"; then
  echo "Login error. Eliminando fichero con el nombre de usuario y password. Inténtelo de nuevo"
  rm /tmp/egg_user
  rm /tmp/egg_password
  rm /tmp/egg_cookie
  exit 1
elif grep -q "Correcto" "tmp_login.txt"; then
  echo "Login OK"
else
  echo "Error desconocido al hacer el login.Inténtelo de nuevo más tarde"
  exit 1
fi
# Recupera listado de tareas cargando la cooike y extrae su id
# el id está en un html <small>XX</small>
# el listado de ids de tareas pendientes se guarda en un fichero
curl -sb "/tmp/egg_cookie" https://theegg.ai/plataforma/u_listar_tarea | grep -Po  "small>#(\K\d{2})" > tareas_pendientes.txt
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
rm tmp_login.txt

echo "Finalizado"