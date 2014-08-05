#!/bin/bash

START_HERE="/home/pi/pi_cluster/";

cd $START_HERE;

git pull

echo "PULLED!";

GO_HERE="/home/pi/";

cd $GO_HERE

cp /home/pi/pi_cluster/bash_git.sh /home/pi/bash_git.sh

chmod 755 bash_git.sh

cd pi_cluster 
python python_mysqldb_test.py
