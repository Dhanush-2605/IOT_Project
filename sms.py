import time
import serial
import requests
from twilio.rest import Client
import json
from urllib.request import urlopen

account_sid = "AC872c82085c60036f383efc48b9370cfd"
auth_token = "5892c6f887f8a813ab5980d66ca269e6"
twilio_number = "++13253265690"
recipient_number = "+917702436070"

serial_port = "COM5"  # Update with your serial port
baud_rate = 9600
ser = serial.Serial(serial_port, baud_rate, timeout=1)
client = Client(account_sid, auth_token)


while True:
    # Reading from arduino
    line = ser.readline().decode("latin-1").strip()
    print(line)

    # Alcohol
    if line =="640":
        
        url = "http://ipinfo.io/json"
        response = urlopen(url)
        data = json.load(response)
        x = f'fire here at: {data["city"]}, region: {data["region"]}, country: {data["country"]}, Lat & Long: {data["loc"]}'
        # Send the message via Twilio
        message = client.messages.create(
            body=x, from_=twilio_number, to=recipient_number
        )
        print("Message sent successfully!")
    # PIR Sensor
# Close the serial port
ser.close()