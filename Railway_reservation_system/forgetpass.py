from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql

# functions defined here
def logpage1():
    fgp_page.destroy()
    import login

def database_connect():
    if f_userEntry.get()=='' or f_passEntry.get()=='' or f_con_passEntry.get()=='':
        messagebox.showerror("Error", "All Fields are required")
    elif f_passEntry.get() != f_con_passEntry.get():
        messagebox.showerror("Error", "Password mismatched ")
    else:
        try:
            con = pymysql.connect(host='localhost',
                                  user='root',
                                  password='Swaroop@696',
                                  database='usernewdata')
            mycursor = con.cursor()
        except:
            messagebox.showerror("Error", "Database connectivity issue")
            return
        query = 'select * from data where username=%s'
        mycursor.execute(query, (f_userEntry.get()))
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror("Error", "Incorrect Username")
        else:
            query = 'update data set password=%s where username=%s'
            mycursor.execute(query, (f_passEntry.get(), f_userEntry.get()))
            con.commit()
            messagebox.showinfo('Successful', 'Password is reset! Login with your new Password')
            fgp_page.destroy()
            import login

# function definition ends here


# login_window
fgp_page = Tk()
fgp_page.title("RESET PASSWORD")
fgp_page.geometry("990x660+50+50")
fgp_page.resizable(0, 0)
fgp_page.iconbitmap('trainlogo.ico')
fgp_page.config(bg='black')

# photo
photo1 = PhotoImage(file='newTrain.png')

# label image
bgImage2 = Label(fgp_page,
                text="hi",
                image=photo1,
                bg='Black',
                bd=0)
bgImage2.place(x=60, y=40)

headname1 = Label(fgp_page,
                 text="RESET PASSWORD",
                 font=('Microsoft Yahei UI Light', 27, 'bold'),
                 fg='#ff3385',
                 bd=2,
                 bg='black')
headname1.place(x=560, y=35)

uname1 = Label(fgp_page,
                 text="Username",
                 font=('Microsoft Yahei UI Light', 20, 'bold'),
                 fg='#ff3385',
                 bd=2,
                 bg='black')
uname1.place(x=560, y=140)

f_userEntry = Entry(fgp_page,
                  width=16,
                  bd=0,
                  fg='#ffff66',
                  bg='black',
                  insertbackground='white',
                  font=('Open sans', 19, 'bold'))
f_userEntry.place(x=566, y=180)
#  ---------------------------------------------------------------------
pass1 = Label(fgp_page,
                 text="New Password",
                 font=('Microsoft Yahei UI Light', 20, 'bold'),
                 fg='#ff3385',
                 bd=2,
                 bg='black')
pass1.place(x=560, y=280)

f_passEntry = Entry(fgp_page,
                  width=16,
                  bd=0,
                  fg='#ffff66',
                  bg='black',
                  insertbackground='white',
                  font=('Open sans', 19, 'bold'))
f_passEntry.place(x=566, y=320)
#--------------------------------------------------------------------

con_pass1 = Label(fgp_page,
                 text="Confirm Password",
                 font=('Microsoft Yahei UI Light', 20, 'bold'),
                 fg='#ff3385',
                 bd=2,
                 bg='black')
con_pass1.place(x=560, y=420)

f_con_passEntry = Entry(fgp_page,
                  width=16,
                  bd=0,
                  fg='#ffff66',
                  bg='black',
                  insertbackground='white',
                  font=('Open sans', 19, 'bold'))
f_con_passEntry.place(x=566, y=460)



# frame  for username
f_userFrame = Frame(fgp_page, width=264, height=2, bg='#ff3385')
f_userFrame.place(x=566, y=222)

f_passFrame = Frame(fgp_page, width=264, height=2, bg='#ff3385')
f_passFrame.place(x=566, y=360)

f_conpassFrame = Frame(fgp_page, width=264, height=2, bg='#ff3385')
f_conpassFrame.place(x=566, y=500)

# submit button

subBut = Button(fgp_page,
             text="SUBMIT",
             activebackground='#cc0066',
             activeforeground='white',
             bg='#cc0066',
             fg='white',
             cursor='hand2',
             width =20,
             command=database_connect,
             font=('Open Sans', 18, 'bold'),
             bd=0)
subBut.place(x=560, y=530)

# last label line
s1Label = Label(fgp_page,
                 text="Return to login page?",
                 font=('Open Snas', 13, 'bold'),
                 fg='red',
                 bg='black')
s1Label.place(x=560, y=593)

# last line button
c1But = Button(fgp_page,
             text="Log In",
             activebackground='black',
             activeforeground='white',
             bg='black',
             fg='white',
             cursor='hand2',
             command=logpage1,
             font=('Microsoft Yahei UI Light', 12, 'bold underline'),
             bd=0)
c1But.place(x=750, y=585)

fgp_page.mainloop()