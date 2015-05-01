## @package drivar
#  Driver library for Raspbuggy
'''
Created on Mar 18, 2015

@author: bcopy
'''
from abc import ABCMeta,abstractmethod
import time



class Drivar(object):
    __metaclass__ = ABCMeta

    DIR_FORWARD = 0x01
    DIR_BACKWARD = 0x02
    
    DIR_LEFT = 0x04
    DIR_RIGHT = 0x08
    
    WHEELS_RIGHT = 0x01
    WHEELS_LEFT = 0x02
    WHEELS_BOTH = 0x04
    
    SPEED_SLOW = 0x01
    SPEED_MEDIUM = 0x02
    SPEED_FAST = 0x04
    
    @abstractmethod
    def initialize(self):
        pass


