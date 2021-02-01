import LCD_Config
import LCD_1in44
from var import *
import RPi.GPIO as GPIO

import time
from PIL import Image,ImageDraw,ImageFont,ImageColor

setup_gpio()

disp = LCD_1in44.LCD()
LCD_ScanDir = LCD_1in44.SCAN_DIR_DFT
disp.LCD_Init(LCD_ScanDir)
disp.LCD_Clear()

width = 128
height = 128

def button_test(width,height):
    image = Image.new('RGB', (width, height))
    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)

    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    disp.LCD_ShowImage(image, 0, 0)

    while 1:
        # with canvas(device) as draw:
        if GPIO.input(KEY_UP_PIN) == 0:  # button is released
            draw.polygon([(20, 20), (30, 2), (40, 20)], outline=255, fill=0xff00)  # Up
            print("Up")
        else:  # button is pressed:
            draw.polygon([(20, 20), (30, 2), (40, 20)], outline=255, fill=0)  # Up filled

        if GPIO.input(KEY_LEFT_PIN) == 0:  # button is released
            draw.polygon([(0, 30), (18, 21), (18, 41)], outline=255, fill=0xff00)  # left
            print("left")
        else:  # button is pressed:
            draw.polygon([(0, 30), (18, 21), (18, 41)], outline=255, fill=0)  # left filled

        if GPIO.input(KEY_RIGHT_PIN) == 0:  # button is released
            draw.polygon([(60, 30), (42, 21), (42, 41)], outline=255, fill=0xff00)  # right
            print("right")
        else:  # button is pressed:
            draw.polygon([(60, 30), (42, 21), (42, 41)], outline=255, fill=0)  # right filled

        if GPIO.input(KEY_DOWN_PIN) == 0:  # button is released
            draw.polygon([(30, 60), (40, 42), (20, 42)], outline=255, fill=0xff00)  # down
            print("down")
        else:  # button is pressed:
            draw.polygon([(30, 60), (40, 42), (20, 42)], outline=255, fill=0)  # down filled

        if GPIO.input(KEY_PRESS_PIN) == 0:  # button is released
            draw.rectangle((20, 22, 40, 40), outline=255, fill=0xff00)  # center
            print("center")
        else:  # button is pressed:
            draw.rectangle((20, 22, 40, 40), outline=255, fill=0)  # center filled

        if GPIO.input(KEY1_PIN) == 0:  # button is released
            draw.ellipse((70, 0, 90, 20), outline=255, fill=0xff00)  # A button
            print("KEY1")
        else:  # button is pressed:
            draw.ellipse((70, 0, 90, 20), outline=255, fill=0)  # A button filled

        if GPIO.input(KEY2_PIN) == 0:  # button is released
            draw.ellipse((100, 20, 120, 40), outline=255, fill=0xff00)  # B button]
            print("KEY2")
        else:  # button is pressed:
            draw.ellipse((100, 20, 120, 40), outline=255, fill=0)  # B button filled

        if GPIO.input(KEY3_PIN) == 0:  # button is released
            draw.ellipse((70, 40, 90, 60), outline=255, fill=0xff00)  # A button
            print("KEY3")
        else:  # button is pressed:
            draw.ellipse((70, 40, 90, 60), outline=255, fill=0)  # A button filled
        disp.LCD_ShowImage(image, 0, 0)

try:
    button_test(width,height)
except KeyboardInterrupt:
    print("Ended Program")
