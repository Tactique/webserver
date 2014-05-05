#!/bin/sh

function usage() {
	echo "either supply no arguments or \"deps\""
}

function syncdb() {
	python manage.py syncdb --noinput
}

function install_deps() {
	sudo pip install -r requirements.txt
}

function main() {
	if [ $# -lt 1 ]; then
		syncdb
	else
		if [ $1 == 'deps' ]; then
			install_deps
		else
			usage
		fi
	fi
}

main $@
