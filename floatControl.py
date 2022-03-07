import time
liftoff=time.time()
import Adafruit_LSM303
import Adafruit_GPIO.SPI as SPI

lsm303 = Adafruit_LSM303.LSM303()
dist = 0
while True:
  accel, mag = lsm303.read()
  accel_x, accel_y, accel_z = accel
  mag_x, mag_y, mag_z = mag
  
  
