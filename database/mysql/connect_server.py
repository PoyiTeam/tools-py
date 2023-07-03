import mysql.connector
import json


cfg_path = 'cfg.json'

with open(cfg_path) as file:
    cfg = json.load(file)

host = cfg['host']
port = cfg['port']
user = cfg['user']
password = cfg['password']

mydb = mysql.connector.connect(
    host=host,
    port=port,
    user=user,
    password=password
)

print(mydb)
