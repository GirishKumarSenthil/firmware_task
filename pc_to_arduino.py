import serial
import time

# Configure serial port
serial_port = serial.Serial('COM6', 2400)  # Change the com port if necessary
time.sleep(2)  # Allow time for the Arduino to reset after opening serial connection

# Sending a string to Arduino
message_to_send = "Finance Minister Arun Jaitley Tuesday hit out at former RBI governor Raghuram Rajan for predicting that the next banking crisis would be triggered by MSME lending, saying postmortem is easier than taking action when it was required. Rajan, who had as the chief economist at IMF warned of impending financial crisis of 2008, in a note to a parliamentary committee warned against ambitious credit targets and loan waivers, saying that they could be the sources of next banking crisis. Government should focus on sources of the next crisis, not just the last one.* In particular, government should refrain from setting ambitious credit targets or waiving loans. Credit targets are sometimes achieved by abandoning appropriate due diligence, creating the environment for future NPAs,\" Rajan said in the note.\" Both MUDRA loans as well as the Kisan Credit Card, while popular, have to be examined more closely for potential credit risk. Rajan, who was RBI governor for three years till September 2016, is currently.\n"
send_start_time = time.time()
for character in message_to_send:
    serial_port.write(character.encode())
    send_end_time = time.time()
    print("Transmission speed for", character, ":", (8.0 / (send_end_time - send_start_time)))
    send_start_time = send_end_time

# Wait for Arduino to process and send back the stored message
time.sleep(2)

serial_port.write(b"0\n1005\n")

# Read the stored string from Arduino
received_string = ''
receive_start_time = time.time()
while True:
    received_char = serial_port.read().decode()
    receive_end_time = time.time()
    if received_char == '\n':
        break
    received_string += received_char
    print("Received character:", received_char)
    reception_speed = 8.0 / (receive_end_time - receive_start_time)
    print("Reception speed:", reception_speed)
    receive_start_time = receive_end_time

# Print the received string
print("Received string from Arduino:\n", received_string.strip())

# Close serial connection
serial_port.close()
