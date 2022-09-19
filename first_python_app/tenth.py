from tkinter import *
import requests

global_test =  requests.get('https://api.coinlore.net/api/tickers/')
x = global_test.json()

usdt = requests.get('http://api.navasan.tech/latest/?api_key=freeH1njcMsLTHCJFd9haMcGI1ZdNK3g&item=usdt')
usdt = usdt.json()
usdt = usdt['usdt']['value']


symbol = dict()
for i in x['data']:
    symbol[i['symbol']]= i['price_usd']

all_symbol = list(symbol.keys())

def update(data):
    list_form.delete(0, END)
    for i in data:
        list_form.insert(END, i)

def price(e):
    data_from = list_form.get(ACTIVE)
    price_entry.delete(0,END)
    price_entry.insert(END , symbol[data_from])
    
def price_farsi(e):
    data_from = list_form.get(ACTIVE)
    price_entry.delete(0,END)
    price_entry.insert(END , float(symbol[data_from]) * float(usdt))
            
    
def symbolOut(e):
    searching.delete(0,END)
    searching.insert(0, list_form.get(ACTIVE))
    
    
def check_symbol(e):
    typed = searching.get()
    if typed == '' :
        data = all_symbol
    else:
        data = []
        for i in all_symbol:
            if typed.upper() in i:
                data.append(i)
    update(data)
            
window1 = Tk()
window1.title('Exchange')
window1.geometry('500x400')
window1.resizable(0,0)
my_font = ('Arial_rounded' ,11)

Label(window1, text='search' ,font=my_font).pack(fill='both' , expand=True)

searching = Entry(window1, font=my_font)
searching.pack(fill='both' , expand=True)
searching.bind('<KeyRelease>', check_symbol)

list_form = Listbox(window1 , font=my_font ,exportselection=False)
list_form.pack(fill='both' , expand=True)
update(all_symbol)
list_form.bind('<<ListboxSelect>>', symbolOut)


Label(window1 , text= 'price' , font=my_font ).pack(fill='both' , expand=True)

price_entry = Entry(window1, font=my_font)
price_entry.pack(fill='both' , expand=True)

btn = Button(window1, bd=5,text='Get the price',font=my_font )
btn.pack(fill='both' , expand=True)
btn.bind('<ButtonPress-1>' ,  price)
btn.bind('<ButtonPress-3>' ,  price_farsi)


window1.mainloop()