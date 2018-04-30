#!/usr/bin/env python
#-*- coding: utf-8 -*-

import pyaudio

class Audio:
    CHUNK = 512
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.inputStream = self.p.open(format = Audio.FORMAT,
                                       channels = Audio.CHANNELS,
                                       rate = Audio.RATE,
                                       input = True,
                                       frames_per_buffer = Audio.CHUNK)
        self.outputStream = self.p.open(format = Audio.FORMAT,
                                        channels = Audio.CHANNELS,
                                        rate = Audio.RATE,
                                        output = True,
                                        frames_per_buffer = Audio.CHUNK)

    def __del__(self):
        self.outputStream.stop_stream()
        self.outputStream.close()
        self.inputStream.stop_stream()
        self.inputStream.close()
        self.p.terminate()

    def inputAudio(self):
        return self.inputStream.read(Audio.CHUNK)

    def outputAudio(self, data):
        self.outputStream.write(data)
