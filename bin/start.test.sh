#!/bin/bash

docker build -f dags/test/docker/dockerfile.test -t docker_test . && \
docker-compose up -d