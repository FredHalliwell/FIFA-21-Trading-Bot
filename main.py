import tkinter as tk
from tkinter import ttk

from threading import Thread

import bot

#define window
master = tk.Tk()
master.title("FIFA 21 Trading Bot")
master.geometry("350x100")

#text labels
blank = tk.Label(master, text= "").grid(row=2, column =0)
player_label = tk.Label(master, text= "Player name").grid(row=0, column =0)
Buy_price_label = tk.Label(master, text= "Buy price").grid(row=1, column =0)
Sell_price_label = tk.Label(master, text= "Sell price").grid(row=2, column =0)

#variables for entry GUI fields
player_variable = tk.StringVar()
buy_variable = tk.IntVar()
sell_variable = tk.IntVar()

#entry fields
player_entry = tk.Entry(master, textvariable = player_variable).grid(row=0, column = 1)
buy_entry = tk.Entry(master, textvariable = buy_variable).grid(row=1, column = 1)
sell_entry = tk.Entry(master, textvariable = sell_variable).grid(row=2, column = 1)


#to get text from boxes, use these
#put these as "start" button commands
#also which checkpoint is selected
#fuck user friendliness
player_variable.get()
buy_variable.get()
sell_variable.get()

#start and end buttons
start_button = tk.Button(master, text = "Launch", command = lambda : bot.auto_login()).grid(row=3, column = 0)
BPM_button = tk.Button(master, text = "BPM", command = lambda : bot.buy_and_sell_bronze_pack()).grid(row=3, column = 1)
sniper_button = tk.Button(master, text = "Snipe", command = lambda : bot.sniper()).grid(row=3, column = 2)

#function to run window
master.mainloop()

