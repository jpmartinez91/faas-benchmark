#!/bin/bash

DIR_=$(pwd)
echo "Entrando al directorio => $DIR_"

cd "$DIR_/fft"
if [ ! -d "node_modules" ]
then
echo "Instalando dependencias"
npm i 
fi
sls deploy


cd "$DIR_/ml"
if [ ! -d "node_modules" ]
then
echo "Instalando dependencias"
npm i 
fi
sls deploy


cd "$DIR_/com"
if [ ! -d "node_modules" ]
then
echo "Instalando dependencias"
npm i 
fi
sls deploy