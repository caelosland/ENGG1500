""" Using the weighted arithmetic mean method from
    the Lab 4 document """

# Import the `Pin' class from the `machine' module and import ADC analog module
from machine import Pin
from pyb import ADC
# Import the `time' module
import time
# Create a Pin instance to configure pin A1, A2, A3, A4 as analog input
IR_sensor1 = ADC(Pin("A1"))
IR_sensor2 = ADC(Pin("A2"))
IR_sensor3 = ADC(Pin("A3"))
IR_sensor4 = ADC(Pin("A4"))
# Declare a variable "sensor_reading" that we can use later,
# At the same time we declare it we set it equal to 0,
# It is declared here so that it can be used inside the while loop
sensor_reading1 = 0
sensor_reading2 = 0
sensor_reading3 = 0
sensor_reading4 = 0

# Distances from the centroid of the robot to the centre of each sensor in mm
x1 = -22.5
x2 = -7.5
x3 = 7.5
x4 = 22.5

while True:
    # TODO: Take sensor measurements using "w1 = adc_A1.read()"
    sensor_reading1 = IR_sensor1.read()         # TODO: Read the sensor's value into sensor_reading here
    sensor_reading2 = IR_sensor2.read()
    sensor_reading3 = IR_sensor3.read()
    sensor_reading4 = IR_sensor4.read()
    # storing sensor data in w1, w2, w3, w4
    # TODO: Calculate numerator of weighted average
    numerator = (sensor_reading1 * x1) + (sensor_reading2 * x2) + (sensor_reading3 * x3) + (sensor_reading4 * x4)
    # TODO: Calculate denominator of weighted average
    denominator = sensor_reading1 + sensor_reading2 + sensor_reading3 + sensor_reading4
    line_dist = numerator/denominator
    print("Distance from line = {:3.2f}".format(line_dist))
    time.sleep(0.3)    # 30ms delay
