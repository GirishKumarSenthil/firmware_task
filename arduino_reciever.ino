#define E2END 1023 // here i am defining the end address of eeprom

//function to write
void EEPROM_write(int address, byte value) {
  while (EECR & (1 << EEPE)) {} // wait for the completion of the previous write
  EEAR = address; // setting up the data and address
  EEDR = value;
  EECR |= (1 << EEMPE); // writing logical 1 to master programming enable
  EECR |= (1 << EEPE); // start eeprom write by setting programming enable
}

// function to read
byte EEPROM_read(int address) {
  while (EECR & (1 << EEPE)) {} // wait for completion of previous write
  EEAR = address; // set up address register
  EECR |= (1 << EERE); // start eeprom read by setting the read enable
  return EEDR; // return the data from eeprom
}

void setup() {
  Serial.begin(2400);
}

void loop() {
  if (Serial.available() > 0) {
    String receivingString = Serial.readStringUntil('\n'); // read until newline character
    
    //to calculate the length of the string
    int Length = receivingString.length();
    
    // write each character of the string to eeprom
    int address = 0; // starting address in eeprom
    for (int i = 0; i < Length; i++) {
      EEPROM_write(address + i, receivingString[i]);
    }
    
    // print the feedback to serial monitor
    Serial.println(receivingString);
    
    // wait for the serial data to be received
    delay(100);
  }

  // read the starting address and length of the string from serial monitor
  if (Serial.available() > 0) {
    int startAddress = Serial.parseInt();
    int Length = Serial.parseInt();
    
    // read each character of the string from eeprom
    String storedString = "";
    for (int i = 0; i < Length; i++) {
      char ch = EEPROM_read(startAddress + i);
      storedString += ch;
    }
    
    // send the stored string back to the PC
    Serial.print(storedString);
    
    // wait for serial data to be received
    delay(100);
  }
}
