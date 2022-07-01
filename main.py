from tkinter import *
import os
from PIL import ImageTk, Image
from functions import register

#Main screen
master = Tk()
master.title("PURSUE BANK")

master.configure(background="white")
#Image import
img = Image.open('unnamed.png')
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)

#Labels
Label(master, text="PURSUE", font=("Calibri", 14),foreground="blue",background="white").grid(row=0,sticky=N,pady=10)
Label(master, text="Here at PURSUE, our parter's CHASE their dreams!", font=("Calibri",12),foreground="blue",background="white").grid(row=1,sticky=N)
Label(master, image=img, background="white").grid(row=2,sticky=N,pady=15)

#Buttons
Button(master, text="Register", font=("Calibri",12),width=20, bg="white", fg="blue", command=register).grid(row=3,sticky=N)
Button(master, text="ATM", font=("Calibri",12), width=20, bg="white", fg="blue").grid(row=4,sticky=N,pady=10)



master.mainloop()

