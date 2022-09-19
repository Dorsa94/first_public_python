from tkinter import *

def injuri():
    x = int(first.get()) + int(second.get()) 
    btn.config(bg='blue')
    answer.config(text=f'answer is : {x}')
    
    
def kie():
    print(choice.get())
    
def saveKone():
    with open('out' , 'w') as f :
        f.write(ad.get(1.0 , END))
        
        
def loadKone():
    with open('out') as f :
        x = f.read()
        if len(ad.get(1.0 , END)) < 2 :
            ad.insert(INSERT , x )   
 
            

window1 = Tk()
window1.title('Dorsa')
window1.geometry('900x900')

Label(window1,text="first number : ").pack()
first = Entry(window1)
first.pack()

Label(window1,text="second number : ").pack()
second = Entry(window1)
second.pack()


btn = Button(window1,text='add' , bd=5 ,width=20,command=injuri)
btn.pack()


answer = Label(window1)
answer.pack()


kiaHastan = [('male' , 'M') , ('female' , 'F')]
choice = StringVar()
choice.set("F")

for m,f in kiaHastan:
    Radiobutton(window1,text=m , value=f , variable=choice).pack()

btn = Button(window1,text='kie' , bd=5 ,width=5,command=kie)
btn.pack()


ad = Text(window1)
ad.pack()

btn1 = Button(window1,text='save' , command=saveKone)
btn1.pack()

btn2 = Button(window1,text='load' , command=loadKone)
btn2.pack()



window1.mainloop()