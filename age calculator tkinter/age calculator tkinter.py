from  tkinter import *
from tkinter import messagebox
import datetime


def cal():
    global age
    year_age = int(year.get())
    month_age =int(month.get())

    time2 = datetime.date.today()

    if month_age > time2.month:
        age=(int(time2.year) - year_age) - 1
    else:
        age=int(time2.year) - year_age


def show():
    name_age = name.get()
    messagebox.showinfo("Show Age"," {}, your Age is {}".format(name_age,age))


window = Tk()
window.configure(bg="#ffde22")

window.title("AGE CALCULATE ")

Label(window , text="AGE CALCULATE",font=('Goudy stout',26),bg="#ffde22",fg="#ff414e").pack(anchor=N)

Label(window,text="Enter your name ",bg="#ff414e",fg="#ffde22",font=("Showcard Gothic",18)).pack(padx=20,pady=5,ipady=5,ipadx=5)
name = Entry(window)
name.pack(pady=10,ipadx=50)

Label(window,text="what is your birthday date ?" ,bg="#ff414e",fg="#ffde22",font=18).pack(pady=10,ipadx=50)

Label(window,text="Enter Year : " ,bg="#ffde22",fg="#ff414e",font=12).pack()
year = Entry(window)
year.pack()

Label(window,text="Enter Month : ",bg="#ffde22",fg="#ff414e",font=12).pack()
month = Entry(window)
month.pack()

Label(window,text="Enter Day : ",bg="#ffde22",fg="#ff414e",font=12).pack()
day = Entry(window)
day.pack(pady=5)

btn1 = Button(window,text="ENTER",font=('Stencil',20),bg="#ff8928",fg="#ffffff",command=cal)
btn1.pack(pady=8)
btn2 = Button(window,text="CALCULATE",font=('Stencil',20),bg="#ff8928",fg="#ffffff",command=show)
btn2.pack(pady=8)





window.geometry('550x500')
window.resizable(width=False,height=False)

window.mainloop()
