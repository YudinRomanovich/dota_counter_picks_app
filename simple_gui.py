
import tkinter as tk
from tkinter import ttk

from main import *

win = tk.Tk()
win.geometry('400x500')
win.title('Dota counter picks')
win.iconphoto(False, tk.PhotoImage(file='dota2.png'))

# List виджет
lbox = tk.Listbox(win) # создаем список виджет
lbox.grid(row=2, column=0, padx=15, pady=15, stick='we')  # располагаем его с помощью grid
lbox2 = tk.Listbox(win) # создаем список виджет
lbox2.grid(row=2, column=1, padx=15, pady=15, stick='we')  # располагаем его с помощью grid



# Entry
name_of_enemy_pick_hero = tk.Entry(win)
name_of_enemy_pick_hero.grid(row=1, column=0, padx=15, stick='we')

# Labels
tk.Label(win, text="Введите имя героя").grid(row=0, column=0, padx=15, stick='we')
tk.Label(win, text="Выбирай этих героев").grid(row=1, column=1, padx=15, stick='we')


win.grid_columnconfigure(0, minsize=200)
win.grid_columnconfigure(1, minsize=200)

win.mainloop()