'''#from time import sleep
import serial
serial_speed = 9600
serial_port = '/dev/ttyACM0'
ser = serial.Serial(serial_port, serial_speed, timeout=1)


# Measure data from the sensor
def measure(self):
    # Request data and read the answer
    ser.write("m")
    data = ser.readline()

    # If the answer is not empty, process & display data
    if (data != ""):
        processed_data = data.split(",")
        self.temp_data.set("Temperature: " + str(processed_data[0]))
        self.temperature.pack()

    self.hum_data.set("Humidity: " + str(processed_data[1]))
    self.humidity.pack()


    # Wait 1 second between each measurement
    self.after(1000, self.measure)

'''
# Graphical User Interface for the Bluetooth sensor

# Imports
import time
import serial
from tkinter import *

# Serial port parameters
serial_speed = 115200
serial_port = '/dev/ttyACM0'

# Test with USB-Serial connection
# serial_port = '/dev/tty.usbmodem1421'

ser = serial.Serial(serial_port, serial_speed, timeout=1)


# Main Tkinter application
class Application(Frame):

    # Measure data from the sensor
    def measure(self):
        # Request data and read the answer
        ser.write(str.encode('m'))
        data = ser.readline()[:-2]

        # If the answer is not empty, process & display data
        if (data != ""):
            print(data)
            processed_data = data.split(str.encode(','),5)

            data = str(processed_data[0], 'utf-8')
            hum = str(processed_data[-1], 'utf-8')
            print(data)
            print(hum)

            self.temp_data.set("Temperature: " + data)
            self.temperature.pack()

            self.hum_data.set("Humidity: " + hum)
            self.humidity.pack()

        # Wait 1 second between each measurement
        self.after(1000, self.measure)

    # Create display elements
    def createWidgets(self):
        self.temperature = Label(self, textvariable=self.temp_data, font=('Verdana', 40, 'bold'))
        self.temp_data.set("Temperature")
        self.temperature.pack()

        self.humidity = Label(self, textvariable=self.hum_data, font=('Verdana', 40, 'bold'))
        self.hum_data.set("Humidity")
        self.humidity.pack()

    # Init the variables & start measurements
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.temp_data = StringVar()
        self.hum_data = StringVar()
        self.createWidgets()
        self.pack()
        self.measure()


# Create and run the GUI
root = Tk()
app = Application(master=root)
app.mainloop()