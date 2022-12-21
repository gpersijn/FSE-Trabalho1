import time
import board
import adafruit_dht


# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
# dhtDevice = adafruit_dht.DHT22(board.D18, use_pulseio=False)

def show_temperature(sala: int):

    if (sala == 1):
        dhtDevice = adafruit_dht.DHT22(board.D4)
        print('sala 01')

    elif (sala == 2):
        dhtDevice = adafruit_dht.DHT22(board.D18)
        print('sala 02')

    try:
        while True:
            try:
                # Print the values to the serial port
                temperature_c = dhtDevice.temperature
                temperature_f = temperature_c * (9 / 5) + 32
                humidity = dhtDevice.humidity
                print(
                    "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                        temperature_f, temperature_c, humidity
                    )
                )

            except RuntimeError as error:
                # Errors happen fairly often, DHT's are hard to read, just keep going
                print(error.args[0])
                time.sleep(2.0)
                continue
            except Exception as error:
                dhtDevice.exit()
                raise error
            time.sleep(2.0)
    except:
        print('Voltando...')
        time.sleep(2.0)
