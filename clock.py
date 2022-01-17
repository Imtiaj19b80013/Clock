from tkinter import Label, Tk
from tkinter.ttk import *
#from time import strftime
import datetime
fm=Tk()
fm.title("Clock")

Label=Label(fm,font=('calibri',40,'bold'),background="purple",foreground='white')
Label.grid(row=0,column=1)
Label.pack(anchor='center')

def time():
    clock= datetime.datetime.now().strftime('%H:%M:%S')
    Label.config(text=clock)
    Label.after(1000,time)

time()
fm.mainloop()
