#step1 : import
from tkinter import *

#step2 : gui interaction
window = Tk()
window.geometry('350x400')
window.title('Calculator')

#step3 : adding input
e = Entry(window , width = 25, font = ('Arial', 20),highlightbackground='black', borderwidth=5)
e.place(x=10, y=10)

#functions
def click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    
def clear():
    e.delete(0, END)
    
def add():
    first_number = e.get()
    global f_num
    global math
    math = 'addition'
    f_num = float(first_number)
    e.delete(0, END)
    
def subtract():
    first_number = e.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = float(first_number)
    e.delete(0, END)
    
def multiply():
    first_number = e.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = float(first_number)
    e.delete(0, END)
    
def divide():
    first_number = e.get()
    global f_num
    global math
    math = 'division'
    f_num = float(first_number)
    e.delete(0, END)
    
def equal():
    second_number = e.get()
    e.delete(0, END)
    
    if math == 'addition':
        e.insert(0, f_num + float(second_number))
        
    if math == 'subtraction':
        e.insert(0, f_num - float(second_number))
        
    if math == 'multiplication':
        e.insert(0, f_num * float(second_number))
        
    if math == 'division':
        e.insert(0, f_num / float(second_number))
        



#Buttons
b = Button(window, text='1', width=12, height=2, command= lambda: click(1))
b.place(x=10, y=80)

b = Button(window, text='2', width=12, height=2, command= lambda: click(2))
b.place(x= 120, y= 80)

b = Button(window, text='3', width=12, height=2, command= lambda: click(3))
b.place(x=230, y=80)

#step4 : adding more buttons
b = Button(window, text='4', width=12, height=2, command= lambda: click(4))
b.place(x=10, y=120)

b = Button(window, text='5', width=12, height=2, command= lambda: click(5))
b.place(x=120, y=120)

b = Button(window, text='6', width=12, height=2, command= lambda: click(6))
b.place(x=230, y=120)

b = Button(window, text='7', width=12, height=2, command= lambda: click(7))
b.place(x=10, y=160)

b = Button(window, text='8', width=12, height=2, command= lambda: click(8))
b.place(x=120, y=160)

b = Button(window, text='9', width=12, height=2, command= lambda: click(9))
b.place(x=230, y=160)

b = Button(window, text='0', width=12, height=2, command= lambda: click(0))
b.place(x=10, y=200)

b = Button(window, text='+', width=12, height=2, command= lambda: add())
b.place(x=230, y=200)

b = Button(window, text='-', width=12, height=2, command= lambda: subtract())
b.place(x=120, y=200)

b = Button(window, text='.', width=12, height=2, command= lambda: click('.'))
b.place(x=120, y=240)

b = Button(window, text='/', width=12, height=2, command= lambda: divide())
b.place(x=230, y=240)

b = Button(window, text='*', width=12, height=2, command= lambda:  multiply())
b.place(x=10, y=240)


b = Button(window, text='=', width=20, height=2,background='green', command= lambda: equal())
b.place(x=180, y=300)

b = Button(window, text='Clear', width=20, height=2, background='red', command= lambda: clear())
b.place(x=10, y=300)


#mainloop
mainloop()