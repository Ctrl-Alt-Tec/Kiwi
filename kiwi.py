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
  
  ## DOWNLOAD
  docURL = firebase.storage().child(docID).download(docID)
  
  ## GET PRICE AND CHECK IF PAYED
  
  ## PRINT
  subprocess.call(["lp", docID])
  
  ## REMOVE FILE
  subprocess.call(["sudo rm", "-rf", docID])
  
true=1
while true==1:
  main
