import tkinter as tk
from PIL import Image, ImageTk
from urllib.request import urlopen
import json
from io import BytesIO

cards = json.load(urlopen('https://api.fabdb.net/cards?per_page=99999'))

mainWindow = tk.Tk()
mainWindow.geometry("546x762")
mainWindow.title("Current card")
images = []

def fetchCard():
    userInput = input("New card >")

    if (userInput == "exit"):
        mainWindow.quit()
    else:
        for card in cards["data"]:
            if card["name"].lower() == userInput.lower():
                url = card["image"].split('?')[0]
                rawData = urlopen(url).read()
                im = Image.open(BytesIO(rawData))
                image = ImageTk.PhotoImage(im)
                label1 = tk.Label(mainWindow, image=image)
                label1.place(x=0, y=0)
                images.append(image)
                break
        mainWindow.after(0, fetchCard)

if __name__ == "__main__":
    mainWindow.after(0, fetchCard)
    tk.mainloop()
