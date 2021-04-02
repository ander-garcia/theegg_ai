#!/usr/bin/bash

# esqueleto para parsear argumentos en 
# https://unix.stackexchange.com/questions/31414/how-can-i-pass-a-command-line-argument-into-a-shell-script

helpFunction()
{
   echo ""
   echo "Usage: $0 -d dir"
   echo -e "\t-d Carpeta en la que están las imágenes"
   exit 1 # Exit script after printing help
}


while getopts "d:" opt
do
   case "$opt" in
      d ) FOLDER="${OPTARG}" ;;
      ? ) helpFunction ;; # Print helpFunction in case parameter is non-existent
   esac
done


# Print helpFunction in case parameters are empty
if [ -z "$FOLDER" ] 
then
   echo "Falta alguno o todos los parámetros";
   helpFunction
fi

# Begin script in case all parameters are correct
# echo "$FOLDER"


# pregunta para continuar
# https://askubuntu.com/questions/1705/how-can-i-create-a-select-menu-in-a-shell-script
read -n 1 -p "Este script renombra las fotos de la  carpeta ${FOLDER} a formato YYYYMMDD_HHMMSS. Para continuar pulsa s, para salir cualquier otra tecla " ans;

case $ans in
    s|S)
        echo "Iniciando ejecución del script";;
    *)
        exit;;
esac

# renombre todas las fotos
# from https://stackoverflow.com/questions/25152995/linux-shell-renaming-files-to-creation-time
for f in *.jpeg *.jpg
do
    mv -n "$f" "$(exiftool -d "%Y%m%d_%H%M%S" -CreateDate "$f" | awk '{print $4".jpg"}')"
done

echo "Finalizado"