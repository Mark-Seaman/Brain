#!/bin/bash
# Execute the system scripts

cd $pa && 

./manage.py runscript devtest    &&
./manage.py runscript initialize &&

echo 'Scripts run successfully'
