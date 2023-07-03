import mysql.connector
import json
from datetime import datetime


cfg_path = 'cfg.json'

with open(cfg_path) as file:
    cfg = json.load(file)

host = cfg['host']
port = cfg['port']
user = cfg['user']
password = cfg['password']
database = cfg['task']
table = datetime.now().strftime("%Y%m%dT%H%M%S")

database = mysql.connector.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=database,
)

cursor = database.cursor()
cursor.execute('SHOW TABLES')


for x in cursor:
    print(x)
