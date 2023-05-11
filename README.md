# weathermonitoring ⛅
IoT project with DHT11 module, moisture sensor and photoresgister 🤖

## Hardware requirements 🧑‍🔧
- Arduino UNO
- DHT 11 module
- moisture sensor
- photoregister

## Data pins used in this model 📌
- Digital pin 4 for DHT 11 module
- Analog A0 pin for photoregister
- Analog A1 pin for moisture sensor
- Other connections are vcc and gnd ( connect accordingly )

## Software requirements 💻
- Python 3.0 or newer

### Before proceeding to next step double check the connection ⚠️

## Steps to run the code ⏩
1. Download this zip and extract it. ( or clone this repo )
2. Open command prompt and install the requirements `pip install -r requirements.txt`
4. change directory to the cloned or extracted folder. `cd weathermonitoring`
5. Create a python server on your desired port. I'm taking port number 5000. `python -m http.server 5000`
6. Replace the Arduino port in the code ('COM3') by your COM port.
7. Create another instance of the terminal and run the python file `python get_data.py`
8. It will create a json file in this directory.
9. Go to your browser and type the url `http://localhost:5000`. You will get a dynamic bar chart showing the light intensity, moisture, humidity and temperature.

# Thank you 👍
