import tkinter as tk
import sqlite3

connection = sqlite3.connect('users.db')
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS orderss (order_number INTEGER PRIMARY KEY, manager INTEGER, calender INTEGER, printer INTEGER, cuter INTEGER, seamstresses INTEGER)")
connection.commit()

order_checkbox_states = {}  # Словарь для хранения состояний чекбоксов для каждого заказа
checkbox_vars = []  # Список переменных для состояния чекбоксов


def submit_order_number():
    order_number = int(entry.get())
    try:
        cursor.execute("INSERT INTO orderss (order_number, manager, calender, printer, cuter, seamstresses) VALUES (?, ?, ?, ?, ?, ?)",
                       (order_number, checkbox_vars[0].get(), checkbox_vars[1].get(), checkbox_vars[2].get(), checkbox_vars[3].get(), checkbox_vars[4].get()))
        connection.commit()


        print(f"Заказ с номером успешно добавлен в базу данных")
    except sqlite3.Error as error:
        print(f"Ошибка при добавлении заказа: {error}")

    clear_fields()  # Очищаем поля ввода и сбрасываем состояние чекбоксов


def show_status():
    order_number = entry.get()
    try:
        cursor.execute("SELECT manager, calender, printer, cuter, seamstresses FROM orders WHERE order_number = ?", (order_number,))
        row = cursor.fetchone()
        if row is not None:
            state = [bool(item) for item in row]
            print(f"Статус заказа {order_number}:")
            print(state)
        else:
            print(f"Для заказа статус не найден")
    except sqlite3.Error as error:
        print(f"Ошибка при получении статуса заказа: {error}")


def clear_fields():
    entry.delete(0, tk.END)  # Очищаем поле ввода
    for var in checkbox_vars:
        var.set(0)  # Сбрасываем состояние чекбокса

def close_connection():
    connection.close()

root = tk.Tk()
root.title("Введите номер заказа")
root.geometry('200x270')

label = tk.Label(root, text="Введите номер заказа:")
label.pack()

entry = tk.Entry(root)
entry.pack()

checkboxes = ["менеджер", "каландер", "печать", "резщики", "швеи"]  # Замените на ваши варианты
for checkbox_text in checkboxes:
    var = tk.IntVar()
    checkbox_vars.append(var)
    checkbox = tk.Checkbutton(root, text=checkbox_text, variable=var)
    checkbox.pack()

submit_button = tk.Button(root, text="Подтвердить", command=submit_order_number)
submit_button.pack()

status_button = tk.Button(root, text="Статус", command=show_status)
status_button.pack()

root.mainloop()














