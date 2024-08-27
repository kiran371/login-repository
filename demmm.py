from cProfile import label
from tkinter import *
from xml.sax.handler import feature_external_ges
from  tkinter import messagebox

root=Tk()
fnt=["arial",18,"bold"]
fnt1=["arial",10,"bold"]

def show():
    messagebox.showinfo("Login Successfully")

frame=Frame(root,height=400,width=400,bg="black")
frame.pack()

lbl1=Label(frame,text="Login",bg="black",fg="green",font=fnt)
lbl1.place(x=150,y=10)



lbl2=Label(frame,text="Username",bg="black",fg="white",font=fnt1)
lbl2.place(x=100,y=60)

lble=Entry(frame,fg="red")
lble.place(x=180,y=60)


lble1=Entry(frame,fg="red",show="*")
lble1.place(x=180,y=100)


lbl3=Label(frame,text="Password",bg="black",fg="white",font=fnt1)
lbl3.place(x=100,y=100)

butt=Button(frame,text="Login",bg="green",fg="white",command=show)
butt.place(x=170,y=150)
root.mainloop()

