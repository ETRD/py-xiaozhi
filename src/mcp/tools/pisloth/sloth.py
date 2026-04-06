from robot_hat import SunfounderRobot
from robot_hat import Pin, setup_env_vars
import time

setup_env_vars()

class Sloth(SunfounderRobot):
    move_list = {
        "forward":[
            [0, 40, 0, 15],
            [-30, 40, -30, 15],
            [-30, 0, -30, 0],

            [0, -15, 0, -40],
            [30, -15, 30, -40],
            [30, 0, 30, 0],
            ],
        "turn right":[
            [0, -20, 0, -40],
            [-20, -20, 0, -40],
            [-20, 0, 0, 0],

            [0, 40, 0, 20],
            [20, 40, 0, 20],
            [20, 0, 0, 0],
            ],
        "turn left":[
            [0, 40, 0, 20],
            [0, 40, 20, 20],
            [0, 0, 20, 0],

            [0, -20, 0, -40],
            [0, -20, -20, -40],
            [0, 0, -20, 0],
            ],
        "backward":[
            [0, 40, 0, 15],
            [30, 40, 30, 15],
            [30, 0, 30, 0],

            [0, -15, 0, -40],
            [-30, -15, -30, -40],
            [-30, 0, -30, 0],
            ],
        "stand":[
            [0,0,0,0],
            ],
        "moon walk left": [
            [0, 0, 0, -30],
            [0, 30, 0, -60],
            [0, 60, 0, -30],
            [0, 30, 0, 0],
            [0, 0, 0, 0]
            ],
        "moon walk right": [
            [0, 30, 0, 0],
            [0, 60, 0, -30],
            [0, 30, 0, -60],
            [0, 0, 0, -30],
            [0, 0, 0, 0]
            ],
        "hook": [
            [0, 50, 0, -50],
            ],
        "big swing": [
            [0, -90, 0, 90],
            ],
        "swing": [
            [0, -40, 0, 40],
            ],
        "walk boldly": [
            [-15, -15, 15, -40],
            [10, -30, 40, -40],
            [10, 0, 40, 0],

            [-15, 40, 15, 15],
            [-40, 40, -10, 30],
            [-40, 0, -10, 0],
            ],
        "walk backward boldly": [
            [-15, -15, 15, -40],
            [-40, -30, -10, -40],
            [-40, 0, -10, 0],

            [-15, 40, 15, 15],
            [10, 40, 40, 30],
            [10, 0, 40, 0],
            ],
        "walk shyly": [
            [10, -15, -10, -40],
            [25, -30, -5, -40],
            [25, 0, -5, 0],

            [10, 40, -10, 15],
            [5, 40, -25, 30],
            [5, 0, -25, 0],
            ],
        "walk backward shyly": [
            [10, -15, -10, -40],
            [5, -30, -25, -40],
            [5, 0, -25, 0],

            [10, 40, -10, 15],
            [25, 40, -5, 30],
            [25, 0, -5, 0],
            ],
        "stomp right": [
            [0, 15, 0, 0],
            [0, 30, 0, -15],
            [0, 15, 0, -30],
            [0, 0, 0, -15],
            [0, 0, 0, 0],
            ], 
        "stomp left": [  
            [0, 0, 0, -15],
            [0, 15, 0, -30],
            [0, 30, 0, -15],
            [0, 15, 0, 0],
            [0, 0, 0, 0]
            ],
        "close": [
            [30, 0, -30, 0],
            # [0, 0, 0, 0]
            ],
        "open": [
            [-30, 0, 30, 0],
            # [0, 0, 0, 0]
            ],
        "tiptoe left":[
            [-20, 35, -20, 15],
            [-20, 15, -20, 15],
            ],
        "tiptoe right":[
            [20, -15, 20, -35],
            [20, -15, 20, -15],
            ],
        "fall left": [
            [-40, 70, -40, 30],
            [-40, 30, -40, 30],
            ],
        "fall right": [
            [40, -30, 40, -70],
            [40, -30, 40, -30],
            ],
    }

    def do_action(self,motion_name, step=1, speed=None, bpm=None):
        if bpm == None:
            speed = 50 if speed == None else speed
            # speed = mapping(speed, 0, 100, 0, 80)
        for _ in range(step):
            for motion in self.move_list[motion_name]:
                if bpm != None:
                    self.servo_move(motion, bpm=bpm)
                else:
                    self.servo_move(motion, speed=speed)

    def add_action(self,action_name,action_list):
        if action_name not in self.move_list.keys():
            self.move_list[action_name] = action_list

# reset mcu first
mcu_rst = Pin("MCURST", Pin.OUT)
mcu_rst.value(0)  # Hold the MCU in reset
time.sleep(0.1)  # Wait for a moment to ensure the reset is registered
mcu_rst.value(1)  # Release the reset to allow the MCU to boot up
time.sleep(0.1)  # Wait for a moment to ensure the reset is registered

config_file = '/home/launcher/.config/robot-hat-pypi/robot-hat.conf'
sloth = Sloth([0,1,2,3], config_file)
sloth.set_offset([0,0,-8,-5])
sloth.calibration()

def pisloth_do_action(action_type='stand'):
    if action_type == 'forward':
        sloth.do_action('forward', 1, 40)
        sloth.do_action('stand', 1, 40)
    elif action_type == 'backward':
        sloth.do_action('backward', 1, 40)
        sloth.do_action('stand', 1, 40)
    elif action_type == 'dance':
        sloth.do_action('stomp right', 1, 70)
        sloth.do_action('stomp left', 1, 70)
        sloth.do_action('stand', 1, 70)
    else:
        sloth.do_action('stand', 1, 40)



if __name__=="__main__":

    ## reset mcu first
    #mcu_rst = Pin("MCURST", Pin.OUT)
    #mcu_rst.value(0)  # Hold the MCU in reset
    #time.sleep(0.1)  # Wait for a moment to ensure the reset is registered
    #mcu_rst.value(1)  # Release the reset to allow the MCU to boot up
#
    #config_file = '/home/launcher/.config/robot-hat-pypi/robot-hat.conf'
    #sloth = Sloth([0,1,2,3], config_file)
    #sloth.set_offset([0,0,-8,-5])
    #sloth.calibration()
    ##while 1:
    #sloth.do_action('forward', 1, 40)
    #sloth.do_action('stand', 1, 40)
    #time.sleep(1)
    #sloth.do_action('backward', 1, 40)
    #sloth.do_action('stand', 1, 40)
    #time.sleep(1)
    #sloth.do_action('open', 1, 40)
    #time.sleep(1)
    #sloth.do_action('close', 1, 40)
    #time.sleep(1)
    #sloth.do_action('stomp right', 1, 40)
    #time.sleep(1)
    #sloth.do_action('stomp left', 1, 40)
    #time.sleep(1)
    #sloth.do_action('stand', 1, 40)
    #time.sleep(1)
    pisloth_do_action('dance')

