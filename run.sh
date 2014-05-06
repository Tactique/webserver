#!/bin/bash

pushd $(dirname $0) > /dev/null

pkill python

./manage.py runserver 0.0.0.0:8000 &

popd > /dev/null
