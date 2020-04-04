#!/bin/bash

docker run -d -p 8089:27017 --name do1mongo \
    -e MONGO_INITDB_ROOT_USERNAME=admin \
    -e MONGO_INITDB_ROOT_PASSWORD=ADMIN123.com \
    -v /data/do1mongo:/data/db \
    mongo

docker exec some-mongo sh -c 'exec mongodump -d <database_name> --archive' > /some/path/on/your/host/all-collections.archive