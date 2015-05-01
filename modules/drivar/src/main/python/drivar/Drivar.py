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
    
## @package drivar
#  Driver library for Raspbuggy - Lego py-nxt implementation
'''
Created on Mar 18, 2015

@author: bcopy
'''

import nxt.locator
from nxt.motor import Motor,PORT_A,PORT_C
from nxt.sensor import Ultrasonic,PORT_4

from drivar.Drivar import Drivar
import time

class DrivarNxt(object):
    
    def __init__(self):
        self.m_initialized = False
        self.m_block = None
        self.m_leftMotor = None
        self.m_rightMotor = None
        self.m_ultrasonicSensor = None
        self.m_moving = False

    def initialize(self):
        self.m_block = nxt.locator.find_one_brick()
        self.m_leftMotor = Motor(self.m_block, PORT_A)
        self.m_rightMotor = Motor(self.m_block, PORT_C)
        self.m_ultrasonicSensor = Ultrasonic(self.m_block, PORT_4)
        self.m_initialized = True
        

    @abstractmethod
    def move(self, direction=Drivar.DIR_FORWARD,durationInMs=1000, callback = None):
        pass
    
    @abstractmethod
    def rotateWheels(self, wheelSet = Drivar.WHEELS_BOTH, direction = Drivar.DIR_FORWARD, speedLevel = Drivar.SPEED_FAST, callback = None):
        pass
    
    @abstractmethod
    def turn(self, direction = Drivar.DIR_LEFT, angle = 90):
        pass

    @abstractmethod
    def stop(self, callback = None):
        pass
 
    '''
      Return the distance to the nearest obstacle, in centimeters
    '''
    @abstractmethod
    def getDistanceToObstacle(self):
        pass
 
    '''
      Indicate with a boolean whether there is an obstacle within the given distance
    '''
    @abstractmethod
    def isObstacleWithin(self, distance):
        pass
        
    def wait(self, duration = 1000):
        time.sleep(duration)
        
    


