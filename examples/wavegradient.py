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

# Based on code by Ira Greenberg (http://processing.org/learning/basics/wavegradient.html)

from openframeworks import *
import math

class WaveGradientApp(ofBaseApp):
    def setup(self):
        ofBackground(200, 200, 200)
        ofFill()
        frequency = 0
        amplitude = 30
        h = 100
        w = 100
        for i in range(-75, h + 75):
            # Reset angle to 0, so waves stack properly
            angle = 0
            # Increasing frequency causes more gaps
            frequency += .006
            for j in range(w + 75):
                py = i + math.sin(math.radians(angle)) * amplitude
                angle += frequency
                c = ofColor()
                c.r = abs(py - i) * 255 / amplitude
                c.g = 255 - abs(py - i) * 255 / amplitude
                c.b = j * (255.0 / (ofGetWidth() + 50))
                ofSetColor(int(c.r), int(c.g), int(c.b))
                # Hack to fill gaps. Raise value of fillGap if you increase frequency
                for filler in range(2):
                    ofCircle(int(j - filler), int(py) - filler, 1)
                    ofCircle(int(j), int(py), 1)
                    ofCircle(int(j + filler), int(py) + filler, 1)

        
if __name__ == "__main__":
    ofSetupOpenGL(500, 500, OF_WINDOW)
    ofRunApp(WaveGradientApp())

