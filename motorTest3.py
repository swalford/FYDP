import time
import resultByIDDao
import settings
import motorFunctions

basetime = time.time()
motorFunctions.connectVFD()

print("Starting Test 3: Short Skid Tests")
print("Test 3 - Clockwise direction")
motorFunctions.setAccelerationTime(90) #9s
motorFunctions.setSpeed(900) #900rpm
motorFunctions.startMotorForward()
time.sleep(9) #accelerate for 9s
time.sleep(30) #maintain speed for 30s TODO: add sensors, may need
motorFunctions.setSmallDecelerationTime(0.4) #0.4s 
motorFunctions.setSpeed(860) #860rpm
time.sleep(0.4) #decelerate for 0.4s TODO: add sensors
time.sleep(10) #maintain speed for 10s TODO: sensors
motorFunctions.setDecelerationTime(90) #9s deceleration time
motorFunctions.setSpeed(500) #500rpm
time.sleep(9) #decelerate for 9s TODO: sensors
time.sleep(30) #maintain speed for 10s
motorFunctions.setSmallDecelerationTime(0.4) #0.4s
motorFunctions.setSpeed(460) #460rpm
time.sleep(0.4) #decelerate for 0.4s TODO: sensors
time.sleep(10) #maintain speed for 10s TODO: sensors
motorFunctions.setDecelerationTime(90) #9s
motorFunctions.setSpeed100() #100rpm
time.sleep(9) #decelerate for 9s
time.sleep(30) #maintain speed for 30s TODO: sensors
motorFunctions.setSmallDecelerationTime(0.4) #0.4s
motorFunctions.setSpeed60() #60rpm
time.sleep(0.4) #decelerate for 0.4s TODO: sensors
time.sleep(10) #maintain speed for 10s
motorFunctions.setDecelerationTime(15) #1.5s
motorFunctions.stopMotor()
time.sleep(1.5) #decelerate for 1.5s
time.sleep(1) #rest for a second
print("Test 3 - Anticlockwise direction")
motorFunctions.setAccelerationTime(90) #9s
motorFunctions.setSpeed(900) #900rpm
motorFunctions.startMotorReverse()
time.sleep(9) #accelerate for 9s
time.sleep(30) #maintain speed for 30s TODO: add sensors, may need
motorFunctions.setSmallDecelerationTime(0.4) #0.4s 
motorFunctions.setSpeed(860) #860rpm
time.sleep(0.4) #decelerate for 0.4s TODO: add sensors
time.sleep(10) #maintain speed for 10s TODO: sensors
motorFunctions.setDecelerationTime(90) #9s deceleration time
motorFunctions.setSpeed(500) #500rpm
time.sleep(9) #decelerate for 9s TODO: sensors
time.sleep(30) #maintain speed for 10s
motorFunctions.setSmallDecelerationTime(0.4) #0.4s
motorFunctions.setSpeed(460) #460rpm
time.sleep(0.4) #decelerate for 0.4s TODO: sensors
time.sleep(10) #maintain speed for 10s TODO: sensors
motorFunctions.setDecelerationTime(90) #9s
motorFunctions.setSpeed100() #100rpm
time.sleep(9) #decelerate for 9s
time.sleep(30) #maintain speed for 30s TODO: sensors
motorFunctions.setSmallDecelerationTime(0.4) #0.4s
motorFunctions.setSpeed60() #60rpm
time.sleep(0.4) #decelerate for 0.4s TODO: sensors
time.sleep(10) #maintain speed for 10s
motorFunctions.setDecelerationTime(15) #1.5s
motorFunctions.stopMotor()
time.sleep(1.5) #decelerate for 1.5s
print("Test 3 finished")


