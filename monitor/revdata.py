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
base_table = "sysstat"
disk_table = "diskstat"
net_table = "netstat"
ora_table = "ora"


def save_to_db(data):
    base_value=[]
    # disk_value=[]
    # port_value=[]
    base_value.append('\''+data['loadaverage']+'\'')
    base_value.append('\''+data['uptime']+'\'')
    base_value.append('\''+data['totaltask']+'\'')
    base_value.append('\''+data['running']+'\'')
    base_value.append('\''+data['sleeping']+'\'')
    base_value.append('\''+data['stopped']+'\'')
    base_value.append('\''+data['zombie']+'\'')
    base_value.append('\''+data['cpuus']+'\'')
    base_value.append('\''+data['cpusy']+'\'')
    base_value.append('\''+data['cpyni']+'\'')
    base_value.append('\''+data['cpuid']+'\'')
    base_value.append('\''+data['cpuwa']+'\'')
    base_value.append('\''+data['cpuhi']+'\'')
    base_value.append('\''+data['cpusi']+'\'')
    base_value.append('\''+data['cpust']+'\'')
    base_value.append('\''+data['memtotal']+'\'')
    base_value.append('\''+data['memfree']+'\'')
    base_value.append('\''+data['memused']+'\'')
    base_value.append('\''+data['memcache']+'\'')
    base_value.append('\''+data['swaptotal']+'\'')
    base_value.append('\''+data['swapfree']+'\'')
    base_value.append('\''+data['swapused']+'\'')
    base_value.append('\''+data['swapcache']+'\'')
    base_value.append('\''+data['hostname']+'\'')
    base_value.append('\''+data['cpu_pcount']+'\'')
    base_value.append('\''+data['cpu_lcount']+'\'')
    base_value.append('\'' + data['version'] + '\'')
    disk_value = data['disks']
    port_value = data['ports']
    insert_base_sql = 'INSERT INTO ' + base_table + ' VALUES (\'1\',' + ",".join(base_value)+')'
    insert_disk_sql = 'INSERT INTO ' + disk_table + ' VALUES (\'1\',' + ",".join(disk_value) + ')'
    insert_port_sql = 'INSERT INTO ' + net_table + ' VALUES (\'1\',' + ",".join(port_value) + ')'
    # print insert_base_sql
    # print insert_disk_sql
    # print insert_port_sql
    #base_insert
    try:
        cursor.execute(insert_base_sql)
        db.commit()
    except MySQLdb.Error,e:
        pass
        # print 'Error %d: %s' % (e.args[0], e.args[1])
    # disk_insert
    try:
        cursor.execute(insert_disk_sql)
        db.commit()
    except MySQLdb.Error,e:
        pass
    # port_insert
    try:
        cursor.execute(insert_port_sql)
        db.commit()
    except MySQLdb.Error,e:
        pass

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
        save_data = eval(data)
        save_to_db(save_data)
    clientsocket.close


if __name__ == "__main__":
    if sys.argv[1]:
        print sys.argv[1]
        client(sys.argv[1])
