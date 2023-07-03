import mysql.connector
import json


cfg_path = 'cfg.json'

with open(cfg_path) as file:
    cfg = json.load(file)

host = cfg['host']
port = cfg['port']
user = cfg['user']
password = cfg['password']
database = cfg['task']

database = mysql.connector.connect(
    host=host,
    port=port,
    user=user,
    password=password
)

cursor = database.cursor()

cursor.execute(f'CREATE DATABASE IF NOT EXISTS {database}')
cursor.execute(
    'CREATE TABLE IF NOT EXISTS rawdata (name VARCHAR(255), address VARCHAR(255))')
