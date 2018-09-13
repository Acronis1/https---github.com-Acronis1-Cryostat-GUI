import sys
import os
import sqlite3

#hmm
#does not support adding new key-value pairs in the dictionary, the number of columns must be manually set with "{}" in ALTER DATA, before logging the data/running!

#creating db:
try:
	conn = sqlite3.connect('measured_data')
except sqlite3.connect.Error as err:
	print("Couldn't establish connection {}".format(err))


#cursor setup:
mycursor = conn.cursor()



#Optional command to delete a table, must be commented out
#mycursor.execute("DROP TABLE measured_data")


#test dict:
testdict={
	"Voltage":"500",
	"Current" :"20",
	"Temperature":"80",
	"Testcol1":10,
	"Testcol2":5
}

#initializing a table with primary key as first column:

mycursor.execute("CREATE TABLE IF NOT EXISTS measured_data (id INTEGER PRIMARY KEY,{} FLOAT(7,4),{} FLOAT(7,4),{} FLOAT(7,4),{} FLOAT(7,4),{} FLOAT(7,4))".format(*list(testdict.keys())))

conn.commit()

#inserting in the measured values:

sql="INSERT INTO measured_data ({},{},{},{},{}) VALUES ({},{},{},{},{})" .format(*list(testdict.keys()),*list(testdict.values()))
mycursor.execute(sql)


#updateing the database with the entries:
conn.commit()



#formatting the header/column names, won't be nice, but usable:
print("({},{},{},{},{},{})".format('id',*list(testdict.keys())))


#printing out the current entries
mycursor.execute("SELECT * from measured_data")
data =mycursor.fetchall()
for row in data:
	print(row)



