from django.shortcuts import render
from pyrebase import initialize_app

config = {
    "apiKey": "AIzaSyBYTCvg38-xxOwGcy9IE0taxQn-XluolTE",
    "authDomain": "cities-handbook.firebaseapp.com",
    "databaseURL": "https://cities-handbook-default-rtdb.firebaseio.com",
    "projectId": "cities-handbook",
    "storageBucket": "cities-handbook.appspot.com",
    "messagingSenderId": "167329826518",
    "appId": "1:167329826518:web:fc6d404f7ffb2c91252b77",
    "measurementId": "G-7WFBB3ZQFD"
}

firebase = initialize_app(config)
authe = firebase.auth()
database = firebase.database()

def main(request, cityKey:str = "paris"):
    cards = database.child("cards").get().val()
    city = database.child('cities').child(cityKey).get().val()
    for i in range(len(city["sights"])):
        city["sights"][i]["reversed"] = i%2 == 1
    data = {
        "cards": cards,
        "city": city
    }
    return render(request, "index.html", context = data)