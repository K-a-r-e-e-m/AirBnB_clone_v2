#!/usr/bin/env bash
# Sets up your web servers for the deployment of web_static.

nginx -v > /dev/null 2>&1
if [ $? -eq 127 ]; then
    apt-get update
    apt-get install nginx -y
fi

mkdir -p /data/web_static/releases
mkdir -p /data/web_static/shared
echo "This is test for nginx config" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu data


sed -i "s/server_name _;/\n\n\tlocation \/hbnb_static\/ {\n\t\talias /data/web_static/current;\n\t}"

service nginx restart
