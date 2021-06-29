from tkinter import *
from random import randint
import requests
import os, os.path
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
from tkinter import ttk
import webbrowser
from time import sleep

root = Tk()

app_width = 455
app_height = 550
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x1 = (screen_width / 2) - (app_width / 2)
y1 = (screen_height / 2) - (app_height / 2)
root.geometry(f'{app_width}x{app_height}+{int(x1)}+{int(y1)}')
root.title("Tkinter App By Miniflint")


ButtonColor = '#d9b3ff'
fontStyle = 'Helvetica'
fontSize = 16

def openweb(url, new):
    webbrowser.open(url,new=new)

root.configure(bg='#b3ffff')

def progressbarFunc(y, progressionText, colorHex):
    bar = ttk.Progressbar(root,orient="horizontal",length=425)
    bar.grid(row=4, columnspan=2, padx=10, pady=10)
    Label(root,text=progressionText, height=1, font=(fontStyle, 6), bg=colorHex).grid(row=4, columnspan=2)
    bar['value']=y
    root.update_idletasks()

def getRandomCountry(urlcountry):
    file_path = os.getcwd()
    FullPath = file_path + "\\Flag.png"
    
    x = 0
    while x != 100:
        if x <= 45:
            progressbarFunc(x, "Starting", "#e6e6e6")
        else:
            progressbarFunc(x, "Starting", "#00b300")
        sleep(0.02)
        x = x + randint(0, 5)
        if x >= 100:
            x = 100

    progressbarFunc(10, "Requesting json","#e6e6e6")
    #request the url and import it as dict
    request = requests.get(urlcountry)
    countries = request.json()
    
    #get a random country name in english
    progressbarFunc(60,"Requesting translations",'#00b300')
    random_country = countries[randint(0,len(countries) - 1)]['name']
    getCountryFlag = requests.get('https://restcountries.eu/rest/v2/name/'+ random_country)
    countryFlagJson = getCountryFlag.json()

    #search translation and flag
    progressbarFunc(80,"Requesting country Flag",'#00b300')
    country_TranslationFR = countryFlagJson[0]['translations']['fr']
    country_Flag = countryFlagJson[0]['flag']
    
    path = file_path + "\\Flag.svg" #
    
    #write image somewhere idk and close the file
    progressbarFunc(90,"Downloading flag", '#00b300')
    write_CountryFlag = requests.get(country_Flag)
    if os.path.exists(path):
        os.remove(path)
    file = open(path, "wb")
    file.write(write_CountryFlag.content)
    file.close()    

    #path to the file svg -> png / output : Flag.png
    drawing = svg2rlg(path)
    renderPM.drawToFile(drawing, FullPath, fmt="PNG")
    
    #put the image as button and that's it
    progressbarFunc(95,"Displaying flag", '#00b300')
    photo = PhotoImage(file=FullPath)
    photoimage = photo.subsample(2)
    button_Flag = Button(root, image=photoimage, width=420, heigh=245, relief=GROOVE, bd=2, command= lambda: openweb("https://fr.wikipedia.org/wiki/"+country_TranslationFR,1))
    
    if len(country_TranslationFR) < 40:
        labelCountry = Label(text="Le pays est :\n" + country_TranslationFR, bg=ButtonColor, width=25, heigh=2, font=(fontStyle,10), relief=GROOVE, bd=2)
    else:
        labelCountry = Label(text="Le pays est :\n" + country_TranslationFR, bg=ButtonColor, width=33, heigh=3, font=(fontStyle,7), relief=GROOVE, bd=2)
    labelCountry.grid(row=3, column=1, padx=10, pady=5)
    button_Flag.grid(row=5, columnspan=2)
    progressbarFunc(100, "Finish", '#00b300')
    root.mainloop()

allCountryB = Button(root, bg=ButtonColor, width=35, font=(fontStyle,fontSize), relief=GROOVE, bd=2, text="Tout les pays",command=lambda: getRandomCountry('https://restcountries.eu/rest/v2/all'))
europeB = Button(root, bg=ButtonColor, width=16, font=(fontStyle,fontSize), relief=GROOVE, bd=2, text="Europe",command=lambda: getRandomCountry('https://restcountries.eu/rest/v2/region/europe'))
asieB = Button(root, bg=ButtonColor, width=16, font=(fontStyle,fontSize), relief=GROOVE, bd=2, text="Asie",command=lambda: getRandomCountry('https://restcountries.eu/rest/v2/region/asia'))
afriqueB = Button(root, bg=ButtonColor, width=16, font=(fontStyle,fontSize), relief=GROOVE, bd=2, text="Afrique",command=lambda: getRandomCountry('https://restcountries.eu/rest/v2/region/africa'))
ameriqueB = Button(root, bg=ButtonColor, width=16, font=(fontStyle,fontSize), relief=GROOVE, bd=2, text="Amerique",command=lambda: getRandomCountry('https://restcountries.eu/rest/v2/region/americas'))
oceanieB = Button(root, bg=ButtonColor, width=16, font=(fontStyle,fontSize), relief=GROOVE, bd=2, text="Oceanie",command=lambda: getRandomCountry('https://restcountries.eu/rest/v2/region/oceania'))

allCountryB.grid(row=0, columnspan=2, pady=16, padx=10)
europeB.grid(row=1, column=0, padx=10, pady=8)
asieB.grid(row=1, column=1, padx=10, pady=5)
afriqueB.grid(row=2, column=1, padx=10, pady=5)
ameriqueB.grid(row=2, column=0, padx=10, pady=5)
oceanieB.grid(row=3, column=0, padx=10, pady=5)

root.mainloop()
