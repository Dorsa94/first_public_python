from tkinter import *
from tkinter import filedialog

def save_File():
    final_save = filedialog.asksaveasfile(mode='w' , defaultextension='.txt')
    txt = text.get(1.0,END)
    final_save.write(txt)
    final_save.close()

def open_File():
    final_open= filedialog.askopenfile(mode='r')
    txt = final_open.read()
    text.insert(INSERT , txt)
    final_open.close()

def clear_File():
    text.delete(1.0 , END)

window1 = Tk()
window1.title('notepad')
window1.geometry('800x500')
window1.resizable(0,0)
text = Text(window1)
text.pack(fill='both' , expand=True)

menubar = Menu(window1)

filemenu = Menu(menubar , tearoff=0)
filemenu.add_command(label='save' , command=save_File)
filemenu.add_command(label='open' , command=open_File)
filemenu.add_command(label='exit' , command=window1.quit)
menubar.add_cascade(menu=filemenu , label='file')

editmenu = Menu(menubar , tearoff=0)
editmenu.add_command(label='clear' , command=clear_File)

menubar.add_cascade(menu=editmenu, label='edit')

window1.config(menu=menubar)


window1.mainloop()