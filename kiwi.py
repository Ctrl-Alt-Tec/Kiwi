#!/usr/bin/python
import pyrebase
import subprocess

config={
  "apiKey": "apiKey",
  "authDomain": "authDomain",
  "databaseURL": "databaseURL",
  "storageBucket": "storageBucket"
}

def main():
  firebase = pyrebase.initialize_app(config)
  
  ## GET DOC ID
  docID = raw_input("Ingresa el código: ")
  docURL = firebase.storage().child(docID).get_url(1)
  
  ## # WARNING! USING SUDO WITH SHELL=TRUE
  subprocess.call("sudo wget -O "+docID+" "+docURL, shell=True)
  
  ## GET PRICE AND CHECK IF PAYED
  
  ## PRINT
  subprocess.call(["lp", docID])
  
true=1
while(true==1):
  main
