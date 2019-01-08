
# KIWI.PY
# VERSION 1.2 BETA

# KIWI PROJECT
# EDVILME 2018
# DEVELOPED FOR CTRL+ALT+TEC

## ASSEMBLING INSTRUCTIONS
## ASSEMBLING INSTRUCTIONS - CONNECTIONS [DEVICE:PI]

### KEYPAD
#### 1:7
#### 2:11
#### 3:13
#### 4:15
#### 5:31
#### 6:33
#### 7:35
#### 8:37

### LCD SCREEN
#### k:GND
#### A:5V
#### D7:8
#### D6:7
#### D5:12
#### D4:16
#### E:20
#### RW:GND
#### RS:21
#### V0:GND
#### VSS:GND
#### VDD:5V


## import libraries
import pyrebase
import subprocess
import schedule
import time
import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO
import os
import signal
import sys
from threading import Thread
import webbrowser
import datetime

## CONFIG
## config - pyrebase
config = {
  "apiKey": "AIzaSyCTC5VTiUENrzDSVstB5ex98BxCDP9tMB4",
  "authDomain": "kiwi-d38bd.firebaseapp.com",
  "databaseURL": "https://kiwi-d38bd.firebaseio.com",
  "storageBucket": "kiwi-d38bd.appspot.com",
  "serviceAccount": "serviceAccountKey.json"
}

firebase = pyrebase.initialize_app(config)

## config - lcd screen
lcd_rs = 21
lcd_en = 20
lcd_d4 = 16
lcd_d5 = 12
lcd_d6 = 7
lcd_d7 = 8
lcd_backlight = 4
lcd_columns = 16
lcd_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

## config - keypad
#GPIO.setmode(GPIO.BOARD)
keypad_keys = [
	["1", "2", "3", "A"],
	["4", "5", "6", "B"],
	["7", "8", "9", "C"],
	["*", "0", "#", "D"]
]
#keyboard_col_pins = [15, 13, 11, 7] FOR MODE GPIO.BOARD
keyboard_col_pins = [22, 27, 17, 4]
#keyboard_row_pins = [37, 35, 33, 31] FOR MODE GPIO.BOARD
keyboard_row_pins = [26, 19, 13, 6]

for j in range(4):
	GPIO.setup(keyboard_col_pins[j], GPIO.OUT)
	GPIO.output(keyboard_col_pins[j], 1)
for i in range(4):	
	GPIO.setup(keyboard_row_pins[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)



## METHODS (INPUT)
## methods - keypad input (DEPRECATED IN V.0.9)
def keypadInput():
	try:
		isTyping=True
		keyboardReturn = ""
		while(isTyping):
			for j in range(4):
				GPIO.output(keyboard_col_pins[j],0)
				for i in range(4):
					if GPIO.input(keyboard_row_pins[i]) == 0:
						if keypad_keys[i][j] == "#":
							isTyping = False
							break
						elif keypad_keys[i][j] == "*":
							keyboardReturn = keyboardReturn[:-1]
						else:
							keyboardReturn = keyboardReturn + keypad_keys[i][j] 
						
						lcd.clear()
						lcd.message(keyboardReturn)
						while(GPIO.input(keyboard_row_pins[i])==0):
							pass
				GPIO.output(keyboard_col_pins[j],1)
		return keyboardReturn
	except KeyboardInterrupt:
		GPIO.cleanup()

## methods - camera input
def qrInput():
	qrReturn=None
	while p.poll() is None:
		qrReturn = p.stdout.readline()
		break
	lcd.clear()
	lcd.message(qrReturn)
	return qrReturn[:-1]



## methods - camera and keypad input
def multiInput():
	isRecording=True
	inputReturn=''
	try:
		while(isRecording):
			for j in range(4):
				GPIO.output(keyboard_col_pins[j], 0)
				for i in range(4):
					if returnedQR != '':
						inputReturn = returnedQR
						isRecording=False
						lcd.clear()
						lcd.message(inputReturn)
						time.sleep(3)
						break
					elif GPIO.input(keyboard_row_pins[i]) == 0:
						if keypad_keys[i][j]=='#':
							isRecording=False
							break
						elif keypad_keys[i][j]=='*':
							inputReturn=inputReturn[:-1]
						else:
							inputReturn=inputReturn+keypad_keys[i][j]
						lcd.clear()
						lcd.message(inputReturn)
						while(GPIO.input(keyboard_row_pins[i])==0):
							pass
				GPIO.output(keyboard_col_pins[j],1)
		return inputReturn
	except KeyboardInterrupt:
		GPIO.cleanup()


returnedQR=''
def liveQR():
	global returnedQR
	p = subprocess.Popen('/usr/bin/zbarcam --raw --prescale=200x200',shell=True, stdout=subprocess.PIPE)
	while p.poll() is None:
		returnedQR = p.stdout.readline()[:-1]
		break


def chronDeleteFiles():
	print("Deleting...")
	allFiles = firebase.database().child("files").get()
	for file in allFiles:
		firebase.storage().child(file.key()).delete(file.key())
		firebase.database().child("files/"+file.key()).remove()

def main():
	liveQRthread = Thread(target=liveQR)
	liveQRthread.start()
	userID = 'a01023646@itesm.mx'
	lcd.clear()
	lcd.message("CTRL+ALT+TEC\n")
	lcd.message("KIWI")
	time.sleep(2)
	lcd.clear()
	lcd.message("ID O CODIGO QR")
	#docID = raw_input("Ingrese el ID: ")
	#try:
	docID = multiInput()
	lcd.clear()
	lcd.message("Bajando...")
	#time.sleep(5)
	try:
		print docID
		print len(docID)
		firebase.storage().child(docID).download(docID)
		pagesCount=12
		subprocess.call(["lp", docID])
		lcd.clear()
		lcd.message("Imprimiendo...")
		time.sleep(10)
		os.remove( docID)
		##	!ADD TO RASPBERRY PI
		webbrowser.open("https://ctrl-alt-tec.github.io/Kiwi/api.html?USER="+userID+"&PAGES="+pagesCount+"&KEY=iruKHi4qAih4kg0fvDHbMNfvPBa2&TIMESTAMP="+time.mktime(datetime.datetime.now().timetuple()))
	except Exception as e:
		lcd.clear()
		lcd.message("Perdoname pero no\nOcurrio un error")
		time.sleep(2)
		lcd.clear()
		lcd.message("Reiniciando...")
		time.sleep(1)
		print(str(e))
	lcd.clear()
	lcd.message("Gracias por usar Kiwi")

schedule.every().day.at("23:45").do(chronDeleteFiles)

while(True):
	schedule.run_pending()
	time.sleep(1)
	main()

## -- END OF CODE (223 LINES) -- JAN 7 2019
