import pynuodb
import csv
 
connection = pynuodb.connect("test", "localhost", "dba", "goalie", options={'schema':'hockey'})
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS ACTOR")
sql = """CREATE TABLE ACTOR (
         ID int NOT NULL AUTO_INCREMENT primary key,
         NAME 		VARCHAR(60),
         MOVIE   	VARCHAR(150))"""
cursor.execute(sql)

with open('actors.csv', 'rb') as csvfile:
	actorReader = csv.reader(csvfile, delimiter=',')
	for row in actorReader:
		actor_val=(row[0]+" "+row[1], row[2])
		cursor.execute("INSERT INTO ACTOR VALUES (?,?)", actor_val)

cursor.execute("SELECT * FROM ACTOR")
print cursor.fetchone()

connection.close()