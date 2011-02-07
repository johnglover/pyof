# Copyright (c) 2010 John Glover, National University of Ireland, Maynooth
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

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

