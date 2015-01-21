#!/usr/bin/python
# -*- coding: utf-8 -*-
import Config
import time
import socket

udpsock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udpsock.sendto('%s:456789:123456:1' % (Config.MANAGE_PASS), (Config.MANAGE_BIND_IP, Config.MANAGE_PORT))
time.sleep(20)
udpsock.sendto('%s:456789:123456:0' % (Config.MANAGE_PASS), (Config.MANAGE_BIND_IP, Config.MANAGE_PORT))
