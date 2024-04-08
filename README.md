# firmware_task
**Description**:
                This Firmware task facilitates seamless communication between a PC and an Arduino board using UART (Universal Asynchronous Receiver-Transmitter) communication protocol. This project is particularly useful for scenarios where text messages need to be transmitted between a PC and an embedded system such as an Arduino board.

**Key Features**:
1. Bidirectional Communication: Allows transmission of text messages from the PC to the Arduino board and vice versa.
2. EEPROM Storage: Enables storing received messages in the Arduino's EEPROM (Electrically Erasable Programmable Read-Only Memory) for later retrieval.
3. Real-time Transmission Speed Display: Provides real-time feedback on the data transmission speed during communication.
4. Python-Arduino Interface: Utilizes a Python script to initiate message transmission from the PC to the Arduino board and display received messages.

**Technologies Used**:
1. Arduino IDE: Used for writing, compiling, and uploading the embedded C++ program to the Arduino board.
2. Python: Utilized for implementing the PC-side script responsible for initiating message transmission and displaying received messages.
3. Serial Communication (UART): Implements serial communication protocol for data exchange between the PC and the Arduino board.
4. EEPROM Memory: Stores received messages in the Arduino's EEPROM memory for persistent storage.

**How to Use**:
1. Upload the provided embedded C++ to your Arduino board using the Arduino IDE.
2. Run the Python script (pc_to_arduino.py) on your PC to initiate the message transmission from the PC to the Arduino board.
3. Enter the desired text message in the the Python script and press Enter to send the message.
4. The Arduino board will store the received message in its EEPROM memory and display the transmission speed in bits per second.
5. Once the transmission is complete, the stored message can be retrieved and sent back to the PC.
6. The Python script will display the received message along with the transmission speed.

**Contribution Guidelines**:
Contributions to this project are welcome! If you'd like to contribute, please fork the repository, make your changes, and submit a pull request. For major changes, please open an issue first to discuss the proposed changes.
