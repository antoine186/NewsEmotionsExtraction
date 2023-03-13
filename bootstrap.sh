#!/bin/sh

export FLASK_APP=ApplicationCore.application
export FLASK_ENV=development
python -m flask run

/bin/bash