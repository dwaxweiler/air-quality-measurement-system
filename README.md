# Air quality measurement system

System based on Raspberry Pi and GrovePi to display temperature, humidity and other air quality parameters

Released under The MIT License, see LICENSE.txt file for more details

## Built with
* [Raspberry Pi 1 Model B](https://www.raspberrypi.org/products/model-b/)
* USB power adapter for the Pi
* [GrovePi+ board](https://www.dexterindustries.com/shop/grovepi-board/) (firmware version 1.2.7)
* [Grove RGB LCD display](http://wiki.seeed.cc/Grove-LCD_RGB_Backlight/)
* [Grove temperature and humidity (DHT) sensor ](http://wiki.seeedstudio.com/wiki/Grove_-_Temperature_and_Humidity_Sensor) or [Grove temperature and humidity (DHT) Pro sensor ](http://wiki.seeed.cc/Grove-Temperature_and_Humidity_Sensor_Pro/)
* [Grove air quality sensor](http://www.seeedstudio.com/wiki/Grove_-_Air_Quality_Sensor_v1.3)
* Lego bricks for the case

## Setup
It is expected that you have already [set up GrovePi on your Raspberry Pi](https://www.dexterindustries.com/GrovePi/get-started-with-the-grovepi/).
1. Connect the display and both sensors.
  * Connect the display to the port I2C-1.
  * Connect the DHT sensor to the port D7.
  * Connect the air quality sensor to the port A0.
2. Download the python script.
3. Depending on which DHT sensor you are using, you have to adapt the value assigned to `DHT_SENSOR_TYPE` at the beginning of the script.
Its comment explains more.
4. Run the script: `python air-quality-measurement-system.py`

## Example case
![Front of the case](front.jpg)
