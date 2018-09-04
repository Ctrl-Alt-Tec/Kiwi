# Kiwi
Porject Kiwi is a printing vending machine that allows printing of files through the internet using an hexadecimal code


# KIWI-CLIENT

## 1.- UPLOAD TO WEBSITE
http://ctrl-alt-tec.github.io/Kiwi/index.html

* Upload using Firebase

* Generate random string

* Name file in firebase after string

* Generate qr code
     https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=Hola1

# KIWI-RASPBERY PI (UBUNTU)

## 2.- DOWNLOAD FROM FIREBASE

Using Python (Pyrebase)
download.py

    storage = firebase.storage()
    print(storage.child("images/example.jpg").get_url())
    
In directory
    
    sudo wget -O /documents/inputVar $(download.py)

## 3.- PRINT
* LP
    > sudo lp /documents/inputVar

## 4.- REMOVE FILE
* REMOVE
    > suro rm -rf /documents/inputVar
