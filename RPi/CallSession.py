#!/usr/bin/env python
#-*- coding: utf-8 -*-

import UDPNetwork
import Filter
import Audio
import Network
import threading

class CallSession:
    def __init__(self):
        self.udpNetwork = UDPNetwork.UDPNetwork()
        self.filter = Filter.Filter()
        self.audio = Audio.Audio()
        self.network = Network.Network()
        self.inputSwitch = 1
        self.outputSwitch = 1

    def __del__(self):
        del self.network
        del self.udpNetwork
        del self.filter
        del self.audio

    def audioInputThread(self):
        while True:
            self.inputAudio = self.audio.inputAudio()
            self.filtered = self.filter.filtering(self.inputAudio, 50.0)
            if self.filtered != None:
                for host in self.network.ipTable.values():
                    self.udpNetwork.sendMsg(host, self.filtered)
            if self.inputSwitch != 1:
                break

    def audioOutputThread(self):
        while True:
            self.outputAudio, self.outputAddr = self.udpNetwork.receiveMsg()
            self.audio.outputAudio(self.outputAudio)
            print self.outputAddr
            if self.outputSwitch != 1:
                break

    def run(self):
        self.t1 = threading.Thread(target = self.audioInputThread)
        self.t2 = threading.Thread(target = self.audioOutputThread)
        self.t1.daemon = True
        self.t2.daemon = True
        self.t1.start()
        self.t2.start()

    def runOff(self):
        self.inputSwitch = 0
        self.outputSwitch = 0
