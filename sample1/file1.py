'''
Created on 18-Jun-2019

@author: surinder singh
'''
from tkinter import *
from PIL import Image
from PIL import ImageTk
def click():
    entered_text=text1.get()
    Label(window,text="Hello "+entered_text,bg="white",fg="black").grid(row=2,column=4)
window=Tk()
window.title("login");
window.configure(background="white");
image=Image.open("robot1.gif")
image=image.resize((100,100),Image.ANTIALIAS)
photo1=ImageTk.PhotoImage(image)
Label(window,image=photo1, bg="white").grid(row=0,column=120)
Label(window, text="username",bg="white", fg="black",font="none 12 bold").grid(row=4,column=10)
Label(window,text="password",bg="white",fg="black",font="none 12 bold").grid(row=5,column=10)
text1=Entry(window,width=20,bg="white")
text1.grid(row=4,column=30)
text2=Entry(window,width=20,bg="white")
text2.grid(row=5,column=30)
Button(window,text="login",width=30,command=click).grid(row=15,column=40)
    
window.mainloop()