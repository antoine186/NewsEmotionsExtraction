#!/bin/sh

sudo systemctl daemon-reload
sudo systemctl start flaskapp
sudo systemctl enable flaskapp

sudo systemctl restart nginx
sudo systemctl start nginx
sudo systemctl enable nginx

cd /home/ubuntu/NewsEmotionsExtraction
sudo python3 -m venv venv

export FLASK_APP='ApplicationCore.app'
gunicorn -b 0.0.0.0:5000 ApplicationCore.app:app
