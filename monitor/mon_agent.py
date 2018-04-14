# !/usr/bin/env python
# -*- coding: UTF-8 -*-
import psutil
import os
from socket import *
import time
from datetime import datetime

last_worktime=0
last_idletime=0

class sys_info:
    def __init__(self):
        self.data = {}

    def host_name(self):
        host=os.popen('echo $HOSTNAME').read().rstrip('\n')
        return host

    def host_time(self):
        now_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return now_time


    def cpu_info(self):
        cpu={}
        # cpu['rate']=str(psutil.cpu_percent())
        # cpu['lcount']=str(psutil.cpu_count())
        # cpu['pcount']=str(psutil.cpu_count(logical=False))
        # cpu['times']=str(psutil.cpu_times())
        cpu['pcount']= os.popen('cat /proc/cpuinfo |grep "physical id"|sort |uniq|wc -l').read().rstrip('\n')
        cpu['lcount']= os.popen('cat /proc/cpuinfo |grep "processor"|wc -l').read().rstrip('\n')
        cpu['rate'] = "10"
        global last_worktime, last_idletime
        f = open("/proc/stat", "r")
        line = ""
        while not "cpu " in line: line = f.readline()
        f.close()
        spl = line.split(" ")
        worktime = int(spl[2]) + int(spl[3]) + int(spl[4])
        idletime = int(spl[5])
        dworktime = (worktime - last_worktime)
        didletime = (idletime - last_idletime)
        rate = float(dworktime) / (didletime + dworktime)
        last_worktime = worktime
        last_idletime = idletime
        if (last_worktime == 0): cpu['rate'] = "0"
        cpu['rate'] = str(round(rate))
        return cpu

    def memory_info(self):
        mem = {}
        f = open("/proc/meminfo")
        lines = f.readlines()
        f.close()
        for line in lines:
            if len(line) < 2: continue
            elif line.split(':')[0] in ['MemTotal','MemFree','MemAvailable','SwapTotal','SwapFree','Buffers','Cached']:
                name = line.split(':')[0]
                var = str(int(line.split(':')[1].split()[0]) / 1024)
                mem[name] = var
        mem['MemUsed'] = str(int(mem['MemTotal']) - int(mem['MemFree']) - int(mem['Buffers']) - int(mem['Cached']))
        return mem


    def load_info(self):
        loadavg = {}
        f = open("/proc/loadavg")
        con = f.read().split()
        f.close()
        loadavg['lavg_1']= con[0]
        loadavg['lavg_5']= con[1]
        loadavg['lavg_15']= con[2]
        # loadavg['nr']=con[0]
        loadavg['last_pid']= con[4]
        return loadavg


    def uptime_info(self):
        uptime = {}
        f = open("/proc/uptime")
        con = f.read().split()
        f.close()
        all_sec = float(con[0])
        MINUTE,HOUR,DAY = 60,3600,86400
        uptime['day'] = str(all_sec / DAY )
        uptime['hour'] = str((all_sec % DAY) / HOUR)
        uptime['minute'] = str((all_sec % HOUR) / MINUTE)
        uptime['second'] = str(all_sec % MINUTE)
        uptime['Free rate'] = str(float(con[1]) / float(con[0]))
        return uptime

    def net_info(self):
        net = []
        f = open("/proc/net/dev")
        lines = f.readlines()
        f.close()
        for line in lines[2:]:
            con = line.split()
            intf = {}
            intf['interface'] = con[0].lstrip(":")
            intf['ReceiveBytes'] = con[1]
            intf['TransmitBytes'] = con[9]
            net.append(intf)
        return net

    def disk_info(self,diskname):
        hd={}
        disk = os.statvfs(diskname)
        hd['name'] = diskname
        hd['total'] = str(disk.f_frsize * disk.f_blocks/(1024*1024*1024))
        hd['free'] = str(disk.f_frsize * disk.f_bfree/(1024*1024*1024))
        hd['used'] = str((disk.f_frsize * disk.f_blocks-disk.f_frsize * disk.f_bfree)/(1024*1024*1024))
        hd['percent'] = str(round((disk.f_frsize * disk.f_blocks-disk.f_frsize * disk.f_bfree)* 100.0 /disk.f_frsize * disk.f_blocks))
        return hd

    def all_info(self):
        self.data['name'] = self.host_name()
        self.data['time'] = self.host_time()
        self.data['cpu']=self.cpu_info()
        self.data['disk']=self.disk_info("/")
        self.data['mem']=self.memory_info()
        self.data['uptime']=self.uptime_info()
        self.data['net']=self.net_info()
        self.data['load']=self.load_info()
        return self.data


def server():
    HOST = ''
    PORT = 10521
    ADDR = (HOST, PORT)
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(ADDR)
    server_socket.listen(5)
    tcpclientsocket, addr = server_socket.accept()
    while True:
        send_info = sys_info()
        data = repr(send_info.all_info())
        try:
            tcpclientsocket.recv(1024)
            tcpclientsocket.send(data)
        except:
            tcpclientsocket, addr = server_socket.accept()
        print data
        time.sleep(5)
    tcpclientsocket.close()
    server_socket.close()

if __name__ == "__main__":
    server()