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
db_name = cfg['machine']
headers = cfg['headers']
rawdata_table_name = cfg['rawdata_table_name']

db = mysql.connector.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=db_name
)

cursor = db.cursor()

trigger_name = 'mytrigger'
sql = f'DROP TRIGGER IF EXISTS {trigger_name}'
cursor.execute(sql)
sql = f'CREATE TRIGGER {trigger_name} AFTER INSERT ON {rawdata_table_name} FOR EACH ROW'
cursor.execute(sql)
