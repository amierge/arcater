#!/bin/sh

port=3006

pid=$(netstat -tunlp | grep :$port | awk '{print $7}' | awk -F"/" '{ print $1 }');

if [  -n  "$pid"  ];  then
    kill  -9  $pid;
fi

cd web
nohup gunicorn -w 3 -k gevent -b :3006 web.wsgi:application > ../.out 2>&1 &
cd -
