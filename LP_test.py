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

# # Draw Circle
# lp.drawCircle(60, 10)

# Draw Square
lp.drawSquare(10, 1)  # I'll come back to this later