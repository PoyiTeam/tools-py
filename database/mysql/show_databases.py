import mysql.connector
import json


cfg_path = 'cfg.json'

with open(cfg_path) as file:
    cfg = json.load(file)

host = cfg['host']
port = cfg['port']
user = cfg['user']
password = cfg['password']

db = mysql.connector.connect(
    host=host,
    port=port,
    user=user,
    password=password
)

cursor = db.cursor()
cursor.execute("SHOW DATABASES")

for x in cursor:
    print(x)