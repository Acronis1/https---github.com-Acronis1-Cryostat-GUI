import sys
import datetime
import pickle
import os
import mysql.connector

#does not support adding new key-value pairs in the dictionary, the number of columns must be manually set with "{}" in ALTER DATA, before logging the data/running!

#logging in:
try:
	mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="1234",
	auth_plugin='mysql_native_password',
	database="test"
	)
except mysql.connect.Error as err:
	print("Couldn't establish connection {}".format(err))


#cursor setup:
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS test")


#Optional command to delete a table, must be commented out
mycursor.execute("DROP TABLE measured_data")


#test dict:
testdict={
	"Voltage":"10",
	"Current" :"40",
	"Temperature":"80",
	"Testcol1":10,
	"Testcol2":20
}
#initializing a table with primary key as first column:
mycursor.execute("CREATE TABLE IF NOT EXISTS measured_data (id INT AUTO_INCREMENT PRIMARY KEY)")


#this should be turned off after the setup, but now handled with exception, it wants to overwirte existing columns but can't do so!
try:
	sql="ALTER TABLE measured_data ADD ({} FLOAT(7,4),{} FLOAT(7,4),{} FLOAT(7,4),{} FLOAT(7,4),{} FLOAT(7,4))" .format(*list(testdict.keys()))
	mycursor.execute(sql)

except mysql.connector.errors.ProgrammingError as er:
	print("Column name already exists don't worry (see line 41)")


#inserting in the measured values:
sql="INSERT INTO measured_data ({},{},{},{},{}) VALUES ({},{},{},{},{})" .format(*list(testdict.keys()),*list(testdict.values()))
mycursor.execute(sql)


#updateing the database with the entries:
mydb.commit()



#formatting the header/column names, won't be nice, but usable:
print("({},{},{},{},{},{})".format('id',*list(testdict.keys())))


#printing out the current entries
mycursor.execute("SELECT * from measured_data")
data =mycursor.fetchall()
for row in data:
	print(row)

