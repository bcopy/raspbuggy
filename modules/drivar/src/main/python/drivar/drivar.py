## @package drivar
#  Driver library for Blockars
'''
Created on Mar 18, 2015

@author: bcopy
'''
import time
import pibrella

class Drivar:
    running = False
    
    def left(self, durationInMs,callback = None):
        durationInMs = max(durationInMs,100)
        self.running = True
        pibrella.output.e.on()
        pibrella.output.f.on()
        time.sleep(durationInMs/1000)
        pibrella.output.e.off()
        pibrella.output.f.off()
        self.running = False
        if callback is not None:
            callback()
      
    def right(self, durationInMs,callback = None):
        durationInMs = max(durationInMs,100)
        self.running = True
        pibrella.output.g.on()
        pibrella.output.h.on()
        time.sleep(durationInMs/1000)
        pibrella.output.g.off()
        pibrella.output.h.off()
        self.running = False
        if callback is not None:
            callback()
        
    def forward(self, durationInMs,callback = None):
        durationInMs = max(durationInMs,100)
        self.running = True
        pibrella.output.on()
        time.sleep(durationInMs/1000)
        pibrella.output.off()
        self.running = False
        if callback is not None:
            callback()
       
drivar = Drivar()
