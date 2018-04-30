#!/usr/bin/env python
#-*- coding: utf-8 -*-

import audioop
import math

class Filter:
    def rms(self, data):
        return audioop.rms(data, 2)

    def decibel(self, rms):
        return math.log10(rms) * 20

    def filtering(self, data, threshold):
        self.rmsData = self.rms(data)
        self.dB = self.decibel(self.rmsData)

        if self.dB > threshold:
            return data
        else:
            return None
