# Dance Rountine to "Chin Up High" by Ame Bababi
from LP import LP
import time
import numpy as np

# Construct a LP object
lp = LP(delay=0.01)

# Center the Device
lp.centerLP()
time.sleep(1)

# Set Tempo
f = 160/60 # for 160 bpm
dt = 1 / f

# Set Rhythm for the Dance
dance = [dt, dt, dt, dt, dt, dt, 2*dt, \
         dt, dt, 2*dt, 2*dt, 2*dt, \
         dt, dt, dt, dt, dt, dt, 2*dt, \
         dt, dt, 2*dt, 2*dt, dt, dt, \
         dt, dt, dt, dt, dt, dt, 2*dt, \
         dt, dt, 2*dt, 2*dt, 2*dt, \
         dt, dt, dt, dt, dt, dt, 2*dt, \
         dt, dt, 2*dt, 2*dt, dt, dt]       

# Set Azimuth Positions
az = [-15, -10, -5, 0, 5, 10, 15, \
      0, 15, 0, -15, 15, \
      -15, -10, -5, 0, 5, 10, 15, \
      0, -15, 15, -15, -5, -10, \
      -15, -10, -5, 0, 5, 10, 15, \
      0, 15, 0, -15, 15, \
      -15, -10, -5, 0, 5, 10, 15, \
      0, -15, 15, -15, -5, -10]

# Set Elevation Positions
el = [-20, -10, -20, -10, -20, -10, -20, \
      0, 30, 60, 15, 45, \
      -20, -10, -20, -10, -20, -10, -20, \
      0, 10, 0, 30, -30, -15, \
      -20, -10, -20, -10, -20, -10, -20, \
      0, 30, 60, 15, 45, \
      -20, -10, -20, -10, -20, -10, -20, \
      0, 10, 0, 30, -30, -15]

# Count Off Dance
print('1')
time.sleep(dt)
print('2')
time.sleep(dt)
print('3')
time.sleep(dt)
print('4')
time.sleep(dt)

# and Dance!
n = np.arange(0, len(dance))
for k in n:
    lp.setLP(az[k], el[k])
    time.sleep(dance[k])
    
lp.centerLP()
print('nice')



      
      
      
      