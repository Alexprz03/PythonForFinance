from tkinter import *
import tkinter.ttk
import webbrowser
import numpy as np
from yahoo_fin import stock_info as si


def clearFrame():
    # destroy all widgets from frame
    for widget in frame.winfo_children():
       widget.destroy()
    
    frame.pack_forget()

def clearFrameTab():
	# destroy all widgets from labelFrame_tab
	for widget in labelFrame_tab.winfo_children():
		widget.destroy()
	labelFrame_tab.pack_forget()

def clearAllFrames():
	clearFrame()
	for widget in frame_title.winfo_children():
		widget.destroy()
	for widget in frame_back_menu.winfo_children():
		widget.destroy()

	frame_title.pack_forget()
	frame_back_menu.pack_forget()



def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

def functions_type():
	#VERIF TAILLE DU TABLEAU
	if var_text.get() > 0 and var_text.get() < 101:
		if type_ == "stock_gainers":
			tab = si.get_day_gainers()
		elif type_ == "stock_losers":
			tab = si.get_day_losers()
		elif type_ == "crypto":
			tab = si.get_top_crypto()
		else:
			print("error1")
		#convert in table
		tab = np.array(tab)
		affichage_tab(tab)


def set_type_gainers():
	global type_
	type_ = "stock_gainers"

def set_type_losers():
	global type_
	type_ = "stock_losers"

def set_type_crypto():
	global type_
	type_ = "crypto"

def convert_int_to_millions_string(valeur):
	valeur = round(valeur / 1000000, 3)
	string_valeur = str(valeur) + "M"

	return string_valeur

def convert_int_to_billions_string(valeur):
	valeur = round(valeur / 1000000000, 3)
	string_valeur = str(valeur) + "B"

	return string_valeur

def callback(url):
    webbrowser.open_new(url)

def taille_tab(): # saisir un nombre
	clearFrame()

	global var_text 
	var_text = IntVar()
	var_text.set(10)

	etiquette = Label(frame, text='Size of array (Need to be between 1 and 100) :', font=("Courrier", 15), bg = color_background, fg = 'black')
	etiquette.pack(pady = 10)

	ligne_texte = Entry(frame, textvariable = var_text, width=6)
	ligne_texte.pack(pady = 20)
	
	button = Button(frame, text = 'OK', command = functions_type)
	button.pack(ipadx=80, pady=20)

	frame.pack(expand=YES, fill='both', padx = 10, pady = 40)


def selectItem(a):
	global data
	curItem = tableau.focus()
	data = tableau.item(curItem)
	print(tableau.item(curItem)["text"])


def next_function():
	#Dividends
	print(data)
	#lien vers l'entreprise
	callback("https://finance.yahoo.com/quote/" + data["text"] + "?p=" + data["text"])


def insert_research():
	def verif_nom():
		# destroy all widgets from labelFrame_tab
		for widget in labelFrame_tab.winfo_children():
			widget.destroy()
			labelFrame_tab.pack_forget()
		#Functions
		symbole = ""
		compteur = 0
		global tableau
		tableau = tkinter.ttk.Treeview(labelFrame_tab, columns=('symbole', 'name'))
		#columns
		tableau.column('symbole', width=80, minwidth = 80, anchor = "center")
		tableau.column('name', width=200, minwidth = 200, anchor = "center")
		#Hending
		tableau.heading('symbole', text='Symbole')
		tableau.heading('name', text='Name')
		tableau['show'] = 'headings'
		tableau.bind('<ButtonRelease-1>', selectItem)

		if type_ == "crypto":
			tab = tab_crypto
		else:
			tab = tab_stocks

		for i in tab:
			if i[0].lower().startswith(var_text_string.get().lower()) == True or i[1].lower().startswith(var_text_string.get().lower()) == True:
				compteur = compteur + 1
				symbole = i[0]
				tableau.insert("", compteur, str(compteur), text = i[0], values = (i[0], i[1]))

		tableau.pack(side = 'left', ipadx = 160)
		
		button = Button(labelFrame_tab, text = 'Valider la selection', command = next_function)
		button.pack()

		labelFrame_tab.pack(fill ='both', expand = YES, padx = 50)



	clearFrame()

	global var_text_string
	labelFrame_tab = LabelFrame(frame, text="Stock list")
	var_text_string = StringVar()
	var_text_string.set("")

	etiquette = Label(frame, text='Entrer le Symbole de l`entreprise que vous recherchez :', font=("Courrier", 10), bg = color_background, fg = 'black')
	etiquette.pack()

	ligne_texte = Entry(frame, textvariable = var_text_string, width=20)
	ligne_texte.pack()
	
	button = Button(frame, text = 'Rechercher', command = verif_nom)
	button.pack(ipadx=80, pady=10)

	frame.pack(expand=YES, fill='both', padx = 10, pady = 40)


def affichage_tab(tab):
	clearFrame()
	compteur = 1

	#AFFICHE MESSAGE
	label_msg = Label(frame, text = "Results were generated a few mins ago. Pricing data is updated frequently. Currency in USD", font=("Courrier", 10), bg = color_background, fg = 'black')
	label_msg.pack(side = 'top', pady = 3)

	global tableau
	tableau = tkinter.ttk.Treeview(frame, columns=('compteur','symbol', 'name', 'price', 'change', 'varia', 'vol', 'Market_c', 'Circulating'))

	tableau.column('compteur', width=30, minwidth = 30, anchor = "center")
	tableau.column('symbol', width=80, minwidth = 80, anchor = "center")
	tableau.column('price', width=90, minwidth = 90, anchor = "center")
	tableau.column('change', width=90, minwidth = 90, anchor = "center")
	tableau.column('varia', width=100, minwidth = 100, anchor = "center")
	tableau.column('vol', width=110, minwidth = 110, anchor = "center")
	tableau.column('Market_c', width=110, minwidth = 110, anchor = "center")
	
	tableau.heading('compteur', text=' ')
	tableau.heading('symbol', text='Symbol')
	tableau.heading('name', text='Name')
	tableau.heading('price', text='Price')
	tableau.heading('change', text='Change')
	tableau.heading('varia', text='% Variation')
	tableau.heading('vol', text='Volume')
	tableau.heading('Market_c', text='Market Cap')
	tableau.heading('Circulating', text='Circulating Supply')
	tableau['show'] = 'headings'
	tableau.bind('<ButtonRelease-1>', selectItem)

	#insert data en fonction de la saisie precedente
	while compteur-1 < var_text.get():
		i = tab[compteur-1]
		array = np.array(i) #Conversion en tableau
		# Ajout du signe +
		if str(array[3])[0] != "-":
			sign3 = "+"
		else:
			sign3 = ""
		if str(array[4])[0] != "-":
			sign4 = "+"
		else:
			sign4 = ""
		if type_ == "stock_gainers" or type_ == "stock_losers":
			#Enregistrement si c'est un stock
			# Conversion des int
			volume = convert_int_to_millions_string(array[5])
			market_c = convert_int_to_billions_string(array[7])
			if compteur == 1:
				tableau.column('name', width=160, minwidth = 160)
				tableau.column('Circulating', width=0, minwidth = 0, anchor = "center")
			tableau.insert("", compteur, str(compteur), text = array[0], values = (compteur, array[0], array[1], array[2], sign3 + str(array[3]), sign4 + str(array[4]) + "%", volume, market_c))
		#enregistrement si c'est une crypto
		elif type_ =="crypto":
			if compteur == 1:
				tableau.column('name', width=100, minwidth = 100)
				tableau.column('Circulating', width=110, minwidth = 110, anchor = "center")
			tableau.insert("", compteur, str(compteur), text = array[0], values = (compteur, array[0], array[1], array[2], sign3 + str(array[3]), sign4 + str(array[4]) + "%",  str(array[6]),  str(array[5]), str(array[9])))
		else:
			print("error2")

		compteur = compteur+1

	tableau.pack(expand=YES, fill='both')

	button = Button(frame, text = 'Valider la selection', command = next_function)
	button.pack(side = 'bottom')

	frame.pack(expand=YES, fill='both', padx = 10, pady = 40)

def tab_crypto():
	new_tab = []
	tab = si.get_top_crypto()
	tab = np.array(tab)

	for i in tab:
		array = np.array(i)
		new_tab.append([array[0], array[1]])

	return new_tab

def tab_stocks():
	#Enregistrement des tickers
	ligne = []
	tab_stocks = []
	file = open("data/nasdaqlisted.txt", "r")
	lignes = file.readlines()
	for i in lignes:
		txt = i.split("|")
		txt2 = txt[1].split(" - ")
		if txt[0] != '' and txt2[0] != '':
			tab_stocks.append([txt[0], txt2[0]])
	file.close()
	return tab_stocks

def funA(): # Les plus grosses variations de marché

	clearFrame()
	
	#Ajouter bouton 1 {pady = marge en y, fill = remplissage en X}
	button1 = Button(frame, text="Bullish", font=("Courrier", 10), bg = 'white', fg = 'green', command = combine_funcs(set_type_gainers, taille_tab))
	button1.pack(padx=250, pady=5, fill = X, expand=YES)

	#Ajouter bouton 2
	button2 = Button(frame, text="Bearish", font=("Courrier", 10), bg = 'white', fg = 'red', command = combine_funcs(set_type_losers, taille_tab))
	button2.pack(padx=250, pady=5, fill = X, expand=YES)

	#Ajouter bouton 3
	button3 = Button(frame, text="Recherche", font=("Courrier", 10), bg = 'white', fg = 'black', command = combine_funcs(set_type_losers, insert_research))
	button3.pack(padx=250, pady=5, fill = X, expand=YES)


	frame.pack(expand=YES, fill=X, padx = 10, pady = 10, ipady=30)

def funB():
	#Clear la frame
	clearFrame()
	
	#Ajouter bouton 1 {pady = marge en y, fill = remplissage en X}
	button1 = Button(frame, text="Voir les plus grosses cryptos", font=("Courrier", 10), bg = 'white', fg = 'black', command = combine_funcs(set_type_crypto, taille_tab))
	button1.pack(padx=250, pady=5, fill = X, expand=YES)

	#Ajouter bouton 2
	button2 = Button(frame, text="Rechercher une crypto", font=("Courrier", 10), bg = 'white', fg = 'black', command = combine_funcs(set_type_crypto, insert_research))
	button2.pack(padx=250, pady=5, fill = X, expand=YES)

	frame.pack(expand=YES, fill=X, padx = 10, pady = 10, ipady=30)


def menu():
	clearAllFrames()
	# Ajout d'un titre
	label_title = Label(frame_title, text = "PROJET PYTHON FOR FINANCE", font=("Courrier", 20), bg = color_background, fg = 'black')
	label_title.pack()

	# Ajouter d'un sous titre
	label_subtitle = Label(frame_title, text = "Alexandre PEREZ - Alec GUESSOUS", font=("Courrier", 10), bg = color_background, fg = 'black')
	label_subtitle.pack()

	#Ajouter bouton 1 {pady = marge en y, fill = remplissage en X}
	button1 = Button(frame, text="Stock", font=("Courrier", 10), bg = 'white', fg = 'black', command = funA)
	button1.pack(padx=250, pady=5, fill = X, expand=YES)

	#Ajouter bouton 2
	button2 = Button(frame, text="Crypto", font=("Courrier", 10), bg = 'white', fg = 'black', command=funB)
	button2.pack(padx=250, pady=5, fill = X, expand=YES)

	#Ajouter bouton 3
	button3 = Button(frame, text="Quitter", font=("Courrier", 10), bg = 'white', fg = 'black', command=window.destroy)
	button3.pack(padx=250, pady=5, fill = X, expand=YES)

	button4 = Button(frame_back_menu, text="Retour au menu", font=("Courrier", 10), bg = 'white', fg = 'black', command=menu)
	button4.pack(side='right')

	# ajouter la frame
	frame_title.pack(side='top')
	frame.pack(expand=YES, fill=X, padx = 10, pady = 10, ipady=30)
	frame_back_menu.pack(fill=X, padx = 10, pady = 10, ipady = 10, side='bottom')



#variable de taille en global
color_background = '#f0f0f0'
#creer une premiere fenetre
window = Tk()

# Personnalisation de la fenetre
window.title("My Application")
window.geometry("860x550")
window.minsize(550, 400)
window.iconbitmap("img/logo.ico")
window.config(background=color_background)

tab_stocks = tab_stocks()
tab_crypto = tab_crypto()

#Creer une frame
frame_title = Frame(window, bg = color_background)
frame = Frame(window, bg = color_background)
frame_back_menu = Frame(window, bg = color_background)

menu()

#Afficher
window.mainloop()

