import mysql.connector
import json


cfg_path = 'cfg.json'

with open(cfg_path) as file:
    cfg = json.load(file)

host = cfg['host']
port = cfg['port']
user = cfg['user']
password = cfg['password']
db_name = cfg['dummy_machine']

db = mysql.connector.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=db_name,
)

cursor = db.cursor()

cursor.execute('SHOW TABLES')
for x in cursor:
    print(x)
