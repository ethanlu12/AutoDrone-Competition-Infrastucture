from Motor import Motor
import time
class Rover:
    def __init__(self):
        self.state = "standby"
        self.motor = Motor()
        self.speed.setMotorModel(0,0,0,0)
    def check_status(self):
        print("rover status:",self.state)

    def move(self,speed,interval):
        #move the rover foward or backward
        self.state = "moving"
        self.motor.setMotorModel(speed,speed,speed,speed)
        time.sleep(interval)

    def rotate(self,direction_flag,speed,interval):
        #rotate rover 90 degrees
        if direction_flag == False:
            print("\nrotate the rover to the left")
            self.state = "rotating"
            self.motor.setMotorModel(-speed/4,-speed/4,speed,speed)
        elif direction_flag == True:
            print("rotate the rover to the right")
            self.state = "rotating"
            self.motor.setMotorModel(speed,speed,-speed/4,-speed/4)
        else:
            print("error in flag, True for turning right, False for turning left")
        time.sleep(interval)
    def halting(self,interval):
        self.state = 'halting'
        Rover.move(0,interval)
    '''
    enter movement set below
    def execute_path(self,path_indicator)
        if path_indicator == 0:
            #enter code for path 0
        elif path_indicator == 1:
            #enter code for path 1
        elif path_indicator == 2:
            #enter code for path 2
        elif path_indicator == 3
            #enter code for path 3
        
    '''