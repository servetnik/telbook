from tkinter import *
import sqlite3

n = 2

window = Tk()
window.geometry("400x400")

def save():
    fname = ent_fname.get()
    lname = ent_lname.get()
    tel = ent_tel.get()
    
    if tel.isdigit():
        user = (str(fname), str(lname), tel)
        cur.execute("INSERT INTO users1 VALUES(?, ?, ?);", user)
        conn.commit()
def find():
    global lbl
    fname = ent_fname.get()
    lname = ent_lname.get()
    user = (str(fname), str(lname))
    
    cur.execute("""SELECT *
    FROM users1 
    WHERE fname = ? 
    OR lname = ?;""", user)
    
    all_results = cur.fetchall()
    lbl.configure(text = all_results)
    lbl.pack()

def delete():
    global lbl
    lbl.configure(text='')

conn = sqlite3.connect('base1.db')
cur = conn.cursor()

ent_fname = Entry()
ent_lname = Entry()
ent_tel = Entry()
btn_save = Button(window,text='save',command = save)
btn_find = Button(window,text='find',command = find)
btn_del = Button(window,text='delete',command = delete)
lbl = Label(text='', fg="#111")

ent_fname.pack()
ent_lname.pack()
ent_tel.pack()
btn_save.pack()
btn_find.pack()
btn_del.pack()