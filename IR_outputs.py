# """Digital Input IR
# Reads a digital (1 or 0) value from an IR sensor connected to the pin A1
# and prints the value to the REPL every 100 ms.
# """
#
# # Import the `Pin' class from the `machine' module
# from machine import Pin
# # Import the `time' module
# import time
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


"""Analog Input IR
Reads an analog value from an IR sensor connected to the pin A1, A2, A3, A4
and prints the value to the REPL every 100 ms.
"""

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

while True:
    # Put code here to run forever
    time.sleep(0.5)        # TODO: Insert 0.1s sleep here
    sensor_reading1 = IR_sensor1.read()         # TODO: Read the sensor's value into sensor_reading here
    sensor_reading2 = IR_sensor2.read()
    sensor_reading3 = IR_sensor3.read()
    sensor_reading4 = IR_sensor4.read()
    # Print the latest value read from the sensor to the REPL
    print(sensor_reading1, sensor_reading2, sensor_reading3, sensor_reading4)