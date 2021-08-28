from tkinter import *

def clicked():
    lbl.configure(text="Я же просил...")

    
window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('900x500')
lbl = Label(window, text="Привет", font=("Arial Bold", 10))  
lbl.grid(column=0, row=0)
txt = Entry(window,width=10)  
txt.grid(column=1, row=0)
#rec=rectangle()
btn = Button(window, text="Не нажимать!", bg="white", fg="black",command=clicked)
btn.grid(column=0, row=1)
window.mainloop()


