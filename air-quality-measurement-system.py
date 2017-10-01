#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Use of the following sensors and actuator:
# - Grove air quality sensor
# - Grove DHT sensor
# - Grove RGB LCD display

from grovepi import *
from grove_rgb_lcd import *
import sys, time


AIR_SENSOR_PORT = 0 # Grove air quality sensor analog port
DHT_SENSOR_PORT = 7 # Grove DHT sensor digital port
DHT_SENSOR_TYPE = 0 # Grove DHT sensor sensor type (0 = DHT11 = blue one = part
                    # of GrovePi+ Starter Kit, 1 = white one)
UPDATE_DISPLAY_FREQUENCY = 7 # Interval after that the display can be updated
                             # in seconds


lastAirQuality = 0 # last air quality measurement
lastAirQualityText = "" # last air quality text representation
lastHumidity = 0 # last humidity measurement
lastTemperature = 0 # last temperature measurement
lastDisplayUpdate = 0 # last display update time


# Setup the air quality sensor on its analog port.
pinMode(AIR_SENSOR_PORT, "INPUT")

# Set background color of screen.
setRGB(0, 128, 64)


def getAirQualityText():
    """Get a text representation of the last air quality measurement."""
    global lastAirQuality
    if lastAirQuality > 700:
        return "High pollution"
    elif lastAirQuality > 300:
        return "Low pollution"
    else:
        return "No pollution"

def updateAirQuality(airQuality):
    """Update the air quality value. Returns false if the value is NaN or not
    new, true otherwise."""
    global lastAirQuality
    if math.isnan(airQuality) or airQuality == lastAirQuality:
        return False
    lastAirQuality = airQuality
    return True

def updateAirQualityText():
    """Update the air quality text representation. Returns false if the new
    text is not new, true otherwise."""
    global lastAirQuality, lastAirQualityText
    newText = getAirQualityText()
    if newText == lastAirQualityText:
        return False
    lastAirQualityText = newText
    return True

def updateHumidity(humidity):
    """Update the humidity value. Returns false if the value is NaN or not new,
    true otherwise."""
    global lastHumidity
    if math.isnan(humidity) or humidity == lastHumidity:
        return False
    lastHumidity = humidity
    return True

def updateTemperature(temperature):
    """Update the temperature value. Returns false if the value is NaN or not
    new, true otherwise."""
    global lastTemperature
    if math.isnan(temperature) or temperature == lastTemperature:
        return False
    lastTemperature = temperature
    return True


while True:
    try:
        # Get temperature and humidity from the DHT sensor.
        [temperature, humidity] = dht(DHT_SENSOR_PORT, DHT_SENSOR_TYPE)
        airQuality = analogRead(AIR_SENSOR_PORT)

        # Uncomment the three following lines if you want to see the
        # measurements on the console.
        #print("temperature = " + str(temperature) + "C\thumidity = "
        #      + str(humidity) + "%")
        #print("air quality = " + str(airQuality))

        # Update the measurements.
        updateAirQuality(airQuality)
        isAirQualityTextUpdated = updateAirQualityText()
        isHumidityUpdated = updateHumidity(humidity)
        isTemperatureUpdated = updateTemperature(temperature)

        # Update the screen if needed at maximum at UPDATE_DISPLAY_FREQUENCY.
        if (time.time() - lastDisplayUpdate > UPDATE_DISPLAY_FREQUENCY) \
            and (isAirQualityTextUpdated or isHumidityUpdated
            or isTemperatureUpdated):
            setText(str(round(lastTemperature,1)) + "C      "
                + str(round(lastHumidity,1)) + "%\n" + lastAirQualityText)
            lastDisplayUpdate = time.time()

    except (IOError, TypeError) as e:
        setText("Error\nPlease restart!")
        print("Error: " + str(e))
        sys.exit()
