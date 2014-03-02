import pynuodb
import csv
 
connection = pynuodb.connect("test", "localhost", "dba", "goalie", options={'schema':'hockey'})
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
sql = """CREATE TABLE EMPLOYEE (
         ID int not null primary key,
         NAME 			VARCHAR(60),
         MOVIE   	VARCHAR(150))"""
cursor.execute(sql)

with open('actors.csv')
while 
employee_val=(123098, "NuoDB", "Admin", "215 First St", "Cambridge", "MA", 02142, 6175000001)
cursor.execute("INSERT INTO EMPLOYEE VALUES (?,?,?,?,?,?,?,?)", employee_val)
cursor.execute("SELECT * FROM EMPLOYEE")
print cursor.fetchone()

connection.close()