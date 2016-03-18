#!/bin/bash
# This script for setting up environment
DJANGO_CONFIGURATION=alex
export DJANGO_CONFIGURATION

# Install dependences
pip install -r requirements/dev.txt

# Drop old database
if
! dropdb -U postgres -h db gather_prov
then
echo "Notice: gather_prov db wasn't drop."
fi

# Create new database
createdb -U postgres -h db gather_prov

# Set up database
# ./manage.py syncdb
./manage.py migrate
fab i18n:action=compile,domain=python,locale=zh_CN
fab i18n:action=compile,domain=js,locale=zh_CN
fab i18n:action=compile,domain=python,locale=zh_TW
fab i18n:action=compile,domain=js,locale=zh_TW
fab i18n:action=compile,domain=python,locale=hi
fab i18n:action=compile,domain=js,locale=hi
fab i18n:action=compile,domain=js,locale=en
./manage.py resass

# Run server
./manage.py runserver 0.0.0.0:8000
