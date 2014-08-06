#!/usr/bin/env python

import MySQLdb
import commands

#grab ip address
ip = commands.getoutput("/sbin/ifconfig").split("\n")[1].split()[1][5:]
print ip

#grab temp
temp = commands.getoutput("/opt/vc/bin/vcgencmd measure_temp")[5:-2]
print temp

#connect to database
db = MySQLdb.connect(host="192.168.0.111",user="root",passwd="drowssap",db="pi_cluster")

#create cursor
curs = db.cursor()

#insert into the log
curs.execute("INSERT INTO log (ip, message, temp) VALUES (%s, 'Test', %s)", (str(ip),str(temp),))

db.commit() 
