import mysql.connector
import mysql.connector.cursor
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
rawdata_table_name = cfg['rawdata_table_name']
headers = cfg['headers']

db = mysql.connector.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=db_name,
)

cursor = db.cursor()

sql = f'USE {db_name}'
cursor.execute(sql)

sql = (f'INSERT INTO {rawdata_table_name} '
       f'({headers[0]}, {headers[1]}, {headers[2]}) '
       'VALUES (%s, %s, %s)')
timestamp = datetime.now().strftime("%Y%m%dT%H%M%S")
val = ('dummy_task', timestamp, './dummy/directory')
cursor.execute(sql, val)
db.commit()
