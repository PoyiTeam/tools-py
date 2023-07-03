import mysql.connector


host_address = "140.134.76.145"
port = 3306
mydb = mysql.connector.connect(
    host=host_address,
    port=port,
    user="AIoTLab-MySQL",
    password="db309-1"
)

print(mydb)
