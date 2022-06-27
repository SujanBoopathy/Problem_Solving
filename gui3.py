from tkinter import *

def sel():
    s=e1.get()
    d=var1.get()
    e=var2.get()
    b=var3.get()
    label.config(text=b)


root=Tk()
root.geometry("400x400")
var1=IntVar()
var2=IntVar()

c1=Checkbutton(root,text='chocolate',variable=var1,onvalue=1,offvalue=0)
c1.pack()

c2=Checkbutton(root,text='milk',variable=var2,onvalue=2,offvalue=0)
c2.pack()

var3=StringVar()
var2.set('C')
r1=Radiobutton(root,text='C',variable=var3,value='C')
r1.pack()
r2=Radiobutton(root,text='C++',variable=var3,value='C++')
r2.pack()
r3=Radiobutton(root,text='java',variable=var3,value='java')
r3.pack()

e1=Entry(root,bd=1)
e1.pack()

label=Label(root,width=4,height=4)
label.pack()

btn=Button(root,text='submit',command=sel)
btn.pack()

root.mainloop()