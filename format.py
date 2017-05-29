import mysql.connector
import csv
file=open('sample.csv','r') 
db=mysql.connector.connect(user='name',password='passwd',host='localhost',database ='db')
mycursor=db.cursor()
for line in file:
        line = line.replace(",", " ")
        words =line.split()
        Query = """ INSERT INTO info VALUES (%s,%s,%s)"""
        mycursor.execute(Query, (words[0],words[1],words[2]))
        db.commit()
        

