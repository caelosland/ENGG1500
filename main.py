# """Digital Input IR
# Reads a digital (1 or 0) value from an IR sensor connected to the pin A1
# and prints the value to the REPL every 100 ms.
# """
#
# # Import the `Pin' class from the `machine' module
# from machine import Pin
# # Import the `time' module
import time
# # Create a Pin instance to configure pin A0/PA0 as a digital input
# IR_sensor1 = Pin("A1", Pin.IN)
# IR_sensor2 = Pin("A2", Pin.IN)
# IR_sensor3 = Pin("A3", Pin.IN)
# IR_sensor4 = Pin("A4", Pin.IN)
# # Declare a variable "sensor_reading" that we can use later,
# # At the same time we declare it we set it equal to 0,
# # It is declared here so that it can be used inside the while loop
# sensor_reading1 = 0
# sensor_reading2 = 0
# sensor_reading3 = 0
# sensor_reading4 = 0
#
# while True:
#     # Put code here to run forever
#     time.sleep(0.1)        # TODO: Insert 0.1s sleep here
#     sensor_reading1 = IR_sensor1.value()         # TODO: Read the sensor's value into sensor_reading here
#     sensor_reading2 = IR_sensor2.value()
#     sensor_reading3 = IR_sensor3.value()
#     sensor_reading4 = IR_sensor4.value()
#     # if sensor_reading1 == 1:
#     #     sensor_reading1 = 0
#     # elif sensor_reading1 == 0:
#     #     sensor_reading1 = 1
#     # following line flips 0 and 1 values (why isn't the value correct to start?)
#     sensor_reading1 = 1 - sensor_reading1
#     sensor_reading2 = 1 - sensor_reading2
#     sensor_reading3 = 1 - sensor_reading3
#     sensor_reading4 = 1 - sensor_reading4
#     # Print the latest value read from the sensor to the REPL
#     print(sensor_reading1, sensor_reading2, sensor_reading3, sensor_reading4)


# """Analog Input IR
# Reads an analog value from an IR sensor connected to the pin A1, A2, A3, A4
# and prints the value to the REPL every 100 ms.
# """
#
# # Import the `Pin' class from the `machine' module and import ADC analog module
# from machine import Pin
# from pyb import ADC
# # Import the `time' module
# import time
# # Create a Pin instance to configure pin A1, A2, A3, A4 as analog input
# IR_sensor1 = ADC(Pin("A1"))
# IR_sensor2 = ADC(Pin("A2"))
# IR_sensor3 = ADC(Pin("A3"))
# IR_sensor4 = ADC(Pin("A4"))
# # Declare a variable "sensor_reading" that we can use later,
# # At the same time we declare it we set it equal to 0,
# # It is declared here so that it can be used inside the while loop
# sensor_reading1 = 0
# sensor_reading2 = 0
# sensor_reading3 = 0
# sensor_reading4 = 0
#
# while True:
#     # Put code here to run forever
#     time.sleep(0.5)        # TODO: Insert 0.1s sleep here
#     sensor_reading1 = IR_sensor1.read()         # TODO: Read the sensor's value into sensor_reading here
#     sensor_reading2 = IR_sensor2.read()
#     sensor_reading3 = IR_sensor3.read()
#     sensor_reading4 = IR_sensor4.read()
#     # Print the latest value read from the sensor to the REPL
#     print(sensor_reading1, sensor_reading2, sensor_reading3, sensor_reading4)


# """ Using the weighted arithmetic mean method from
#     the Lab 4 document """
#
# # Import the `Pin' class from the `machine' module and import ADC analog module
# from machine import Pin
# from pyb import ADC
# # Import the `time' module
# import time
# # Create a Pin instance to configure pin A1, A2, A3, A4 as analog input
# IR_sensor1 = ADC(Pin("A1"))
# IR_sensor2 = ADC(Pin("A2"))
# IR_sensor3 = ADC(Pin("A3"))
# IR_sensor4 = ADC(Pin("A4"))
# # Declare a variable "sensor_reading" that we can use later,
# # At the same time we declare it we set it equal to 0,
# # It is declared here so that it can be used inside the while loop
# sensor_reading1 = 0
# sensor_reading2 = 0
# sensor_reading3 = 0
# sensor_reading4 = 0
#
# # Distances from the centroid of the robot to the centre of each sensor in mm
# x1 = -22.5
# x2 = -7.5
# x3 = 7.5
# x4 = 22.5
#
# while True:
#     # TODO: Take sensor measurements using "w1 = adc_A1.read()"
#     sensor_reading1 = IR_sensor1.read()         # TODO: Read the sensor's value into sensor_reading here
#     sensor_reading2 = IR_sensor2.read()
#     sensor_reading3 = IR_sensor3.read()
#     sensor_reading4 = IR_sensor4.read()
#     # storing sensor data in w1, w2, w3, w4
#     # TODO: Calculate numerator of weighted average
#     numerator = (sensor_reading1 * x1) + (sensor_reading2 * x2) + (sensor_reading3 * x3) + (sensor_reading4 * x4)
#     # TODO: Calculate denominator of weighted average
#     denominator = sensor_reading1 + sensor_reading2 + sensor_reading3 + sensor_reading4
#     line_dist = numerator/denominator
#     print("Distance from line = {:3.2f}".format(line_dist))
#     time.sleep(0.3)    # 30ms delay


# from machine import SoftI2C, Pin
# from time import sleep
# from APDS9960LITE import APDS9960LITE
#
# # Initialise I2C bus
# i2c = SoftI2C(scl=Pin("PB13"), sda=Pin("PB14"))
# # Initialise APDS9960
# apds9960 = APDS9960LITE(i2c)    # Create APDS9960 sensor object
# apds9960.prox.enableSensor()    # Send I2C command to enable sensor
# sleep(0.1)    # Let sensor measurement stabilise before starting loop
# while True:
#     proximity_measurement = apds9960.prox.proximityLevel    # Read the proximity
#     # ...value
#     print(proximity_measurement)    # Print proximity value
#     sleep(0.2)    # Wait for measurement to be ready




# from motor import Motor
# from encoder import Encoder
#
# # Create left and right 'Motor' objects
# motor_left = Motor("left", "D6", "D7", "D4")
# motor_right = Motor("right", "D8", "D9", "D5")
#
# # Create encoder object
# ENC_L = "D2"
# ENC_R = "D3"
# enc = Encoder(ENC_L, ENC_R)
#
# left_count = 0
# right_count = 0
# print("PWM, ENC_L, ENC_R")
#
# pwm = 0
# for pwm in range(0, 101, 1):
#     enc.clear_count()           # zero encoders
#     motor_left.set_forwards()  # Set the left motor to run forwards
#     motor_right.set_forwards()  # Set the right motor to run forwards
#     motor_left.duty(pwm)  # Set the left motor to x% pwm forwards
#     motor_right.duty(pwm)  # Set the left motor to x% pwm forwards
#     time.sleep(1)
#     left_count = enc.get_left()
#     right_count = enc.get_right()
#     print("{:3d}, {:4d}, {:4d}".format(pwm, left_count, right_count))


import matplotlib.pyplot as plt
import csv
pwm = []
left_enc = []
right_enc = []
with open('motor_csv.txt', 'r') as csvfile:
    plotdata = csv.reader(csvfile, delimiter=',')
    for row in plotdata:
        pwm.append(int(row[0]))
        left_enc.append(int(row[1]))
        right_enc.append(int(row[2]))
plt.plot(pwm, left_enc, marker='o')
plt.plot(pwm, right_enc, marker='o')
plt.title("Motor PWM vs Encoder Speed")
plt.xlabel("PWM Duty Cycle")
plt.ylabel("Encoder Count / Speed")
plt.show()
