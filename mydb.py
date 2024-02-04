import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost', user='root',
    password='',
    database='mydata',
)
if dataBase.is_connected():
    print("connected")
else:
    print("not connected")
# prepare a cursor object
cousorObject = dataBase.cursor()

# create a database

#cousorObject.execute("CREATE table sno")

print("All done!")
