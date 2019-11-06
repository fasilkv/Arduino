#from time import sleep
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
