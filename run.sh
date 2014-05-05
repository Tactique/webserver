#!/bin/sh

pushd $(dirname $0) > /dev/null

pkill python

./manage.py runserver 0.0.0.0:8000 2>&1 > django.log &

popd > /dev/null
