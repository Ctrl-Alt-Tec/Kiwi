# Kiwi
Porject Kiwi is a printing vending machine that allows printing of files through the internet using an hexadecimal code


# KIWI-CLIENT

## 1.- UPLOAD TO WEBSITE
http://ctrl-alt-tec.github.io/Kiwi/index.html

* Upload using Firebase

* Generate random string

* Name file in firebase after string

# KIWI-RASPBERY PI (UBUNTU)

## 2.- DOWNLOAD FROM FIREBASE
* Listen to doc id (inputVar)

* Install firebase-cli tools
    
    > let downloadURL = await firebase.storage().ref(inputVar).getDownloadUrl();
    
* In directory
    > sudo wget -O /documents/inputVar downloadURL

## 3.- PRINT
* LP
    > sudo lp /documents/inputVar

## 4.- REMOVE FILE
* REMOVE
    > suro rm -rf /documents/inputVar
