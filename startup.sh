#!/usr/bin/bash

# source env/bin/activate

python3 -m gunicorn line.asgi:application -k uvicorn.workers.UvicornWorker --bind=0.0.0.0:9000
