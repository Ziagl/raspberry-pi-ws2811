#!/usr/bin/env python3
import time
from neopixel import *
import sys
import datetime
import math

# LED strip configuration:
LED_COUNT      = 100     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

# colored lines
def colorlines(strip, color1, color2, lines, wait_ms=50):
    block = math.ceil(strip.numPixels() / lines)
    if lines % 2 != 0:
        block+=1
    count = 0
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        count+=1
        if count < block:
            strip.setPixelColor(i, color1)
        if count >= block:
            strip.setPixelColor(i, color2)
        if count == block * 2:
           count = 0
        strip.show()

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
        
        # 255 0 0 blue
        # 0 255 0 red
        # 0 0 255 green
        colorlines(strip, Color(0, 255, 0), Color(255, 255, 255), 3)
        
        while loop:
            now = datetime.datetime.now()
            if now.hour >= starttime.hour + int(sys.argv[1]):
                loop = False

        # reset LED strip (all LEDs off)
        colorWipe(strip, Color(0,0,0), 10)