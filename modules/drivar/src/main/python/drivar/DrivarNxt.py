## @package drivar
#  Driver library for Raspbuggy - Lego py-nxt implementation
'''
Created on Mar 18, 2015

@author: bcopy
'''

import nxt.locator
from nxt.motor import *
from nxt.sensor import *
from drivar.Drivar import Drivar



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
        

    def move(self, direction=Drivar.DIR_FORWARD,durationInMs=1000, callback = None):
        durationInMs = max(durationInMs,100)
        _direct = direction
        self.rotateWheels(direction = _direct)
        time.sleep(durationInMs/1000)
        self.stop()
        if callback is not None:
            callback()
    
    def rotateWheels(self, wheelSet = Drivar.WHEELS_BOTH, direction = Drivar.DIR_FORWARD, speedLevel = Drivar.SPEED_FAST, callback = None):
        power = self._getNxtSpeed(speedLevel)
        # Correct the power (positive vs negative) depending on the direction
        if(direction == Drivar.DIR_FORWARD):
            if(power < 0):
                power = power * -1
        if(direction == Drivar.DIR_BACKWARD):
            if(power > 0):
                power = power * -1
        # Get the wheels turning
        if(wheelSet == Drivar.WHEELS_LEFT or wheelSet == Drivar.WHEELS_BOTH):
            self.m_leftMotor.run(power)
        if(wheelSet == Drivar.WHEELS_RIGHT or wheelSet == Drivar.WHEELS_BOTH):
            self.m_rightMotor.run(power)
        self.m_moving = True
        
    def stop(self, callback = None):
        self.m_leftMotor.idle()
        self.m_rightMotor.idle()
        self.m_moving = False
 
 
    '''
      Return the distance to the nearest obstacle, in centimeters
    '''
    def getDistanceToObstacle(self):
        return m_ultrasonicSensor.get_sample()
 
    '''
      Indicate with a boolean whether there is an obstacle within the given distance
    '''
    def isObstacleWithin(self, distance):
        dist = m_ultrasonicSensor.get_sample()
        if(dist <= distance):
            return True
        else:
            return False
        
    def wait(self, duration = 1000):
        time.sleep(duration)
        
    '''
      Return the NXT speed equivalent for the given DRIVAR speed flag
    '''
    @staticmethod
    def _getNxtSpeed(speed):
        if(speed==Drivar.SPEED_SLOW):
            return 70
        elif(speed==Drivar.SPEED_MEDIUM):
            return 100
        elif(speed==Drivar.SPEED_FAST):
            return 127
        else :
            return 100 

Drivar.register(DrivarNxt)

