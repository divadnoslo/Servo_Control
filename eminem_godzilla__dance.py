# Dance Rountine to "The Next Episode"
from LP import LP
import time
import numpy as np

# Construct a LP object
lp = LP(delay=0.005)

# Center the Device
# lp.centerLP()
# time.sleep(1)

# Set Tempo
f = (40*4)/60
dt = 1 / f
dt8 = dt/2
dt16 = dt/4

# Set Rhythm for the Dance
dance = [3*dt, dt8, dt8, 3*dt8, dt, 3*dt, \
         3*dt, dt8, dt8, 3*dt8, dt, 3*dt, \
         2*dt, dt16, dt16, dt16, dt16, dt16, dt16, dt16, dt16,\
         dt16, dt16, dt16, dt16, dt16, dt16, dt16, dt16, dt16, dt16, dt16, dt16, dt16, dt16, dt16, dt16, \
         dt16, dt16, dt16, dt16, dt16, dt16, dt16, dt16, dt16, dt16, dt16, dt16, dt16, dt16, dt16, dt16, \
         dt16, dt16, dt16, dt16, dt16, dt16, dt16, dt16, dt16, dt16, dt16, dt16, dt16, dt16, dt16, dt16, \
         dt16, dt16, dt16, dt16, dt16, dt16, dt16, dt16, dt16, dt16, dt16, dt16, dt16, dt16, dt16, dt16, \
         ]

# Set Azimuth Positions
az = [45, 0, -15, -30, -45, 0, \
      45, 0, -15, -30, -45, 0, \
      60, 75, 70, 65, 60, 55, 50, 45, 40, \
      35, 30, 25, 20, 15, 10, 5, 0, 5, 10, 15, 20, 25, 30, 35, 40, \
      35, 30, 25, 20, 15, 10, 5, 0, 5, 10, 15, 20, 25, 30, 35, 40, \
      35, 30, 25, 20, 15, 10, 5, 0, 5, 10, 15, 20, 25, 30, 35, 40, \
      35, 30, 25, 20, 15, 10, 5, 0, 5, 10, 15, 20, 25, 30, 35, 40, \
      ]

# Set Elevation Positions
el = [-15, -45, -30, 15, 5, 0, \
      -15, -45, -30, 15, 5, 0, \
      -45, -40, -35, -30, -25, -20, -15, -10, -5, \
      5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, \
      15, 10, 15, 10, 15, 10, 15, 10, 15, 10, 15, 10, 15, 10, 15, 10, \
      5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, \
      15, 10, 15, 10, 15, 10, 15, 10, 15, 10, 15, 10, 15, 10, 15, 10, \
      ]

# # Count Off Dance
# print('1')
# time.sleep(dt1)
# print('2')
# time.sleep(dt1)
# print('3')
# time.sleep(dt1)
# print('4')
# time.sleep(dt1)
# print('now!')

# and Dance!
n = np.arange(0, len(dance))
for k in n:
    lp.setLP(az[k], el[k])
    time.sleep(dance[k])

time.sleep(1)
lp.centerLP()
print('nice')



      
      
      
      
