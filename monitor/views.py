# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.http import HttpResponse
from django.shortcuts import render
from monitor.models import *
from dwebsocket import require_websocket,accept_websocket


def revdata(request):
    if request.is_websocket():
        message =request.WebSocket.read()
        request.websocket.send("return: " + message)
        message = request.websocket.wait()
        if request.method == "POST":
            data = json.loads(request.body)
            try:
                MonitorSysstat.objects.create(host=data['name'],time=data['time'],mem_free=data['mem']['MemFree'],\
                       mem_used=data['mem']['MemUsed'],mem_total=data['mem']['MemTotal'],up_day=data['uptime']['day'],\
                       up_hour=data['uptime']['hour'],up_minute=data['uptime']['minute'],up_free=data['uptime']['Free rate'],\
                       cpu_count=data['cpu']['lcount'],cpu_rate=data['cpu']['rate'],cpu_pcount=data['cpu']['pcount'],\
                       disk1_used=data['disk']['used'],disk1_total=data['disk']['total'],disk1_percent=data['disk']['percent'],disk1_name=data['disk']['name'],disk1_free=data['disk']['free'],\
                       net_port1=data['net'][0]['interface'],net_port1_rec=data['net'][0]['ReceiveBytes'],net_port1_send=data['net'][0]['TransmitBytes'],\
                       net_port2=data['net'][1]['interface'],net_port2_rec=data['net'][1]['ReceiveBytes'],net_port2_send=data['net'][1]['TransmitBytes'],\
                       lovg_1= data['load']['lavg_1'],lavg_5=data['load']['lavg_5'],lavg_15= data['load']['lavg_15'],lavg_last_pid= data['load']['last_pid'])
            except Exception, e:
                print Exception,e.message
            return HttpResponse("ok")
        else:
            return render(request,'index.html')




