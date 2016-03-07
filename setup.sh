#!/bin/bash

if [ ! -d dockerfiles/nginx/nginx ]; then
    mkdir dockerfiles/nginx/nginx
fi

mkdir workspace
cd workspace
git clone git@git.gatherhealth.com:gather/gather-rest.git
git clone git@git.gatherhealth.com:gather/gather-prov.git
git clone git@git.gatherhealth.com:gather/gather-tests.git
cd ..

cp ./setup_rest.sh ./workspace/gather-rest/
cp ./create_super_user.sh ./workspace/gather-rest/
chmod +x ./workspace/gather-rest/setup_rest.sh
chmod +x ./workspace/gather-rest/create_super_user.sh
cp ./setup_prov.sh ./workspace/gather-prov/
chmod +x ./workspace/gather-prov/setup_prov.sh
cp ./setup_test.sh ./workspace/gather-tests/
chmod +x ./workspace/gather-tests/setup_test.sh
cp ./local_settings_rest.py ./workspace/gather-rest/shaman_dm/local_settings.py
cp ./local_settings_prov.py ./workspace/gather-prov/shaman_prov/local_settings.py

#Create network for docker
docker network create -d bridge provider_net

#Docker compose setup
docker-compose build
docker-compose up
