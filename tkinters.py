from tkinter import *

app = Tk()
app.geometry("400x400")
app.configure(background="yellow")
l1 = Label(app, text="Enter First NUmber : ",background="yellow").pack()
b2 = Entry(app, width=50)
b2.pack()
l2 = Label(app, text="Enter Second NUmber : ",background="yellow").pack()
b3 = Entry(app, width=50)
b3.pack()
l3 = Label(app, text="Enter One operation : ",background="yellow").pack()
b4 = Entry(app)
b4.pack()
def calculate():
    val1 = int(b2.get())
    val2 = int(b3.get())
    val3 = b4.get()
    if val3 == "+":
        res =  val1+val2
        label = Label(app, text="Addition : "+str(res)).pack()
    elif val3 == "-":
        res =  val1 - val2
        label = Label(app, text="Substraction : "+str(res)).pack()
    elif val3 == "/":
        res =  val1/val2
        label = Label(app, text="Division : "+str(res)).pack()
    elif val3 == "*":
        res = val1*val2
        label = Label(app, text="Multiplication : "+str(res)).pack()
    else:
        label = Label(app, text="Wrong Input").pack()
        
button = Button(app, text="submit", command=calculate).pack()


app.mainloop()