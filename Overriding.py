#!/usr/bin/env python
#-*- coding: utf-8 -*-

import CallSession as cs
import Network
import time
import os

if __name__ == "__main__":
    audioInputOutput = cs.CallSession()
    network = Network.Network()
    callSwitch = 0

    # Ctrl - C 누르면 꺼지게 하려고 넣음. 의미 없음.
    while True:
        try:
            # time.sleep(100000)
            os.system('clear')
            print "1.\tView My Network Interface"
            print "2.\tGroup Call"
            print "3.\tNetwork Setting"
            print "4.\tExit"
            select = raw_input(">>> ")
            print ""

            if select == '1':   # View Network
                network.viewNetwork()
                raw_input()
            elif select == '2': # Group Call
                if callSwitch == 0:
                    print "Group Call - On"
                    audioInputOutput.run()
                    callSwitch = 1
                    raw_input()
                elif callSwitch == 1:
                    print "Group Call - Off"
                    audioInputOutput.runOff()
                    callSwitch = 0
                    raw_input()
            elif select == '3':
                network.batmanSetting();
                raw_input()
            elif select == '4': # Exit
                del network
                del audioInputOutput
                print "Turn off"
                break
            select = None
        except KeyboardInterrupt:
            del network
            del audioInputOutput
            print "Turn off"
            break
