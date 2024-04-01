import sqlite3
from tkinter import *
from tkinter import messagebox


class DB:
    def __init__(self):
        self.conn = sqlite3.connect("users0.db")
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS buy (id INTEGER PRIMARY KEY, product TEXT,comment TEXT, cost INTEGER, size INTEGER, price INTEGER)")
        self.cur.execute("UPDATE buy SET price = cost * size")
        self.conn.commit()


    def __del__(self):
        self.conn.close()


    def view(self):
        self.cur.execute("SELECT * FROM buy")
        rows = self.cur.fetchall()
        return rows

    def insert(self, product, comment, cost, size):
        cost = float(cost)
        size = int(size)
        price = cost * size
        self.cur.execute("INSERT INTO buy (product, comment, cost, size, price) VALUES (?, ?, ?, ?, ?)",
                         (product, comment, cost, size, price))
        self.conn.commit()

    def update(self, id, product, cost, size):
        self.cur.execute("UPDATE buy SET product=?, cost=?, size=? WHERE id=?", (product, cost, size, id))
        self.conn.commit()

    def delete(self, id):
        self.cur.execute("DELETE FROM buy WHERE id=?", (id,))
        self.conn.commit()

    def search(self, product="", cost="", size=""):
        price = cost * size
        self.cur.execute("SELECT * FROM buy WHERE product=?", (product, size, cost))
        # формируем полученные строки и возвращаем их как ответ
        rows = self.cur.fetchall()
        return rows


db = DB()


def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END, selected_tuple[4])


def view_command():
    list1.delete(0, END)
    for row in db.view():
        list1.insert(END, row)



def search_command():
    list1.delete(0, END)
    for row in db.search(product_text.get()):
        list1.insert(END, row)



def add_command():
    db.insert(product_text.get(), comment_text.get(), size_text.get(), cost_text.get())
    view_command()


def delete_command():
    db.delete(selected_tuple[0])
    view_command()


def update_command():
    db.update(selected_tuple[0], product_text.get())
    view_command()


window = Tk()
window.title("Заказы")
window.geometry('650x500')

def on_closing():
    if messagebox.askokcancel("", "Закрыть программу?"):
        window.destroy()


window.protocol("WM_DELETE_WINDOW", on_closing)

l1 = Label(window, text="Название")
l1.grid(row=0, column=0)

l2 = Label(window, text="Цена")
l2.grid(row=0, column=3)

l3 = Label(window, text="Размер")
l3.grid(row=1, column=0)

l4 = Label(window, text="Комментарий")
l4.grid(row=1, column=3)

product_text = StringVar()
e1 = Entry(window, textvariable=product_text)
e1.grid(row=0, column=1)

cost_text = IntVar()
e2 = Entry(window, textvariable=cost_text)
e2.grid(row=0, column=4)

size_text = IntVar()
e3 = Entry(window, textvariable=size_text)
e3.grid(row=1, column=1)

comment_text = StringVar()
e4 = Entry(window, textvariable=comment_text)
e4.grid(row=1, column=4)

price_text = IntVar()

list1 = Listbox(window, height=25, width=65)
list1.grid(row=2, column=0, rowspan=5, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=3, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)


list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text="Посмотреть все", width=12, command=view_command)
b1.grid(row=2, column=4)

b2 = Button(window, text="Поиск", width=12, command=search_command)
b2.grid(row=3, column=4)

b3 = Button(window, text="Добавить", width=12, command=add_command)
b3.grid(row=4, column=4)

b4 = Button(window, text="Обновить", width=12, command=update_command)
b4.grid(row=5, column=4)

b5 = Button(window, text="Удалить", width=12, command=delete_command)
b5.grid(row=6, column=4)

b6 = Button(window, text="Закрыть", width=12, command=on_closing)
b6.grid(row=7, column=4)

view_command()

window.mainloop()
