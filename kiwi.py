# KIWI.PY
# VERSION 0.9 BETA

# KIWI PROJECT
# EDVILME 2018
# DEVELOPED FOR CTRL+ALT+TEC

## import libraries
import pyrebase
import subprocess
import schedule
import time
import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO


## config
## config - pyrebase
config={
	"apiKey": "AIzaSyCTC5VTiUENrzDSVstB5ex98BxCDP9tMB4",
	"authDomain": "kiwi-d38bd.firebaseapp.com",
	"databaseURL": "https://kiwi-d38bd.firebaseio.com",
	"storageBucket": "kiwi-d38bd.appspot.com",
	"serviceAccount": "serviceAccountKey.json"
}
firebase = pyrebase_initialize_app(config)

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
GPIO.setmode(GPIO.board)
keypad_keys = [
	["1", "2", "3", "A"],
	["4", "5", "6", "B"],
	["7", "8", "9", "C"],
	["*", "0", "#", "D"]
]
keyboard_col_pins = [15, 13, 11, 7]
keyboard_row_pins = [37, 35, 33, 31]

for i in range(4):
	GPIO.setup(keyboard_col_pins[i], GPIO.OUT)
	GPIO.output(keyboard_col_pins[i], 1)
	
	GPIO.setup(keyboard_row_pins[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)


## methods
## methods - keypad
############################################## check
def keypadInput():
	try:
		keyboardReturn = ""
		while(True):
			for j in range(4):
				GPIO.output(keyboard_col_pins[j],0)
				for i in range(4):
					if GPIO.input(keyboard_row_pins[i]) == 0:
						if keypad_keys[i][j] == "#":
							break
						else:
							keyboardReturn = keyboardReturn.concat( keypad_keys[i][j] )
						while(GPIO.input(keyboard_row_pins[i)==0):
							pass
				GPIO.output(keyboard_col_pins[j],1)
		return keyboardReturn
	except KeyboardInterrupt:
		GPIO.cleanup()


def chronDeleteFiles():
	print("Deleting...")
	allFiles = firebase.database().child("files").get()
	for file in allFiles:
		firebase.storage().child(file.key()).delete(file.key())
		firebase.database().child("files/"+file.key()).remove()

def main():
	lcd.clear()
	lcd.message("KIWI \n")
	lcd.message("By CTRL+ALT+TEC \n")

	lcd.message("Ingrese el ID")
	#docID = raw_input("Ingrese el ID: ")
	docID = keyboardInput()
	try:
		firebase.storage().child(docID).download(docID)

		subprodess.call(["lp", docID])
		lcd.message("Printing...")

		subprocess.call(["sudo rm", "-rf", docID])
	catch:
		lcd.message("Perdoname pero no \n")
		lcd.message("Ocurrio un error")


schedule.every().day.at("23:45").do(chronDeleteFiles)

while(True):
	schedule.run_pending()
	time.sleep(1)
	main()

