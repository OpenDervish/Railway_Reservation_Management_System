from tkinter import *
from tkinter import messagebox

count = 0
te = ''

def slider():
    global te
    global count
    # if it reaches the last char restart it
    if count == len(s):
        count = 0
        te = ''
    # else
    te = te + s[count]
    headName.config(text=te)
    count = count+1
    headName.after(100, slider)  # after 200 ms it will call the function again


        


def adminw_but():
    first.destroy()
    import admin_login

def user_but():
    first.destroy()
    import login


first = Tk()

# 990x660+50+50
first.title("Welcome page")
first.geometry("990x660+50+50")
first.resizable(0, 0)
first.iconbitmap('trainlogo.ico')
first.config(bg='black')

# photo
photo = PhotoImage(file='train3d.png')

# labels
bgImage = Label(first,
                image=photo,
                bg='black',
                bd=0)
bgImage.place(x=60, y=40)

s = "RAILWAY RESERVATION MANAGEMENT SYSTEM"
headName = Label(first,
                 text=s,
                 font=('Consolas', 30, 'bold'),
                 fg='#ff3385',
                 bd=2,
                 bg='black')
headName.place(x=60, y=50)
slider()
# add slider to the text

logBut = Button(first,
             text="ADMIN",
             activebackground='#cc0066',
             activeforeground='white',
             bg='#cc0066',
             fg='white',
             cursor='hand2',
             width =16,
                                                    command=adminw_but,
             font=('Cambria', 20, 'bold'),
             bd=5)
logBut.place(x=620, y=250)

logBut1 = Button(first,
             text="USER",
             activebackground='#cc0066',
             activeforeground='white',
             bg='#cc0066',
             fg='white',
             cursor='hand2',
             width =16,
             command=user_but,
             font=('Cambria', 20, 'bold'),
             bd=5)
logBut1.place(x=620, y=360)

first.mainloop()
