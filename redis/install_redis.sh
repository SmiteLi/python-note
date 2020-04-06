#!/bin/bash

mkdir -p /data/do1redis

docker run  -d \
  -p 8088:6379 \
  --restart=always \
  -v /data/do1redis:/data \
  --name do1redis \
  redis redis-server --appendonly yes --requirepass "Admin123.com"

# pip install hiredis
# pip install redis
# py -m pip install redis
# pip install hiredis

