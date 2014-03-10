#!/bin/bash

go run jswars/server.go -logpath=(pwd)/jswars.log &
python manage.py runserver
