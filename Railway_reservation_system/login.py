from tkinter import *
from tkinter import messagebox
import pymysql
# functions defined here
def on_enter(event):
    if userEntry.get() == 'Username':
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

def signupPage():
    login_win.destroy()
    import signup

def login_user():
    if userEntry.get()=='' or passEntry.get()=='':
        messagebox.showerror("Error", "ALl Fields are Required")
    else:
        try:
            con = pymysql.connect(host='localhost',user='root',password='Swaroop@696')
            mycursor = con.cursor()
        except:
            messagebox.showerror("Error","Connection is not establoblished")
            return
        mycursor.execute('use usernewdata')
        query = 'select * from data where username=%s and password=%s'
        mycursor.execute(query,(userEntry.get(),passEntry.get()))
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror("Error", "Invalid Username or Password")
        else:
            messagebox.showinfo("Welcome", "Login is successful")
            login_win.destroy()
            import user_reg

def forget():
    login_win.destroy()
    import forgetpass



# end of functions

# login_window
login_win = Tk()
login_win.title("Login page")
login_win.geometry("990x660+50+50")
login_win.resizable(0, 0)
login_win.iconbitmap('trainlogo.ico')
login_win.config(bg='black')

# photo
photo = PhotoImage(file='train3d.png')

# labels
bgImage = Label(login_win,
                text="hi",
                image=photo,
                bg='black',
                bd=0)
bgImage.place(x=60, y=40)
headName = Label(login_win,
                 text="USER LOGIN",
                 font=('Microsoft Yahei UI Light', 27, 'bold'),
                 fg='#ff3385',
                 bd=2,
                 bg='black')
headName.place(x=620, y=88)

# entry for username
userEntry = Entry(login_win,
                  width=13,
                  bd=0,
                  fg='#ffff66',
                  bg='black',
                  insertbackground='white',
                  font=('Microsoft Yahei UI Light', 21, 'bold'))
userEntry.place(x=610, y=180)
userEntry.insert(0, 'Username')
userEntry.bind('<FocusIn>', on_enter)

# frame  for username
userFrame = Frame(login_win, width=264, height=2, bg='#ff3385')
userFrame.place(x=613, y=222)

#-----------------------------------------------------------------------------

# entry for password
passEntry = Entry(login_win,
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
passFrame = Frame(login_win, width=264, height=2, bg='#ff3385')
passFrame.place(x=613, y=295)

# eyebutton

img2 = PhotoImage(file='oeye.png')
eye1 = Button(login_win,
             image=img2,
             activebackground='black',
             bg='black',
             cursor='hand2',
             command=showpass,
             bd=0)
eye1.place(x=847, y=260)

# forget password
fgp = Button(login_win,
             text="Forgot Password?",
             activebackground='black',
             activeforeground='white',
             bg='black',
             fg='white',
             command=forget,
             cursor='hand2',
             font=('Microsoft Yahei UI Light', 12, 'bold'),
             bd=0)
fgp.place(x=732, y=305)

# login button
logBut = Button(login_win,
             text="LOGIN",
             activebackground='#cc0066',
             activeforeground='white',
             bg='#cc0066',
             fg='white',
             cursor='hand2',
             width =19,
             command=login_user,
             font=('Microsoft Yahei UI Light', 20, 'bold'),
             bd=0)
logBut.place(x=600, y=370)

# or label
orLabel = Label(login_win,
                 text="--------------- OR ---------------",
                 font=('Open Snas', 20),
                 fg='#ff3385',
                 bg='black')
orLabel.place(x=590, y=450)

# remaining images
facebookImage = PhotoImage(file ='facebook.png')
facebook = Label(login_win,image=facebookImage,bg='black')
facebook.place(x=680,y=500)

googleImage = PhotoImage(file ='google.png')
google = Label(login_win,image=googleImage, bg='black')
google.place(x=740, y=500)

twitterImage = PhotoImage(file ='twitter.png')
twitter = Label(login_win,image=twitterImage,bg='black')
twitter.place(x=800,y=500)

# last label line
signLabel = Label(login_win,
                 text="Don't have an account?",
                 font=('Open Snas', 13, 'bold'),
                 fg='#ff3385',
                 bg='black')
signLabel.place(x=580, y=565)

# last line button
createBut = Button(login_win,
             text="Create new account!",
             activebackground='black',
             activeforeground='white',
             bg='black',
             fg='white',
             command=signupPage,
             cursor='hand2',
             font=('Microsoft Yahei UI Light', 12, 'bold underline'),
             bd=0)
createBut.place(x=770, y=560)

login_win.mainloop()