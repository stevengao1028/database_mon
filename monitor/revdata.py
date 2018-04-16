# coding:utf8
import MySQLdb
from socket import *
# import logging
import sys
import json
# logging.getLogger('socket').setLevel(logging.DEBUG)
# logging.basicConfig()
sql_con=0
while sql_con==0:
    try:
        db = MySQLdb.connect("127.0.0.1", "root", "123456", "ora", charset='utf8' )
        cursor = db.cursor()
        sql_con=1
    except:
        pass
log_table = "monitor_sysstat"


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
    insert_data_sql = 'INSERT INTO ' + log_table + ' VALUES (\'1\',' + ",".join(sql_value)+')'
    # print insert_data_sql
    try:
        cursor.execute(insert_data_sql)
        db.commit()
    except MySQLdb.Error,e:
        pass
        # print 'Error %d: %s' % (e.args[0], e.args[1])


def client(host):
    HOST = host
    PORT = 10521
    is_con=0
    while is_con==0:
        try:
            clientsocket = socket(AF_INET, SOCK_STREAM)
            clientsocket.connect((HOST, PORT))
            is_con=1
        except:
            clientsocket.close
    while True:
        try:
            clientsocket.send("ok")
            data = clientsocket.recv(10240)
        except:
            client(host)
        print data
        print type(json.loads(data))
        # save_data = eval(data)
        # save_to_db(save_data)
    clientsocket.close


if __name__ == "__main__":
    if sys.argv[1]:
        print sys.argv[1]
        client(sys.argv[1])
