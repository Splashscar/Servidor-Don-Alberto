#!/bin/bash
echo"Iniciando el despliegue automatico de Don Alberto"

#moverse a la carpeta
cd /home/$USER/moto-api

# Traer los cambios desde GIT
echo"Trayendo la ultima version desde git"
git pull origin master

#Activar el entorno virtual
echo"Asegurando las dependencias"
source venv/bin/activate
pip install -r requeriments.txt --quiet

#Reiniciar el servicio de systemd
echo"Reiniciando el motor gunicorn"
suso systemctl restart moto-api.service

#Verificar que este vivo
echo"Despliegue completado con exito. El estado actual es:"
sudo systemctl status moto-api.service | grep "Active:"
