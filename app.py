from tkinter import *
import webbrowser #import des pages webs
import yfinance as yf
from pandas_datareader import data as pdr

import requests_html
from yahoo_fin.stock_info import *

#fonction de webbrowser
def open_web():
	webbrowser.open_new("https://youtu.be/IwH5bUm9ChU")

def clearFrame():
    # destroy all widgets from frame
    for widget in frame_buttons.winfo_children():
       widget.destroy()
    
    # this will clear frame and frame will be empty
    # if you want to hide the empty panel then
    frame_buttons.pack_forget()

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

def gainers():
	print(get_day_gainers())

def loosers():
	print(get_day_losers())

def variations_menu():
	# Creation des boutons de selections 
	frame_buttons = Frame(window, bg = 'grey', bd=1)

	#Ajouter bouton 1 {pady = marge en y, fill = remplissage en X}
	button1 = Button(frame_buttons, text="Plus gros gains", font=("Courrier", 10), bg = 'white', fg = 'black', command=gainers)
	button1.pack(pady=10, fill=X)

	#Ajouter bouton 2
	button2 = Button(frame_buttons, text="Plus grosses pertes", font=("Courrier", 10), bg = 'white', fg = 'black', command=loosers)
	button2.pack(pady=10, fill=X)

	frame_buttons.pack(expand=YES, fill='both', padx = 150, pady = 80)





#creer une premiere fenetre
window = Tk()

# Personnalisation de la fenetre
window.title("My Application")
window.geometry("720x480")
window.minsize(480, 360)
window.iconbitmap("logo.ico")
window.config(background='grey')

#Creer une frame
frame_title = Frame(window, bg = 'grey')
frame_buttons = Frame(window, bg = 'grey')

# Ajout d'un titre
label_title = Label(frame_title, text = "PROJET PYTHON FOR FINANCE", font=("Courrier", 20), bg = 'grey', fg = 'black')
label_title.pack()

# Ajouter d'un sous titre
label_subtitle = Label(frame_title, text = "Alexandre PEREZ - Alec GUESSOUS", font=("Courrier", 10), bg = 'grey', fg = 'black')
label_subtitle.pack()

#Ajouter bouton 1 {pady = marge en y, fill = remplissage en X}
button1 = Button(frame_buttons, text="Les plus grosses variations de marché", font=("Courrier", 10), bg = 'white', fg = 'black', command=combine_funcs(clearFrame, variations_menu) )
button1.pack(pady=10, fill=X)

#Ajouter bouton 2
button2 = Button(frame_buttons, text="Boutton 2", font=("Courrier", 10), bg = 'white', fg = 'black', command=clearFrame)
button2.pack(pady=10, fill=X)

#Ajouter bouton 3
button3 = Button(frame_buttons, text="Boutton 3", font=("Courrier", 10), bg = 'white', fg = 'black', command=clearFrame)
button3.pack(pady=10, fill=X)

# ajouter la frame
frame_title.pack(expand=YES, side='top')
frame_buttons.pack(expand=YES, fill='both', padx = 150, pady = 80)





#Afficher
window.mainloop()

