#!/usr/bin/python
import pyrebase
import subprocess
import schedule
import time


config = {
  "apiKey": "AIzaSyCTC5VTiUENrzDSVstB5ex98BxCDP9tMB4",
  "authDomain": "kiwi-d38bd.firebaseapp.com",
  "databaseURL": "https://kiwi-d38bd.firebaseio.com",
  "storageBucket": "kiwi-d38bd.appspot.com",
  "serviceAccount": "serviceAccountKey.json"
}

firebase = pyrebase.initialize_app(config)
schedule.every().day.at("23:45").do(deleteFilesDaily)
def main():
        ## GET ID
        docID = raw_input("ID: ");
        docURL = firebase.storage().child(docID).get_url(1)
        firebase.storage().child(docID).download(docID)

        ## PRINT
        subprocess.call(["lp", docID])




def deleteFilesDaily():
        print "Deleting..."
        all_files = firebase.database().child("files").get()
        for file in all_files.each():
                firebase.storage().child(file.key()).delete(file.key())
                firebase.database().child("files/"+file.key()).remove()

while True:
        #main()
        schedule.run_pending()
        time.sleep(1)
        main()#!/usr/bin/python
import pyrebase
import subprocess
import schedule
import time


config = {
  "apiKey": "AIzaSyCTC5VTiUENrzDSVstB5ex98BxCDP9tMB4",
  "authDomain": "kiwi-d38bd.firebaseapp.com",
  "databaseURL": "https://kiwi-d38bd.firebaseio.com",
  "storageBucket": "kiwi-d38bd.appspot.com",
  "serviceAccount": "serviceAccountKey.json"
}

firebase = pyrebase.initialize_app(config)
schedule.every().day.at("23:45").do(deleteFilesDaily)
def main():
        ## GET ID
        docID = raw_input("ID: ");
        docURL = firebase.storage().child(docID).get_url(1)
        firebase.storage().child(docID).download(docID)

        ## PRINT
        subprocess.call(["lp", docID])




def deleteFilesDaily():
        print "Deleting..."
        all_files = firebase.database().child("files").get()
        for file in all_files.each():
                firebase.storage().child(file.key()).delete(file.key())
                firebase.database().child("files/"+file.key()).remove()

while True:
        #main()
        schedule.run_pending()
        time.sleep(1)
        main()#!/usr/bin/python
import pyrebase
import subprocess
import schedule
import time


config = {
  "apiKey": "AIzaSyCTC5VTiUENrzDSVstB5ex98BxCDP9tMB4",
  "authDomain": "kiwi-d38bd.firebaseapp.com",
  "databaseURL": "https://kiwi-d38bd.firebaseio.com",
  "storageBucket": "kiwi-d38bd.appspot.com",
  "serviceAccount": "serviceAccountKey.json"
}

firebase = pyrebase.initialize_app(config)
schedule.every().day.at("23:45").do(deleteFilesDaily)
def main():
        ## GET ID
        docID = raw_input("ID: ");
        docURL = firebase.storage().child(docID).get_url(1)
        firebase.storage().child(docID).download(docID)

        ## PRINT
        subprocess.call(["lp", docID])




def deleteFilesDaily():
        print "Deleting..."
        all_files = firebase.database().child("files").get()
        for file in all_files.each():
                firebase.storage().child(file.key()).delete(file.key())
                firebase.database().child("files/"+file.key()).remove()

while True:
        #main()
        schedule.run_pending()
        time.sleep(1)
        main()#!/usr/bin/python
import pyrebase
import subprocess
import schedule
import time


config = {
  "apiKey": "AIzaSyCTC5VTiUENrzDSVstB5ex98BxCDP9tMB4",
  "authDomain": "kiwi-d38bd.firebaseapp.com",
  "databaseURL": "https://kiwi-d38bd.firebaseio.com",
  "storageBucket": "kiwi-d38bd.appspot.com",
  "serviceAccount": "serviceAccountKey.json"
}

firebase = pyrebase.initialize_app(config)
schedule.every().day.at("23:45").do(deleteFilesDaily)
def main():
        ## GET ID
        docID = raw_input("ID: ");
        docURL = firebase.storage().child(docID).get_url(1)
        firebase.storage().child(docID).download(docID)

        ## PRINT
        subprocess.call(["lp", docID])




def deleteFilesDaily():
        print "Deleting..."
        all_files = firebase.database().child("files").get()
        for file in all_files.each():
                firebase.storage().child(file.key()).delete(file.key())
                firebase.database().child("files/"+file.key()).remove()

while True:
        #main()
        schedule.run_pending()
        time.sleep(1)
        main()#!/usr/bin/python
import pyrebase
import subprocess
import schedule
import time


config = {
  "apiKey": "AIzaSyCTC5VTiUENrzDSVstB5ex98BxCDP9tMB4",
  "authDomain": "kiwi-d38bd.firebaseapp.com",
  "databaseURL": "https://kiwi-d38bd.firebaseio.com",
  "storageBucket": "kiwi-d38bd.appspot.com",
  "serviceAccount": "serviceAccountKey.json"
}

firebase = pyrebase.initialize_app(config)
schedule.every().day.at("23:45").do(deleteFilesDaily)
def main():
        ## GET ID
        docID = raw_input("ID: ");
        docURL = firebase.storage().child(docID).get_url(1)
        firebase.storage().child(docID).download(docID)

        ## PRINT
        subprocess.call(["lp", docID])




def deleteFilesDaily():
        print "Deleting..."
        all_files = firebase.database().child("files").get()
        for file in all_files.each():
                firebase.storage().child(file.key()).delete(file.key())
                firebase.database().child("files/"+file.key()).remove()

while True:
        #main()
        schedule.run_pending()
        time.sleep(1)
        main()#!/usr/bin/python
import pyrebase
import subprocess
import schedule
import time


config = {
  "apiKey": "AIzaSyCTC5VTiUENrzDSVstB5ex98BxCDP9tMB4",
  "authDomain": "kiwi-d38bd.firebaseapp.com",
  "databaseURL": "https://kiwi-d38bd.firebaseio.com",
  "storageBucket": "kiwi-d38bd.appspot.com",
  "serviceAccount": "serviceAccountKey.json"
}

firebase = pyrebase.initialize_app(config)
schedule.every().day.at("23:45").do(deleteFilesDaily)
def main():
        ## GET ID
        docID = raw_input("ID: ");
        docURL = firebase.storage().child(docID).get_url(1)
        firebase.storage().child(docID).download(docID)

        ## PRINT
        subprocess.call(["lp", docID])




def deleteFilesDaily():
        print "Deleting..."
        all_files = firebase.database().child("files").get()
        for file in all_files.each():
                firebase.storage().child(file.key()).delete(file.key())
                firebase.database().child("files/"+file.key()).remove()

while True:
        #main()
        schedule.run_pending()
        time.sleep(1)
        main()#!/usr/bin/python
import pyrebase
import subprocess
import schedule
import time


config = {
  "apiKey": "AIzaSyCTC5VTiUENrzDSVstB5ex98BxCDP9tMB4",
  "authDomain": "kiwi-d38bd.firebaseapp.com",
  "databaseURL": "https://kiwi-d38bd.firebaseio.com",
  "storageBucket": "kiwi-d38bd.appspot.com",
  "serviceAccount": "serviceAccountKey.json"
}

firebase = pyrebase.initialize_app(config)
schedule.every().day.at("23:45").do(deleteFilesDaily)
def main():
        ## GET ID
        docID = raw_input("ID: ");
        docURL = firebase.storage().child(docID).get_url(1)
        firebase.storage().child(docID).download(docID)

        ## PRINT
        subprocess.call(["lp", docID])




def deleteFilesDaily():
        print "Deleting..."
        all_files = firebase.database().child("files").get()
        for file in all_files.each():
                firebase.storage().child(file.key()).delete(file.key())
                firebase.database().child("files/"+file.key()).remove()

while True:
        #main()
        schedule.run_pending()
        time.sleep(1)
        main()#!/usr/bin/python
import pyrebase
import subprocess
import schedule
import time


config = {
  "apiKey": "AIzaSyCTC5VTiUENrzDSVstB5ex98BxCDP9tMB4",
  "authDomain": "kiwi-d38bd.firebaseapp.com",
  "databaseURL": "https://kiwi-d38bd.firebaseio.com",
  "storageBucket": "kiwi-d38bd.appspot.com",
  "serviceAccount": "serviceAccountKey.json"
}

firebase = pyrebase.initialize_app(config)
schedule.every().day.at("23:45").do(deleteFilesDaily)
def main():
        ## GET ID
        docID = raw_input("ID: ");
        docURL = firebase.storage().child(docID).get_url(1)
        firebase.storage().child(docID).download(docID)

        ## PRINT
        subprocess.call(["lp", docID])




def deleteFilesDaily():
        print "Deleting..."
        all_files = firebase.database().child("files").get()
        for file in all_files.each():
                firebase.storage().child(file.key()).delete(file.key())
                firebase.database().child("files/"+file.key()).remove()

while True:
        #main()
        schedule.run_pending()
        time.sleep(1)
        main()#!/usr/bin/python
import pyrebase
import subprocess
import schedule
import time


config = {
  "apiKey": "AIzaSyCTC5VTiUENrzDSVstB5ex98BxCDP9tMB4",
  "authDomain": "kiwi-d38bd.firebaseapp.com",
  "databaseURL": "https://kiwi-d38bd.firebaseio.com",
  "storageBucket": "kiwi-d38bd.appspot.com",
  "serviceAccount": "serviceAccountKey.json"
}

firebase = pyrebase.initialize_app(config)
schedule.every().day.at("23:45").do(deleteFilesDaily)
def main():
        ## GET ID
        docID = raw_input("ID: ");
        docURL = firebase.storage().child(docID).get_url(1)
        firebase.storage().child(docID).download(docID)

        ## PRINT
        subprocess.call(["lp", docID])




def deleteFilesDaily():
        print "Deleting..."
        all_files = firebase.database().child("files").get()
        for file in all_files.each():
                firebase.storage().child(file.key()).delete(file.key())
                firebase.database().child("files/"+file.key()).remove()

while True:
        #main()
        schedule.run_pending()
        time.sleep(1)
        main()#!/usr/bin/python
import pyrebase
import subprocess
import schedule
import time


config = {
  "apiKey": "AIzaSyCTC5VTiUENrzDSVstB5ex98BxCDP9tMB4",
  "authDomain": "kiwi-d38bd.firebaseapp.com",
  "databaseURL": "https://kiwi-d38bd.firebaseio.com",
  "storageBucket": "kiwi-d38bd.appspot.com",
  "serviceAccount": "serviceAccountKey.json"
}

firebase = pyrebase.initialize_app(config)
schedule.every().day.at("23:45").do(deleteFilesDaily)
def main():
        ## GET ID
        docID = raw_input("ID: ");
        docURL = firebase.storage().child(docID).get_url(1)
        firebase.storage().child(docID).download(docID)

        ## PRINT
        subprocess.call(["lp", docID])




def deleteFilesDaily():
        print "Deleting..."
        all_files = firebase.database().child("files").get()
        for file in all_files.each():
                firebase.storage().child(file.key()).delete(file.key())
                firebase.database().child("files/"+file.key()).remove()

while True:
        #main()
        schedule.run_pending()
        time.sleep(1)
        main()
