# import LCD_Config
import RPi.GPIO as GPIO
from PIL import Image, ImageDraw

import LCD_1in44
from var import *

setup_gpio()

disp = LCD_1in44.LCD()
LCD_ScanDir = LCD_1in44.SCAN_DIR_DFT
disp.LCD_Init(LCD_ScanDir)
disp.LCD_Clear()

width = 128
height = 128
image = Image.new('RGB', (width, height))

button_display_test()