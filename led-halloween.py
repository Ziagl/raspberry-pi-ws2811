#!/usr/bin/env python3
import time
from neopixel import *
import sys
import datetime
from random import randrange

# LED strip configuration:
LED_COUNT      = 100     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


def colorShow(strip, color):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()
        
# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, rand = 0, wait_ms=50):
    if rand == 0:
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
    elif rand == 1:
        for i in range(strip.numPixels()):
            strip.setPixelColor(strip.numPixels() - i, color)
            strip.show()
            time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

# Main program logic follows:
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Argument for runtime in hours needed for example: python scriptname.py 2')
        exit()
    else:
        # Create NeoPixel object with appropriate configuration.
        strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        # Intialize the library (must be called once before other functions).
        strip.begin()

        loop = True
        starttime = datetime.datetime.now()
        
        now = datetime.datetime.now()
        print ('start time: '+str(now.hour)+':'+str(now.minute))
        print ('end time: '+str(now.hour + int(sys.argv[1])) + ':' + str(now.minute))
        
        while loop:
            type = randrange(3)
            print(type)
            if type == 0:
                count = 0
                rand = randrange(2)
                while count < 20:
                    colorWipe(strip, Color(0, 255, 60), rand, 0)  # Red wipe
                    colorWipe(strip, Color(0, 0, 0), rand, 0)  # Red wipe
                    count = count + 1
            elif type == 1:
                count = 0;
                while count < 100:
                    colorShow(strip, Color(0, 255, 60))  # Red wipe
                    time.sleep(1/50.0)
                    colorShow(strip, Color(0, 0, 0))  # Red wipe
                    time.sleep(1/50.0)
                    count = count + 1
            elif type == 2:
                colorShow(strip, Color(0, 255, 60))  # Red wipe
                time.sleep(60.0)
            
            now = datetime.datetime.now()
            if now.hour >= starttime.hour + int(sys.argv[1]):
                loop = False

        # reset LED strip (all LEDs off)
        colorWipe(strip, Color(0,0,0), 10)
