from ServoDriver import ServoDriver
import numpy as np
import time

# Define Specific Laser Pointer (LP) Class
class LP(ServoDriver):
    
    # Constructor
    def __init__(self, AZ=0, EL=1, delay=0.1):
        super().__init__(0x40, False)
        self.AZ = AZ # Azimuth is Channel Zero
        self.EL = EL # Elevation is Channel One
        self.delay = delay # seconds
        
    # Center the LP Orientation
    def centerLP(self):
        self.center(self.AZ)
        time.sleep(self.delay)
        self.center(self.EL)
        time.sleep(self.delay)
        
    # Move the LP to a new Orientation
    def setLP(self, az, el):
        self.setAngle(self.AZ, az)
        time.sleep(self.delay)
        self.setAngle(self.EL, el)
        time.sleep(self.delay)
        
    # Draw a Circle
    def drawCircle(self, theta, delta):
        self.setLP(0, theta)
        time.sleep(1)
        for k in np.arange(0, 2*np.pi, delta * np.pi/180):
            self.setLP(theta * np.sin(k), theta * np.cos(k))
        time.sleep(1)
        self.centerLP()
        
    # Draw a Square
    def drawSquare(self, theta, delta, corner="NW", dir="CW"):
        pass
        
    
        
    
    
    
        
    