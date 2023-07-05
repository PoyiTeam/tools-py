import mysql.connector
import json


cfg_path = 'cfg.json'

with open(cfg_path) as file:
    cfg = json.load(file)

host = cfg['host']
port = cfg['port']
user = cfg['user']
password = cfg['password']
db_name = cfg['machine']

db = mysql.connector.connect(
    host=host,
    port=port,
    user=user,
    password=password
)

cursor = db.cursor()
sql = f'CREATE DATABASE IF NOT EXISTS {db_name}'
cursor.execute(sql)
