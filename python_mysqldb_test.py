#!/usr/bin/env python

import MySQLdb
import commands

#grab ip address
ip = commands.getoutput("/sbin/ifconfig").split("\n")[1].split()[1][5:]
print ip

#connect to database
db = MySQLdb.connect(host="192.168.0.111",user="root",passwd="drowssap",db="pi_cluster")

#create cursor
curs = db.cursor()

#insert into the log
curs.execute("INSERT INTO log (ip, message) VALUES (%s, 'Test')", (str(ip),))

db.commit() 
