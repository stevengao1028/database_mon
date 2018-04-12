# coding:utf8
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "database_mon.settings")
django.setup()

from socket import *
import sqlite3

db_name = "ora.sqlite3"
conn = sqlite3.connect(db_name)
cursor = conn.cursor()
table = "monitor_sysstat"

def save_to_db(data):
    sql_value=[]
    sql_value.append('\''+data['name']+'\'')
    sql_value.append('\''+data['time']+'\'')
    sql_value.append('\''+data['mem']['MemFree']+'\'')
    sql_value.append('\''+data['mem']['MemUsed']+'\'')
    sql_value.append('\''+data['mem']['MemTotal']+'\'')
    sql_value.append('\''+data['uptime']['day']+'\'')
    sql_value.append('\''+data['uptime']['hour']+'\'')
    sql_value.append('\''+data['uptime']['minute']+'\'')
    sql_value.append('\''+data['uptime']['Free rate']+'\'')
    sql_value.append('\''+data['cpu']['lcount']+'\'')
    sql_value.append('\''+data['cpu']['rate']+'\'')
    sql_value.append('\''+data['cpu']['pcount']+'\'')
    sql_value.append('\''+data['disk']['used']+'\'')
    sql_value.append('\''+data['disk']['total']+'\'')
    sql_value.append('\''+data['disk']['percent']+'\'')
    sql_value.append('\''+data['disk']['name']+'\'')
    sql_value.append('\''+data['disk']['free']+'\'')
    sql_value.append('\''+data['net'][0]['interface']+'\'')
    sql_value.append('\''+data['net'][0]['ReceiveBytes']+'\'')
    sql_value.append('\''+data['net'][0]['TransmitBytes']+'\'')
    sql_value.append('\''+data['net'][1]['interface']+'\'')
    sql_value.append('\''+data['net'][1]['ReceiveBytes']+'\'')
    sql_value.append('\''+data['net'][1]['TransmitBytes']+'\'')
    sql_value.append('\''+data['load']['lavg_1']+'\'')
    sql_value.append('\''+data['load']['lavg_5']+'\'')
    sql_value.append('\''+data['load']['lavg_15']+'\'')
    sql_value.append('\''+data['load']['last_pid']+'\'')
    insert_data_sql = 'INSERT INTO ' + table + ' VALUES (' + ",".join(sql_value)+')'
    print insert_data_sql
    try:
        cursor.execute(insert_data_sql)
        conn.commit()
        result = "sucessful"
    except Exception,e:
        result = e.message
    return result
def client():
    HOST = '192.168.42.178'
    PORT = 10521
    clientsocket = socket(AF_INET, SOCK_STREAM)
    clientsocket.connect((HOST, PORT))
    while True:
        data = clientsocket.recv(1024)
        save_data = eval(data)
        print type(save_data)
        result = save_to_db(save_data)
        print result
    clientsocket.close



if __name__ == "__main__":
    client()