import mysql.connector
data="weatherdata" 
mydb = mysql.connector.connect(
	host="172.16.51.28",
	user="sois",
	password="Msois@123",
	database=str(data) 
)

mycursor = mydb.cursor()

mycursor.execute("Show tables;")

myresult = mycursor.fetchall()

for x in myresult:
	print(x)

