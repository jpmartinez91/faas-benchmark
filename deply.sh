#!/bin/bash
#!/bin/bash

DIR_=$(pwd)
cd "$DIR_/az"
./deploy.sh


cd "$DIR_/goo"
./deploy.sh

cd "$DIR_/ibm"
./deploy.sh

DIR_=$(pwd)
cd "$DIR_/az"
echo "Creando grupo de recuros"
az group create --name thesis --location eastus
echo "Creando cuenta de almacenamiento"
echo "Ejecutando... az storage account create --name thesisbenchmark --location eastus --resource-group thesis --sku Standard_LRS"
az storage account create --name thesisbenchmark --location eastus --resource-group thesis --sku Standard_LRS
echo "Creando Aplicacion de funcion"
echo "Ejecutando... az functionapp create --resource-group thesis --os-type Linux --consumption-plan-location eastus  --runtime python --name thesisbenchmark --storage-account  thesisbenchmark"
az functionapp create --resource-group thesis --os-type Linux \
--consumption-plan-location eastus  --runtime python \
--name thesisbenchmark --storage-account  thesisbenchmark
echo "Desplegando Aplicacion de funcion"
echo "Ejecutando... func azure functionapp publish thesisbenchmark --build-native-deps --no-bundler"
func azure functionapp publish thesisbenchmark --build-native-deps --no-bundler