from tkinter import *


allnum = ""
def operation(var) :
    global allnum
    allnum = allnum + str(var)
    display.set(allnum)

def equal() :
    total = str(eval(allnum))
    display.set(total)

def clear() :
    global allnum
    allnum = ""
    display.set("")



window = Tk()
window.configure(bg='#F5E8C7')
window.title("CAlCULATOR")


display = StringVar()
numbers = Entry(window,bg='#F5E8C7',fg='#6F4C5B',font=20,state="disabled",textvariable=display)
numbers.grid(columnspan=10,ipady=35,ipadx=50)

btn1 = Button(window,text='7',bg='#9E7777',fg='#DEBA9D',font=10,command=lambda: operation(7))
btn1.grid(row=2,column=1,ipadx=27,ipady=27)

btn2 = Button(window,text='8',bg='#9E7777',fg='#DEBA9D',font=10,command=lambda: operation(8))
btn2.grid(row=2,column=2,ipadx=27,ipady=27)

btn3 = Button(window,text='9',bg='#9E7777',fg='#DEBA9D',font=10,command=lambda: operation(9))
btn3.grid(row=2,column=3,ipadx=27,ipady=27)

btn4 = Button(window,text=' +',bg='#9E7777',fg='#DEBA9D',font=10,command=lambda: operation('+'))
btn4.grid(row=2,column=4,ipadx=27,ipady=27)

btn5 = Button(window,text='4',bg='#9E7777',fg='#DEBA9D',font=10,command=lambda: operation(4))
btn5.grid(row=3,column=1,ipadx=27,ipady=27)

btn6 = Button(window,text='5',bg='#9E7777',fg='#DEBA9D',font=10,command=lambda: operation(5))
btn6.grid(row=3,column=2,ipadx=27,ipady=27)

btn7 = Button(window,text='6',bg='#9E7777',fg='#DEBA9D',font=10,command=lambda: operation(6))
btn7.grid(row=3,column=3,ipadx=27,ipady=27)

btn8 = Button(window,text=' _',bg='#9E7777',fg='#DEBA9D',font=10,command=lambda: operation('-'))
btn8.grid(row=3,column=4,ipadx=27,ipady=27)

btn9 = Button(window,text='1',bg='#9E7777',fg='#DEBA9D',font=10,command=lambda: operation(1))
btn9.grid(row=4,column=1,ipadx=27,ipady=27)

btn10 = Button(window,text='2',bg='#9E7777',fg='#DEBA9D',font=10,command=lambda: operation(2))
btn10.grid(row=4,column=2,ipadx=27,ipady=27)

btn11 = Button(window,text='3',bg='#9E7777',fg='#DEBA9D',font=10,command=lambda: operation(3))
btn11.grid(row=4,column=3,ipadx=27,ipady=27)

btn12 = Button(window,text='X',bg='#9E7777',fg='#DEBA9D',font=10,command=lambda: operation('*'))
btn12.grid(row=4,column=4,ipadx=27,ipady=27)

btn13 = Button(window,text='. ',bg='#9E7777',fg='#DEBA9D',font=10,command=lambda: operation('.'))
btn13.grid(row=5,column=1,ipadx=27,ipady=27)

btn14 = Button(window,text='0',bg='#9E7777',fg='#DEBA9D',font=10,command=lambda: operation(0))
btn14.grid(row=5,column=2,ipadx=27,ipady=27)

btn15 = Button(window,text='=',bg='#9E7777',fg='#DEBA9D',font=10,command=equal)
btn15.grid(row=5,column=3,ipadx=27,ipady=27)

btn16 = Button(window,text='-:-',bg='#9E7777',fg='#DEBA9D',font=10,command=lambda: operation('/'))
btn16.grid(row=5,column=4,ipadx=27,ipady=27)

btn17 = Button(window,text='CLEAR',bg='#9E7777',fg='#FF0303',font=10,command=clear)
btn17.grid(row=6,ipadx=125,columnspan=20,ipady=20)


window.geometry('310x500')
window.resizable(width=False,height=False)
window.mainloop()