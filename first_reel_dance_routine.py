from ServoDriver import ServoDriver
import numpy as np
import time

# Initialize
s = ServoDriver(0x40, debug=False)
AZ = 0 # channel 0 refers to azimuth
EL = 1 # channel 1 refers to elevation
delay = 0.25;
time.sleep(delay)

# Center the ALP (automated laser pointer)
print('Centering ALP...')
s.center(AZ)
time.sleep(delay)
s.center(EL)
time.sleep(delay)
print('Complete! \n')

# Count Down
print('4')
time.sleep(1)
print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
time.sleep(1)
print('now!')


# Move ALP
print('Test Move #1...')

delay = 1
for i in range(2): 
    s.setAngle(AZ, 30)
    time.sleep(delay)
    s.setAngle(EL, 30)
    time.sleep(delay)
    s.setAngle(AZ, -30)
    time.sleep(delay)
    s.setAngle(EL, -30)
    time.sleep(delay)
    
delay = 0.5
for i in range(5): 
    s.setAngle(AZ, 30)
    time.sleep(delay)
    s.setAngle(EL, 30)
    time.sleep(delay)
    s.setAngle(AZ, -30)
    time.sleep(delay)
    s.setAngle(EL, -30)
    time.sleep(delay)
    
print('Complete! \n')

# Center the ALP (automated laser pointer)
print('Centering ALP...')
s.center(AZ)
time.sleep(delay)
s.center(EL)
time.sleep(delay)
print('Complete! \n')

