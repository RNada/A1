#1/bin/bash

project_name=team_position

#Build server
docker build -t ${project_name}_server server

#Build animal_api
docker build -t ${project_name}_api team_api

#Create network
docker network create ${project_name}_network

#Run containers
docker run -d \
    -p 5000:5000 \
    --name ${project_name}_server \
    --network ${project_name}_network \
    ${project_name}_server

docker run -d \
    -p 5000:5000 \
    --name ${project_name}_api \
    --network ${project_name}_network \
    ${project_name}_api 



