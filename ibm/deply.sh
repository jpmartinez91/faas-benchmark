#!/bin/bash

DIR_=$(pwd)
echo "Obteniendo Docker Image"
docker pull ibmfunctions/action-python-v3.7
echo "Entrando al directorio => $DIR_"

cd "$DIR_/fft"
echo "Instalando dependencias"
npm i 
docker run --rm -v "$PWD:/tmp" ibmfunctions/action-python-v3.7 bash -c "cd /tmp && virtualenv virtualenv && source virtualenv/bin/activate && pip install -r requirements.txt"

sls deploy

cd "$DIR_/com"
echo "Instalando dependencias"
npm i 
docker run --rm -v "$PWD:/tmp" ibmfunctions/action-python-v3.7 bash -c "cd /tmp && virtualenv virtualenv && source virtualenv/bin/activate && pip install -r requirements.txt"
sls deploy

# cd "$DIR_/ml"
# echo "Instalando dependencias"
# npm i 
# docker run --rm -v "$PWD:/tmp" ibmfunctions/action-python-v3.7 bash -c "cd /tmp && virtualenv virtualenv && source virtualenv/bin/activate && pip install -r requirements.txt"
# sls deploy