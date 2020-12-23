import yfinance as yf
from pandas_datareader import data as pdr

import requests_html
from yahoo_fin.stock_info import *

# aapl= yf.Ticker("aapl")
# aapl

# aapl_historical = aapl.history(start="2020-11-01", end="2020-12-20", interval="1h")
# print(aapl_historical)

#data = yf.download("AMZN AAPL GOOG", start="2017-01-01",end="2017-04-30", group_by='tickers')
#print(data)

print(get_day_gainers())



#print(aapl.info['forwardPE'])

 def menu():
 	os.system("cls")
 	print("PROJET PYTHON FOR FINANCE ESILV 2020 - PEREZ Alexandre, GUESSOUS Alec\n\n")
 	print("Selectionner une action: ")
	print("1 - Plus grosse variation de marché")
	print("2 - ")

 	c = input()

 	if c == "1":
 		print("1 - Plus gros gain")
 		print("2 - Plus grosse perte")
 		c = input()

 		if c == "1":
 			print(get_day_gainers())
 		elif c == "2"
 			print(get_day_losers())


 	elif c == "2":

		
 	print("Appuyer sur entrer pour continuer")
 	input()

