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

config_file="/etc/nginx/sites-enabled/default"
searching="server_name _;"
new_string="\n\n\tlocation \/hbnb_static\/ {\n\t\talias /data/web_static/current;\n\t}"
sed -i "s/$searching/$new_string" $config_file

service nginx restart
