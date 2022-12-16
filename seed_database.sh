#!/bin/bash

rm db.sqlite3
rm -rf ./totspotapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations totspotapi
python3 manage.py migrate totspotapi
python3 manage.py loaddata users
python3 manage.py loaddata allergies
python3 manage.py loaddata parents
python3 manage.py loaddata children
python3 manage.py loaddata posts
python3 manage.py loaddata comments
python3 manage.py loaddata providers