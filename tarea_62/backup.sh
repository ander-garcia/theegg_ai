#!/bin/bash

# esqueleto para parsear argumentos en 
# https://unix.stackexchange.com/questions/31414/how-can-i-pass-a-command-line-argument-into-a-shell-script
DEFAULT_DAYS=14

helpFunction()
{
   echo ""
   echo "Usage: $0 -f file -d days -b backup_folder"
   echo -e "\t-f Fichero o carpeta para el backup"
   echo -e "\t-d Si existen backups de más días de antiguedad se eliminan (valor por defecto 14)"
   echo -e "\t-b Carpeta donde almacenar el backup"
   exit 1 # Exit script after printing help
}


while getopts "f:d:b:" opt
do
   case "$opt" in
      f ) FILE="$OPTARG" ;;
      d ) DAYS="${OPTARG}" ;;
      b ) BACKUP_FOLDER="${OPTARG}" ;;
      ? ) helpFunction ;; # Print helpFunction in case parameter is non-existent
   esac
done

# por defecto 14 días
DAYS="${DAYS:-$DEFAULT_DAYS}"

# Print helpFunction in case parameters are empty
if [ -z "$FILE" ] || [ -z "$DAYS" ] || [ -z "$BACKUP_FOLDER" ] 
then
   echo "Falta alguno o todos los parámetros";
   helpFunction
fi

# Begin script in case all parameters are correct
# echo "$FILE"
# echo "$DAYS"
# echo "$BACKUP_FOLDER"

# pregunta para continuar
# https://askubuntu.com/questions/1705/how-can-i-create-a-select-menu-in-a-shell-script
read -n 1 -p "Este script generará un backup en formato tar de ${FILE} y lo guardará en ${BACKUP_FOLDER}. También borrará los ficheros en la carpeta ${BACKUP_FOLDER} de más de ${DAYS} días. Para continuar pulsa s, para salir cualquier otra tecla " ans;

case $ans in
    s|S)
        echo "Iniciando ejecución del script";;
    *)
        exit;;
esac

# crea el tar con la marca de tiempo + theegg_backup
datetime=$(date '+%Y-%m-%d_%H%M%S')
BACKUP_NAME="${datetime}_theegg_backup"
tar -zcf $BACKUP_FOLDER/$BACKUP_NAME.tgz $FILE

echo "Backup creado en ${BACKUP_FOLDER}/${BACKUP_NAME}.tgz"
# Delete backups older than retention period
find $BACKUP_FOLDER -type f -mtime +$DAYS -exec rm {} +
echo "Backups antiguos eliminados"
echo "Finalizado"