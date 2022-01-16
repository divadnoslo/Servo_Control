# import numpy as np
from ServoDriver import ServoDriver
import time

# Initialize
s = ServoDriver(0x40, debug=False)
time.sleep(1)
# 
# print('go!')
# s.setServoPulse(0, 2710)
# time.sleep(1)
# 
# print('and back!')
# s.setServoPulse(0, 390)

# Center the Servo
print('center! \n')
s.center(0)
time.sleep(5)

# Test Some Angles
print('45 \n')
s.setAngle(0, 45)
time.sleep(5)

print('-45 \n')
s.setAngle(0, -45)
time.sleep(5)

print('90 \n')
s.setAngle(0, 90)
time.sleep(5)

print('-90 \n')
s.setAngle(0, -90)
time.sleep(5)

print('center! \n')
s.center(0)

