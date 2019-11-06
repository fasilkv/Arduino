// Bluetooth temperature sensor

#include "DHT.h"

//#define DHTPIN 3    
#define DHTPIN 3
//#define DHTTYPE DHT22
#define DHTTYPE DHT11

// Create instance for the DHT sensor
DHT dht(DHTPIN, DHTTYPE);

// Setup
void setup(void)
{
  dht.begin();
  Serial.begin(115200);
  // for usb serial communication
  //Serial.println(F("DHTxx test!"));
}

void loop(void)
{
 
  //float t = dht.readTemperature();
  
    // Get command
    if (Serial.available() > 0) {
       //Serial.println(F("available!"));

    
      // Read command
      byte c = Serial.read ();
      
      // If a measurement is required, measure data and send it back
      if (c == 'm'){
           
          // Read temperature and humidity (the default)
          float h = dht.readHumidity();
          float t = dht.readTemperature();
          
          // Send data (temperature,humidity)
          Serial.print(t);
          Serial.print(",");
          Serial.print(h);
          Serial.print(",");
                        
      }
   
  }

}
