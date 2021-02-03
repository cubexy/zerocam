import LCD_Config
import LCD_1in44
from var import *
import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep
from io import BytesIO

import time
from PIL import Image,ImageDraw,ImageFont,ImageColor

version = "v.0.1"

setup_gpio()
camera = PiCamera()
camera.resolution=(128,128)
camera.start_preview()

disp = LCD_1in44.LCD()
LCD_ScanDir = LCD_1in44.SCAN_DIR_DFT
disp.LCD_Init(LCD_ScanDir)
disp.LCD_Clear()

width = 128
height = 128

print("Activating camera")
sleep(2)
print("Sleep time exited")

def show_menu(width,height):
    image = Image.open("splashscreen.jpg")
    draw = ImageDraw.Draw(image)
    draw.rectangle((9, 59, 56, 106), outline=0, fill=(96,96,96))
    draw.rectangle((71, 59, 119, 106), outline=0, fill=(96,96,96))
    draw.multiline_text((19, 70), "Photo\nMode", fill=(255, 255, 255), align="center")
    draw.multiline_text((78, 70), "Webcam\nMode", fill=(255, 255, 255), align="center")
    draw.text((5,5), version, fill=(255,255,255))
    disp.LCD_ShowImage(image , 0, 0)
    selector=-1
    selected=False
    while selected == False:
        if GPIO.input(KEY_LEFT_PIN) == 0:
            # If LEFT input pressed:
            draw.rectangle((71, 59, 119, 106), outline=0, fill=(96, 96, 96))
            draw.rectangle((9, 59, 56, 106), outline=0, fill=(58, 176, 255))
            draw.multiline_text((19, 70), "Photo\nMode", fill=(255, 255, 255), align="center")
            draw.multiline_text((78, 70), "Webcam\nMode", fill=(255, 255, 255), align="center")
            selector = 0
            disp.LCD_ShowImage(image, 0, 0)
            sleep(0.2)
        if GPIO.input(KEY_RIGHT_PIN) == 0:
            # If RIGHT input pressed:
            draw.rectangle((9, 59, 56, 106), outline=0, fill=(96, 96, 96))
            draw.rectangle((71, 59, 119, 106), outline=0, fill=(58, 176, 255))
            draw.multiline_text((19, 70), "Photo\nMode", fill=(255, 255, 255), align="center")
            draw.multiline_text((78, 70), "Webcam\nMode", fill=(255, 255, 255), align="center")
            selector = 1
            disp.LCD_ShowImage(image, 0, 0)
            sleep(0.2)
        if GPIO.input(KEY_PRESS_PIN) == 0:
            # If input selector pressed:
            if selector == 0:
                draw.rectangle((9, 59, 56, 106), outline=0, fill=(0, 0, 0))
                disp.LCD_ShowImage(image, 0, 0)
                sleep(0.2)
                return "PHOTO_MODE"
            elif selector == 1:
                draw.rectangle((71, 59, 119, 106), outline=0, fill=(0, 0, 0))
                disp.LCD_ShowImage(image, 0, 0)
                sleep(0.2)
                return "WEBCAM_MODE"



def mode_test(width,height):
    image = Image.new('RGB', (width, height))
    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    disp.LCD_ShowImage(image, 0, 0)
    draw.rectangle((11, 30, 48, 68), outline=0, fill="ffffff")
    draw.rectangle((),outline=0,fill="1a2744")
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

def mode_camera():
    # button_test(width,height)
    image_c = Image.open("splashscreen_camera.jpg")
    draw = ImageDraw.Draw(image_c)
    disp.LCD_ShowImage(image_c, 0, 0)
    back=False
    while back==False:
        if GPIO.input(KEY2_PIN) == 0:  # button is pressed
            stream = BytesIO()
            camera.capture(stream, format='jpeg')
            stream.seek(0)
            img = Image.open(stream)
            img = img.transpose(Image.FLIP_TOP_BOTTOM)
            img = img.transpose(Image.FLIP_LEFT_RIGHT)
            disp.LCD_ShowImage(img, 0, 0)
            sleep(1.5)
            stream.flush()
            stream.close()
            disp.LCD_ShowImage(image_c, 0, 0)

def mode_webinterface():
    print("WIP")

try:
    m = show_menu(128,128)
    if m == "PHOTO_MODE":
        mode_camera()
    elif m == "WEBCAM_MODE":
        mode_webinterface()
except KeyboardInterrupt:
    print("\nEnded Program")
    disp.LCD_Clear()
    camera.close()