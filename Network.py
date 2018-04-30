#!/usr/bin/env python
#-*- coding: utf-8 -*-

import subprocess

class Network:
    ipTable = {
               'MacAddress': 'localhost'
              }

    def updateIpTable(self, macAddress, ipAddress):
        ipTable[macAddress] = ipAddress

    def deleteIpTable(self, macAddress):
        del ipTable[macAddress]

    def viewNetwork(self):
        self.ifconfig = subprocess.check_output('ifconfig wlan0', shell = True).split('\n')
        self.iwconfig = subprocess.check_output('iwconfig wlan0', shell = True).split('\n')
        for msg in self.ifconfig:
            print msg
        for msg in self.iwconfig:
            print msg

    def batmanSetting(self):
        subprocess.call("./batmanSetting.sh", shell = True);
