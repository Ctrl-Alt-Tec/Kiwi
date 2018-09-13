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
    storage = firebase.storage()
    storage.delete("ywuka2.jpeg")

main