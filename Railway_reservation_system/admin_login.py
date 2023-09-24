from tkinter import *
from tkinter import messagebox

def on_enter(event):
    if userEntry.get() == 'AdminName':
        userEntry.delete(0, END)

def in_enter(event):
    if passEntry.get() == 'Password':
        passEntry.delete(0, END)

def hide():
    img2.config(file='ceye.png')
    passEntry.config(show='*')
    eye1.config(command=showpass)

def showpass():
    img2.config(file='oeye.png')
    passEntry.config(show='')
    eye1.config(command=hide)

def login_ad():
    if userEntry.get() == "swaroop" and passEntry.get() == "123":
        messagebox.showinfo("Status", "Login successfull")
        ad_log.destroy()
        import admin_entries
    else:
        messagebox.showerror("Status", "Invalid user entry")
        # userEntry.delete(0, END)
        # passEntry.delete(0, END)


# login_window
ad_log = Tk()
ad_log.title("Login page")
ad_log.geometry("990x660+50+50")
ad_log.resizable(0, 0)
ad_log.iconbitmap('trainlogo.ico')
ad_log.config(bg='black')

# photo
photo = PhotoImage(file='train3d.png')

# labels
bgImage = Label(ad_log,
                text="hi",
                image=photo,
                bg='black',
                bd=0)
bgImage.place(x=60, y=40)
headName = Label(ad_log,
                 text="ADMIN LOGIN",
                 font=('Microsoft Yahei UI Light', 27, 'bold'),
                 fg='#ff3385',
                 bd=2,
                 bg='black')
headName.place(x=620, y=78)

# entry for username
userEntry = Entry(ad_log,
                  width=13,
                  bd=0,
                  fg='#ffff66',
                  bg='black',
                  insertbackground='white',
                  font=('Microsoft Yahei UI Light', 21, 'bold'))
userEntry.place(x=610, y=180)
userEntry.insert(0, 'AdminName')
userEntry.bind('<FocusIn>', on_enter)

# frame  for username
userFrame = Frame(ad_log, width=264, height=2, bg='#ff3385')
userFrame.place(x=613, y=222)

#-----------------------------------------------------------------------------

# entry for password
passEntry = Entry(ad_log,
                  width=13,
                  bd=0,
                  fg='#ffff66',
                  bg='black',
                  insertbackground='white',
                  font=('Microsoft Yahei UI Light', 21, 'bold'))
passEntry.place(x=610, y=256)
passEntry.insert(0, 'Password')
passEntry.bind('<FocusIn>', in_enter)

# frame  for password
passFrame = Frame(ad_log, width=264, height=2, bg='#ff3385')
passFrame.place(x=613, y=295)

# eyebutton

img2 = PhotoImage(file='oeye.png')
eye1 = Button(ad_log,
             image=img2,
             activebackground='black',
             bg='black',
             cursor='hand2',
             command=showpass,
             bd=0)
eye1.place(x=847, y=260)



# login button
logBut = Button(ad_log,
             text="LOGIN",
             activebackground='#cc0066',
             activeforeground='white',
             bg='#cc0066',
             fg='white',
             cursor='hand2',
             width =19,
             command=login_ad,
             font=('Microsoft Yahei UI Light', 20, 'bold'),
             bd=0)
logBut.place(x=600, y=370)

ad_log.mainloop()
