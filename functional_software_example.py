import time, board, busio
import cpc
import adafruit_lsm9ds1 as IMU

# I2C connection:
i2c = busio.I2C(board.SCL, board.SDA)
sensor1 = IMU.LSM9DS1_I2C(i2c, address=0x40)
sensor2 = IMU.LSM9DS1_I2C(i2c, address=0x45)
# SPI connection:
spi = busio.SPI(board.SCK,
 MOSI=board.MOSI,
 MISO=board.MISO)
radio = CC1101(spi, freq=434400000, "666A")
radio.setupRX()
radio.setupCheck()
# the operational Loop
while True:
if 'take measurement' in radio.reciveData():
 [print(x, y, z) for x,y,z in sensor1.acceleration]
time.sleep(1)
