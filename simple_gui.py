
# Импортируем модуль tkinter
import tkinter as tk
from collections import Counter
import main

# Функция для добавления героя в список выбранных героев
def update_listbox(event):
    # Получаем значение из поля ввода
    enemy_pick = name_of_enemy_pick_hero.get()
    # Добавляем значение в список выбранных героев
    lbox.insert(tk.END, enemy_pick)
    # Очищаем поле ввода
    name_of_enemy_pick_hero.delete(0, tk.END)

# Функция для обработки выбранных героев и отображения контр-героев
def process_enemy_picks():
    # Получаем лист героев
    list_of_enemy_picks = list(lbox.get(0, tk.END))
    # Передаем их в функцию и получаем 
    list_of_enemy_pick_urls = main.get_list_of_url_enemy_pick(list_of_enemy_picks)
    list_of_counter_picks = main.get_all_counter_enemy_hero(list_of_enemy_pick_urls)
    lbox2.delete(0, tk.END)
    counter_dict = Counter(list_of_counter_picks)
    sorted_counter_dict = sorted(counter_dict.items(), key=lambda x: x[1], reverse=True)
    for item, count in sorted_counter_dict:
        if count > 1:
            lbox2.insert(tk.END, f"{item} ({count/3})")
        else:
            lbox2.insert(tk.END, item)

# Создаем главное окно приложения
win = tk.Tk()

# Устанавливаем размеры окна
win.geometry('500x400')

# Убираем изменение ширины высоты окна  
win.resizable(False, False)

# Устанавливаем заголовок окна
win.title('Dota counter picks')

# Устанавливаем иконку окна
win.iconphoto(False, tk.PhotoImage(file='dota2.png'))

# Создаем стиль оформления окна
win.configure(bg='black')

# List виджет для отображения выбранных героев
lbox = tk.Listbox(win, bg="black", fg="white", font=("Helvetica", 14, "bold"))
lbox.grid(row=0, column=0, padx=15, pady=50, stick='s')

tk.Label(win, text="Counter Picks", font=("Helvetica", 16), bg="black", fg="red").grid(row=0, column=1, stick='n')
tk.Label(win, text="Enter hero name", font=("Helvetica", 16), bg="black", fg="red").grid(row=0, column=0, stick='n')

# Entry виджет для ввода названия героя
name_of_enemy_pick_hero = tk.Entry(win, bg="black", fg="white", font=("Helvetica", 14))
name_of_enemy_pick_hero.grid(row=0, column=0, padx=15, pady=25, stick='n')
# Привязываем обработчик событий к полю ввода для добавления героя в список выбранных героев при нажатии Enter
name_of_enemy_pick_hero.bind('<Return>', update_listbox)

# Button виджет для обработки выбранных героев и отображения контр-героев
process_button = tk.Button(win, text="Process Enemy Picks", command=process_enemy_picks, bg="red", fg="white", font=("Helvetica", 14))
process_button.grid(row=1, column=0, padx=15, stick='s')

# List виджет для отображения контр-героев
lbox2 = tk.Listbox(win, bg="black", fg="white", font=("Helvetica", 14))
lbox2.grid(row=0, column=1, padx=15, pady=15, stick='we')

# Запускаем главный цикл приложения
win.mainloop()
