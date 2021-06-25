from tkinter import *
from tkinter import messagebox
from random import randint
import requests
import json
import webbrowser
root = Tk()
root.geometry("455x250")

#variables pour pas répéter 50 fois la même chose
ButtonColor = '#d9b3ff'
fontStyle = 'Helvetica'
fontSize = 16

root.configure(bg='#b3ffff')
root.eval('tk::PlaceWindow . center')

def getRandomCountry(urlcountry):
    request = requests.get(urlcountry)
    countries = request.json()
    random_country = countries[randint(0,len(countries) - 1)]['translations']['fr']
    if len(random_country) < 40:
        myLabel = Label(text="Le pays est :\n" + random_country, bg=ButtonColor, width=24, heigh=2, font=(fontStyle,10), relief=GROOVE, bd=2)
    else:
        myLabel = Label(text="Le pays est :\n" + random_country, bg=ButtonColor, width=38, heigh=3, font=(fontStyle,6), relief=GROOVE, bd=2)
    myLabel.grid_forget()
    myLabel.grid(row=3, column=1, padx=10, pady=5)

def urlAll():
    url = 'https://restcountries.eu/rest/v2/all'
    getRandomCountry(url)

def europe():
    url = 'https://restcountries.eu/rest/v2/region/europe'
    getRandomCountry(url)

def asia():
    url = 'https://restcountries.eu/rest/v2/region/asia'
    getRandomCountry(url)

def afrique():
    url = 'https://restcountries.eu/rest/v2/region/africa'
    getRandomCountry(url)

def amerique():
    url = 'https://restcountries.eu/rest/v2/region/americas'
    getRandomCountry(url)

def oceanie():
    url = 'https://restcountries.eu/rest/v2/region/oceania'
    getRandomCountry(url)

allCountryB = Button(root, bg=ButtonColor, width=35, font=(fontStyle,fontSize), relief=GROOVE, bd=2, text="Tout les pays",command = urlAll)
europeB = Button(root, bg=ButtonColor, width=16, font=(fontStyle,fontSize), relief=GROOVE, bd=2, text="Europe",command = europe)
asieB = Button(root, bg=ButtonColor, width=16, font=(fontStyle,fontSize), relief=GROOVE, bd=2, text="Asie",command = asia)
afriqueB = Button(root, bg=ButtonColor, width=16, font=(fontStyle,fontSize), relief=GROOVE, bd=2, text="Afrique",command = afrique)
ameriqueB = Button(root, bg=ButtonColor, width=16, font=(fontStyle,fontSize), relief=GROOVE, bd=2, text="Amerique",command = amerique)
oceanieB = Button(root, bg=ButtonColor, width=16, font=(fontStyle,fontSize), relief=GROOVE, bd=2, text="Oceanie",command = oceanie)

allCountryB.grid(row=0, columnspan=2, pady=16)
europeB.grid(row=1, column=0, padx=10, pady=8)
asieB.grid(row=1, column=1, padx=10, pady=5)
afriqueB.grid(row=2, column=1, padx=10, pady=5)
ameriqueB.grid(row=2, column=0, padx=10, pady=5)
oceanieB.grid(row=3, column=0, padx=10, pady=5)
root.mainloop()