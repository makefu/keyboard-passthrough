/*
  Passthrough keypresses from serial to Keyboard 
 
 Not all pins on the Leonardo support change interrupts,
 so only the following can be used for RX:
 8, 9, 10, 11, 14 (MISO), 15 (SCK), 16 (MOSI).
 
 Protocol:
 2 bytes total:
   1 byte - press flag
     0x0 - next key released
     0x1 - next key pressed
   1 byte - character pressed
     for special chars look at arduino keyboard mapping
 
 */
#include <SoftwareSerial.h>

SoftwareSerial mySerial(9, 10); // RX, TX

// flag if the next key is pressed or released
bool press=true;

void setup(){
  mySerial.begin(9600);
  Keyboard.begin();
  //Serial.begin(9600);
}

void loop(){
  
  if (mySerial.available())
  {
    char k = mySerial.read();
    //Serial.write(k);
    //Serial.println(" received");

    if (k == 0){
      press = 0;
    }else if (k == 1){
      press = 1;
    }else {
      //mySerial.write(k);
      if (press){
        Keyboard.press(k);
        //mySerial.println(" pressed");
        
      } else {
        Keyboard.release(k);
        //mySerial.println(" released");
      }
    }
  }
}

