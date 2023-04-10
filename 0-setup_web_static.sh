#!/usr/bin/env bash
# Sets up your web servers for the deployment of web static
sudo apt-get update

sudo apt-get install nginx -y

DIR_1=/data/web_static/releases/test/
DIR_2=/data/web_static/shared/
SYMLINK_FILE=/data/web_static/current
html_content="<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>"

sudo mkdir -p $DIR_1

sudo mkdir -p $DIR_2

echo -e "$html_content" > "$DIR_1"index.html

if [ -L $SYMLINK_FILE ]
then
        sudo unlink $SYMLINK_FILE
fi

sudo ln -s $DIR_1 $SYMLINK_FILE

sudo chown -R ubuntu:ubuntu /data/

new_config="server_name \_\;\n\tlocation \/hbnb_static \{\n\t\talias \/data\/web\_static\/current\/\;\n\t\}\n"

sed -i "s/server_name _;/$new_config/" /etc/nginx/sites-enabled/default

sudo service nginx restart
