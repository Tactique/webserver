#!/bin/sh

python manage.py syncdb
python manage.py SeedDB
python manage.py ImportTemplates
