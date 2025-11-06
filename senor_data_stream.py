import random
import time
def temperature_sensor():
    while True:
        yield round(random.uniform(20.0,30.0),2)
        time.sleep(1)
for reading in temperature_sensor():
    print(f"Current temperatur: {reading}")