import pynuodb
 
connection = pynuodb.connect("test", "localhost", "dba", "goalie", options={'schema':'hockey'})
# Do something with your connection
cursor = connection.cursor()
cursor.arraysize = 3
cursor.execute("select * from hockey")
print cursor.fetchone()
print cursor.fetchone()
print cursor.fetchone()
print cursor.fetchone()
print cursor.fetchone()
connection.close()