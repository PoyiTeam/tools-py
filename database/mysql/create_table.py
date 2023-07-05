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
sql = f'CREATE TABLE IF NOT EXISTS {rawdata_table_name} ({headers[0]} VARCHAR(255), {headers[1]} VARCHAR(15), {headers[2]} VARCHAR(255))'
cursor.execute(sql)
