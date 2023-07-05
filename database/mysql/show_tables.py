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
)

cursor = db.cursor()

sql = 'USE dummy_machine'
cursor.execute(sql)

sql = 'SHOW TABLES'
cursor.execute(sql)

for x in cursor:
    print(x)
