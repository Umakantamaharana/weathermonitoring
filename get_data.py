import serial
import json

b = serial.Serial('COM3', 9600, timeout=1)
data = []

while True:
    d = b.readline()
    d = d.decode().rstrip()
    if d != "_":
        try:
            data.append(float(d))
        except:
            data.append(d)
    if d == "_":
        try:
            data[0] = data[0]/10
            data[1] = data[1]*20
        except:
            pass
        json_data = [
            data[0],
            data[1],
            data[2],
            data[3]
        ]

        print(json_data)
        with open("data.json", "w") as f:
            json.dump(json_data, f)

        data = []
