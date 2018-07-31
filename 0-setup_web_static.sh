#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static.
sudo mkdir /data
sudo mkdir /data/web_static
sudo mkdir /data/web_static/releases
sudo mkdir /data/web_static/shared
sudo mkdir /data/web_static/releases/test
echo "Holberton School" | sudo tee -a /data/web_static/releases/test/index.html
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "45i location /hbnb_static/ {\nalias /data/web_static/current;\n}" /etc/nginx/sites-enabled/default
sudo service nginx restart
