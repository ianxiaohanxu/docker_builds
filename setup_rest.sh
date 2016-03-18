#!/bin/bash
# This script for setting up environment
DJANGO_CONFIGURATION=Slave_alex
export DJANGO_CONFIGURATION

PYTHONPATH="$PYTHONPATH:/root/python_modules"
export PYTHONPATH
# Install dependences
pip install -r requirements/dev.txt

# Drop old database
psql -U postgres -h db -c "create extension hstore" template1

if
! dropdb -U postgres -h db gather_rest
then
echo "Notice: gather_rest db wasn't drop."
fi

if 
! dropdb -U postgres -h db gather_demo
then
echo "Notice: gather_demo db wasn't drop."
fi

# Create new database
createdb -U postgres -h db gather_demo
createdb -U postgres -h db gather_rest

# Set up database
# ./manage.py syncdb
# ./manage.py syncdb --database=demo
./manage.py migrate
./manage.py migrate --database=demo

# Create superuser
expect create_super_user.sh

# Run server
./manage.py dev_reset
./manage.py runserver 0.0.0.0:8081

