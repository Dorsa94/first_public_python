from tkinter import *
from converter_class import *

def send_data():
    data_from = list_from.get(ACTIVE)
    data_to = list_to.get(ACTIVE)
    value = int(EN_from.get())
    
    obj = converter1(data_from , data_to , value)
    
    
    EN_to.delete(0,END)
    EN_to.insert(END , obj.convert_kon())



window1 = Tk()
window1.title('converter ')
window1.resizable(0,0)

my_font = ('Arial_rounded' ,11)

# from
Label(window1, text='From' , font=my_font).grid(row=0,column=0,sticky=W )
EN_from = Entry(window1 , font=my_font)
EN_from.grid(row=1,column=0,sticky=W ,padx=5, pady=2)
list_from = Listbox(window1, font=my_font , exportselection=False)
list_from.grid(row=2,column=0,sticky=W ,padx=5, pady=5)
list_from.insert(END , 'gr')
list_from.insert(END , 'kg')
list_from.insert(END , 'ton')


# to
Label(window1, text='To', font=my_font).grid(row=0,column=1,sticky=W)
EN_to = Entry(window1, font=my_font)
EN_to.grid(row=1,column=1,sticky=E ,padx=5, pady=2)
list_to = Listbox(window1, font=my_font, exportselection=False)
list_to.grid(row=2,column=1,sticky=E,padx=5, pady=5)
list_to.insert(END , 'gr')
list_to.insert(END , 'kg')
list_to.insert(END , 'ton')


# btn
btn = Button(window1 , text='covert', font=my_font , bd=5 ,command=send_data) 
btn.grid(row=3 ,column=0,padx=5,pady=5 ,columnspan=2, sticky=W+E)





window1.mainloop()