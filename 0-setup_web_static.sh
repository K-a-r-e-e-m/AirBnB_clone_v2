#!/usr/bin/env bash
# Sets up your web servers for the deployment of web_static.

nginx -v > /dev/null 2>&1
if [ $? -eq 127 ]; then
    apt-get update
    apt-get install nginx -y
fi

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "This is test for nginx config" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/

echo "
server {
        listen 80 default_server;
        listen [::]:80 default_server;

        add_header X-Served-By $HOSTNAME;
        error_page 404 /error_not_found.html;

        location = /error_not_found.html {
                root /var/www/html;
                internal;
        }

        root /var/www/html;
        server_name _;

        location /redirect_me {
            return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }

        location /hbnb_static/  {
            # Attempt to serve request as file
            alias /data/web_static/current;

        }
}" > /etc/nginx/sites-enabled/default

service nginx restart
