#!/usr/bin/env bash

if [[ -d "venv" ]]; then
    source venv/bin/activate
else
    python3 -m venv venv
    source venv/bin/activate
fi
pip install flask
pip freeze > requirements.txt
source env.sh

mkdir -p ./app/static/css
mkdir -p ./app/static/images
mkdir -p ./app/templates
mkdir -p ./app/auth

touch ./main.py

touch ./app/config.py
touch ./app/firestore_service.py
touch ./app/forms.py
touch ./app/models.py
touch ./app/__init__.py

touch ./app/auth/__init__.py
touch ./app/auth/viewa.py
touch ./app/templates/templates.py
