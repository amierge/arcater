#!/bin/sh

cd web
nohup gunicorn -w 3 -k gevent -b :3006 web.wsgi:application > ../.out 2>&1 &
cd -
