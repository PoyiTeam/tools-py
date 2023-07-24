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

column_name = 'start_time'
sql = f'SELECT {column_name} FROM {rawdata_table_name} WHERE {column_name}=(SELECT MAX({column_name}) FROM {rawdata_table_name})'
cursor.execute(sql)
field_names = cursor.description
result = cursor.fetchall()
print(f'target column name: {cursor.column_names[0]}')
print(f'element: {result[0][0]}')
