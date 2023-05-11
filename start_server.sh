#!/bin/sh

sudo tmux kill-server

sudo systemctl daemon-reload
sudo systemctl start flaskapp
sudo systemctl enable flaskapp

sudo systemctl restart nginx
sudo systemctl start nginx
sudo systemctl enable nginx

cd /home/ubuntu/NewsEmotionsExtraction
sudo python3 -m venv venv

tmux new -s flask_backend_session

export FLASK_APP='ApplicationCore.app'
flask run --host=0.0.0.0

exit N
