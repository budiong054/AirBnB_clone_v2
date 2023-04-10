#!/usr/bin/env bash
# Sets up your web servers for the deployment of web static

apt-get update
apt-get install nginx -y

DIR_1=/data/web_static/releases/test/
DIR_2=/data/web_static/shared/
SYMLINK_FILE=/data/web_static/current
html_content="<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>"

mkdir -p $DIR_1
mkdir -p $DIR_2
echo -e "$html_content" > "$DIR_1"index.html

if [ -L $SYMLINK_FILE ]
then
        unlink $SYMLINK_FILE
fi

ln -s $DIR_1 $SYMLINK_FILE
chown -R ubuntu:ubuntu /data/

printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index index.html index.htm;
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
    location /redirect_me {
        return 301 http://cuberule.com/;
    }
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-enabled/default

service nginx restart
