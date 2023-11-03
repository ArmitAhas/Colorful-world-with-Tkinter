from tkinter import *
from translate import Translator

# translator to farsi
translator = Translator(to_lang="fa")

window = Tk()


def trans():
    word1 = word.get()
    tran = translator.translate(word1)
    lab1.configure(text="Translation: {} ".format(tran))


window.configure(bg='#D6CDA4')
window.title("TRANSLATOR")

lab = Label(window, text="Enter text", bg='#D6CDA4', fg='#1C6758', font=24)
lab.pack()

word = Entry(window, bg='#3D8361', fg='#D6CDA4', font=15)
word.pack(ipadx=20, ipady=20)

Button(window, text='Translate', bg='#1C6758', fg='#D6CDA4', font=20, command=trans).pack(ipadx=15, ipady=10, pady=5)

lab1 = Label(window, text=': Translation', bg='#D6CDA4', fg='#1C6758', font=22)
lab1.pack(pady=5)


window.geometry('500x250')
window.resizable(height=False, width=False)
window.mainloop()
