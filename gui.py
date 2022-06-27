import tkinter as tk

m=tk.Tk()
m.title("Counting second")
m.geometry("600x600")


frame1=tk.Frame(m,bg='black',width=30,height=30)
frame1.pack()

frame2=tk.Frame(frame1,bg='blue',width=15,height=15)
frame2.pack(padx=15,pady=15)


label=tk.Label(text="hello world",foreground='black',background='blue' ,width=30,height=30)
label.pack()
button=tk.Button(m,text="stop",width=25,command=m.destroy)

button.pack()
m.mainloop()