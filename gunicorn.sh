#!/bin/bash
kill `cat /var/www/bakery.pid`
gunicorn wsgi:app \
    --log-file bakery-error.log \
    -p /var/www/bakery.pid -D \
    -w 4 \
    --worker-class socketio.sgunicorn.GeventSocketIOWorker \
    -b 0.0.0.0:5000 \
    -t 360
