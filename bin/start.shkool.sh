#!/bin/bash

docker build -f dags/shkool/docker/dockerfile.extract -t docker_extract . && \
docker build -f dags/shkool/docker/dockerfile.load -t docker_load . && \
docker build -f dags/shkool/docker/dockerfile.transform -t docker_transform . && \
docker-compose up -d