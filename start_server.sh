#!/bin/sh

sudo systemctl daemon-reload
sudo systemctl start flaskapp
sudo systemctl enable flaskapp

sudo systemctl restart nginx
sudo systemctl start nginx
sudo systemctl enable nginx

export FLASK_APP='ApplicationCore.app'
flask run --host=0.0.0.0
