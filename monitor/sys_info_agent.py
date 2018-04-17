# !/usr/bin/env python
# -*- coding: UTF-8 -*-
import commands
from socket import *
import time
import json
from datetime import datetime


def exe_command(exe_cmd):
    (status,output)=commands.getstatusoutput(exe_cmd)
    result={'status':str(status),'info':output}
    return result


def base_info():
    sys_info={'loadaverage':"",'uptime':"",'totaltask':"",'running':"",'sleeping':"",'stopped':"",'zombie':"", \
              'cpuus':"",'cpusy':"",'cpyni':"",'cpuid':"",'cpuwa':"",'cpuhi':"",'cpusi':"",'cpust':"",'memtotal':"",\
              'memfree':"",'memused':"",'memcache':"",'swaptotal':"",'swapfree':"",'swapused':"",'swapcache':"",\
              'hostname':"",'cpu_pcount':"",'cpu_lcount':"",'version':"",'disks':"",'ports':""}
    disks=[]
    netports=[]
    top_cmd = "top  -n 1 -bi"
    top_result = exe_command(top_cmd)
    if top_result['status'] == "0":
        for line in top_result['info'].split('\n'):
            if line.startswith("top ") and len(line.split("load average:"))==2:
                sys_info['loadaverage'] = line.split("load average:")[1]
                sys_info['uptime'] = line.split("load average:")[0].split(",")[0].lstrip("top -")
            if line.startswith("Tasks:") and len(line.split(","))==5:
                sys_info['totaltask'] = line.split(",")[0].lstrip("Tasks:").rstrip("total").strip()
                sys_info['running'] = line.split(",")[1].rstrip("running").strip()
                sys_info['sleeping'] = line.split(",")[2].rstrip("running").strip()
                sys_info['stopped'] = line.split(",")[3].rstrip("stopped").strip()
                sys_info['zombie'] = line.split(",")[4].rstrip("zombie").strip()
            if line.startswith("%Cpu(s)")  and len(line.split(","))==8:
                sys_info['cpuus'] = line.split(",")[0].lstrip("%Cpu(s):").rstrip("us").strip()
                sys_info['cpusy'] = line.split(",")[1].rstrip("sy").strip()
                sys_info['cpyni'] = line.split(",")[2].rstrip("ni").strip()
                sys_info['cpuid'] = line.split(",")[3].rstrip("id").strip()
                sys_info['cpuwa'] = line.split(",")[4].rstrip("wa").strip()
                sys_info['cpuhi'] = line.split(",")[5].rstrip("hi").strip()
                sys_info['cpusi'] = line.split(",")[6].rstrip("si").strip()
                sys_info['cpust'] = line.split(",")[7].rstrip("st").strip()
            if line.startswith("KiB Mem") and len(line.split(","))==4:
                sys_info['memtotal'] = line.split(",")[0].lstrip("KiB Mem :").rstrip("total").strip()
                sys_info['memfree'] = line.split(",")[1].rstrip("free").strip()
                sys_info['memused'] = line.split(",")[2].rstrip("used").strip()
                sys_info['memcache'] = line.split(",")[3].rstrip("buff/cache").strip()
            if line.startswith("KiB Swap") and len(line.split(","))==3:
                sys_info['swaptotal'] = line.split(",")[0].lstrip("KiB Swap:").rstrip("total").strip()
                sys_info['swapfree'] = line.split(",")[1].rstrip("free").strip()
                if len(line.split(",")[2].split('.')) ==2:
                    sys_info['swapused'] = line.split(",")[2].split('.')[0].rstrip("used").strip()
                    sys_info['swapcache'] = line.split(",")[2].split('.')[1].rstrip("avail Mem").strip()
    sys_info['now_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    host_cmd = "echo $HOSTNAME"
    host_result = exe_command(host_cmd)
    if host_result['status'] == "0":
        sys_info['hostname'] = host_result['info']
    cpu_pcount_cmd = """cat /proc/cpuinfo |grep "physical id"|sort |uniq|wc -l"""
    cpu_pcount_result = exe_command(cpu_pcount_cmd)
    if cpu_pcount_result['status'] == "0":
        sys_info['cpu_pcount'] = cpu_pcount_result['info']
    cpu_lcount_cmd = """cat /proc/cpuinfo |grep "processor"|wc -l"""
    cpu_lcount_result = exe_command(cpu_lcount_cmd)
    if cpu_lcount_result['status'] == "0":
        sys_info['cpu_lcount'] = cpu_lcount_result['info']
    version_cmd = "cat /proc/version"
    version_result = exe_command(version_cmd)
    if version_result['status'] == "0":
        sys_info['version'] = version_result['info']
    disk_cmd = """df -h |awk '$1!~/Filesystem/{print $1,$2,$5}'"""
    disk_result = exe_command(disk_cmd)
    if disk_result['status'] == "0":
        disks.append('\''+sys_info['now_time']+'\'')
        for line in disk_result['info'].split('\n'):
            disks.append('\''+line+'\'')
        sys_info['disks'] = disks
    port_cmd = """cat /proc/net/dev |awk '{print $1,$2,$10}' |sed '/Inter/d;/face/d'"""
    port_result = exe_command(port_cmd)
    if port_result['status'] == "0":
        netports.append('\'' + sys_info['now_time'] + '\'')
        for line in port_result['info'].split('\n'):
            netports.append('\''+line+'\'')
        sys_info['ports'] = netports
    result = sys_info
    return result



def server():
    HOST = ''
    PORT = 10521
    ADDR = (HOST, PORT)
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(ADDR)
    server_socket.listen(5)
    tcpclientsocket, addr = server_socket.accept()
    while True:
        data = base_info()
        try:
            tcpclientsocket.recv(1024)
            tcpclientsocket.send(json.dumps(data))
        except:
            tcpclientsocket, addr = server_socket.accept()
        print data
        time.sleep(5)
    tcpclientsocket.close()
    server_socket.close()

if __name__ == "__main__":
    server()
