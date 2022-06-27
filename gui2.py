from tkinter import *

def sel():
    s=str(var.get())
    label.config(text=s)

root=Tk()
root.title("gui")
root.geometry("400x400")

# Label(root,text="Name",foreground='black',background='blue',width=4,height=4).pack(side=LEFT)
# Label(root,text="pass",width=4,height=4).pack(side=RIGHT)
# Label(root,text='hello',width=5,height=5).pack(side=TOP)
frame=Frame(root)
frame.pack()
frame2=Frame(root)
frame2.pack()
frame3=Frame(root)
frame3.pack()

red=Button(frame,text='red').pack(side=LEFT)
blue=Button(frame,text='blue').pack(side=LEFT)
green=Button(frame,text='green').pack(side=LEFT)


Label(frame2,text='hello').pack(side=BOTTOM)

var = IntVar
r1=Radiobutton(frame3,text="C",variable=var,value=1,command=sel).pack()

r2=Radiobutton(frame3,text='c++',variable=var,value=2,command=sel).pack()

r3=Radiobutton(frame3,text='java',variable=var,value=3,command=sel).pack()


label=Label(frame3)
label.pack(side=BOTTOM)



root.mainloop()