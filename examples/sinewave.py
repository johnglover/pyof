# Copyright (c) 2010 John Glover
# 
# Based on code by Daniel Shiffman (http://www.shiffman.net)

from openframeworks import *
import math

class SineWaveApp(ofBaseApp):
    def setup(self):
        ofBackground(255, 255, 255)
        ofSetFrameRate(25)
        ofEnableAlphaBlending()
        ofEnableSmoothing()
        # distance between each horizontal point (in pixels)
        self.x_spacing = 5
        # width of the wave
        self.wave_width = ofGetWidth()
        # current angle
        self.theta = 0.0
        # wave period (pixels)
        self.period = ofGetWidth() / 2.0
        # x increment
        self.dx = (2.0 * math.pi * self.x_spacing) / self.period 
        # maximum amplitude of the wave
        self.max_amplitude = (ofGetHeight() / 2.0) * 0.75
        # current amplitude values
        self.amplitudes = [0.0 for _ in range(self.wave_width / self.x_spacing)]
        
    def update(self):
        self.theta += 0.02
        x = self.theta
        c = (self.wave_width / 2)
        for i in range(len(self.amplitudes)):
            self.amplitudes[i] = c + (math.sin(x) * self.max_amplitude)
            x += self.dx
        
    def draw(self):
        ofBackground(255, 255, 255)
        ofFill()
        ofSetColor(0, 0, 0, 100)
        for i in range(len(self.amplitudes)):
            ofCircle(i*self.x_spacing, self.amplitudes[i], self.x_spacing*2)

if __name__ == "__main__":
    ofSetupOpenGL(500, 500, OF_WINDOW)
    ofRunApp(SineWaveApp())
