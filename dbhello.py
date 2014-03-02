import pynuodb
# Initialize database connection
connection = pynuodb.connect("test", "localhost", "dba", "goalie", options={'schema':'hello'})
cursor = connection.cursor()
# Creates a schema "hello" and a table "accounts" with three columns
def createTable():
    try:
        cursor.execute("create schema hello")
        cursor.execute("create table accounts (id int primary key, name string, balance int)")
    except:
        print "Table already exists"
# Inserts data from a pre-populated array
def insertData():
    try:
        idArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        nameArray = ["Sarah", "Carl", "Sophia", "John", "Maya", "Will", "Laura", "David", "Lily", "Chris", "Emily", "Matt", "Zoe", "Dan", "Mia"]
        accountBalance = [15000, 70000, 8000, 2000, 90000, 40000, 100000, 20000, 11000, 55000, 63000, 10000, 1500, 6000, 47000]
        i=1
        while(i <= 15):
            cursor.execute("insert into accounts values (?, ?, ?)", (i, nameArray[i-1], accountBalance[i-1]))
            str(accountBalance[i-1]);
            i+=1
    except:
        print "Data already exists"
    # Commiting insertions into the database
    connection.commit();
def getName(i):
    n = cursor.execute("select name from accounts where id=" + str(i))
    name = (cursor.fetchone())[0]
    return name
def getBalance(i):
    b = cursor.execute("select balance from accounts where id=" + str(i))
    balance = (cursor.fetchone())[0]
    return str(balance)

if __name__ == '__main__':
    createTable()
    insertData()
    i = 1
    while(i <= 15):
        print getName(i) + ": \n Account ID = " + str(i) + "\n Balance = " + getBalance(i) + "\n"
        i += 1