import pyrebase
import subprocess
import schedule
import time


config = {
  "apiKey": "qwertyuiop",
  "authDomain": "qwertyuiop",
  "databaseURL": "qwertyuiop",
  "storageBucket": "qwertyuiop",
  "serviceAccount": "qwertyuiop"
}

firebase = pyrebase.initialize_app(config)

def main():     
        ## GET ID
        print("BIENVENIDO A KIWI...")
        print("POR CTRL-ALT-TEC")
        print("")
        docID = raw_input("INGRESE EL ID: ")
        docURL = firebase.storage().child(docID).get_url(1)
        #firebase.storage().child(docID).download(docID)

        ## PRINT
        #subprocess.call(["lp", docID])
        #print("Printing...")

        ## DELETE
        #subprocess.call(["sudo rm", "-rf", docID])

def deleteFilesDaily():
        print( "Deleting..." )
        all_files = firebase.database().child("files").get()
        for file in all_files.each():
                firebase.storage().child(file.key()).delete(file.key())
                firebase.database().child("files/"+file.key()).remove()

schedule.every().day.at("23:45").do(deleteFilesDaily)


while True:
        #main()
        schedule.run_pending()
        time.sleep(1)
        main()
