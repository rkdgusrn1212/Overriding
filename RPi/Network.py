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
        try:
            self.ifconfig = subprocess.check_output('ifconfig wlan1', shell = True).split('\n')
            for msg in self.ifconfig:
                print msg

            self.iwconfig = subprocess.check_output('iwconfig wlan1', shell = True).split('\n')
            for msg in self.iwconfig:
                print msg
        except:
            print "wlan1 off"

        try:
            self.ifconfig = subprocess.check_output('ifconfig bat0', shell = True).split('\n')
            for msg in self.ifconfig:
                print msg

            subprocess.check_output('sudo batctl o', shell = True)
        except:
            print "bat0 off"


    def batmanSetting(self, ipAddress, subnet, essid, channel):
        try:
            subprocess.check_output('sudo ifconfig bat0 down', shell = True)
        except:
            print "bat0 off"
        subprocess.check_output('sudo ifconfig wlan1 down', shell = True)

        self.string = 'sudo iwconfig wlan1 mode ad-hoc essid ' + essid + ' channel ' + str(channel)
        subprocess.check_output(self.string, shell = True)
        subprocess.check_output('sudo ifconfig wlan1 up', shell = True)
        print "Setting: wlan1"
        print "\tmode:\tad-hoc"
        print "\tessid:\t" + essid
        print "\tchannel:\t" + str(channel)

        subprocess.check_output('sudo modprobe batman-adv', shell = True)
        subprocess.check_output('sudo batctl if add wlan1', shell = True)

        self.string = 'sudo ifconfig bat0 ' + ipAddress + '/' + str(subnet)
        subprocess.check_output(self.string, shell = True)
        subprocess.check_output('sudo ifconfig bat0 up', shell = True)
        print "Setting: bat0"
        print "\tIP:\t" + ipAddress + "/" + str(subnet)
        print ""

        print "Complete."
