from LP import LP
import time

# Construct a LP object
lp = LP()

# Center the Device
lp.centerLP()
time.sleep(1)

# # Move the Device to Different Positions
# lp.setLP(30, 30)
# time.sleep(3)
# lp.centerLP()

# Calibrate LP
lp.calLP(0, -2)

# Set LP
time.sleep(1)
lp.setLP(-15, 0)
time.sleep(1)
lp.setLP(15, 0)
time.sleep(1)

#Center LP
lp.centerLP()

# # Draw Circle
# lp.drawCircle(10, 10)

# # Draw Square
# lp.drawSquare(10, 1)  # I'll come back to this later