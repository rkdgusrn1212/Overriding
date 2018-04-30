#!/usr/bin/env python
#-*- coding: utf-8 -*-

import socket

class UDPNetwork:
    port = 10000

    def __init__(self):
        self.serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.serverSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.serverSock.bind(('', self.port))

        self.clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def __del__(self):
        self.serverSock.close()
        self.clientSock.close()

    def sendMsg(self, host, sendData):
        self.clientSock.sendto(sendData, (host, self.port))

    def receiveMsg(self):
        self.receiveData, self.receiveAddr = self.serverSock.recvfrom(1024)
        return self.receiveData, self.receiveAddr
