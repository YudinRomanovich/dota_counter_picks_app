import tkinter as tk
import main

from tkinter import ttk

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
    # Получаем список выбранных героев
    list_of_enemy_picks = list(lbox.get(0, tk.END))
    # Получаем список ссылок на страницы контр-героев
    list_of_enemy_pick_urls = main.get_list_of_url_enemy_pick(list_of_enemy_picks)
    # Получаем список контр-героев
    list_of_counter_picks = main.get_all_counter_enemy_hero(list_of_enemy_pick_urls)
    # Очищаем поле с контр-героями
    lbox2.delete(0, tk.END)
    # Создаем словарь для хранения количества контр-героев
    counter_dict = {}
    # Подсчитываем количество каждого контр-героя в списке
    for item in list_of_counter_picks:
        if item in counter_dict:
            counter_dict[item] += 1
        else:
            counter_dict[item] = 1
    # Сортируем словарь по количеству контр-героев в порядке убывания
    sorted_counter_dict = sorted(counter_dict.items(), key=lambda x: x[1], reverse=True)
    # Отображаем контр-героев в списке
    for item, count in sorted_counter_dict:
        if count > 1:
            lbox2.insert(tk.END, f"{item} ({count})")
        else:
            lbox2.insert(tk.END, item)


# Создаем главное окно приложения
win = tk.Tk()
# Устанавливаем размеры окна
win.geometry('600x500')
# Устанавливаем заголовок окна
win.title('Dota counter picks')
# Устанавливаем иконку окна
win.iconphoto(False, tk.PhotoImage(file='dota2.png'))

# Создаем стиль оформления окна
win.configure(bg='white')

# List виджет для отображения выбранных героев
lbox = tk.Listbox(win, bg="white", fg="black", font=("Helvetica", 14, "bold"))
lbox.grid(row=0, column=0, padx=15, pady=50, stick='n')

# Entry виджет для ввода названия героя
name_of_enemy_pick_hero = tk.Entry(win, bg="white", fg="black", font=("Helvetica", 14))
name_of_enemy_pick_hero.grid(row=0, column=0, padx=15, pady=15, stick='n')
# Привязываем обработчик событий к полю ввода для добавления героя в список выбранных героев при нажатии Enter
name_of_enemy_pick_hero.bind('<Return>', update_listbox)

# Button виджет для обработки выбранных героев и отображения контр-героев
process_button = tk.Button(win, text="Process Enemy Picks", command=process_enemy_picks, bg="blue", fg="white", font=("Helvetica", 14))
process_button.grid(row=1, column=0, padx=15, pady=15, stick='n')

# List виджет для отображения контр-героев
lbox2 = tk.Listbox(win, bg="white", fg="black", font=("Helvetica", 14))
lbox2.grid(row=0, column=1, padx=15, pady=15, stick='we')

# Запускаем главный цикл приложения
win.mainloop()