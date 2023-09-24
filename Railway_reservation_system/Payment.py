from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql

# functions defined here
def clear():
    emailEntry.delete(0, END)
    s_user_Entry.delete(0, END)
    s_pass_Entry.delete(0, END)
    s_cpass_Entry.delete(0, END)
    ch.set(0)


def logpage():
    Payment_win.destroy()
    import login

def connect_database():
    if emailEntry.get() == '' or s_user_Entry.get() == '' or s_pass_Entry.get() == '' or s_cpass_Entry.get() == '':
        messagebox.showerror("Error", "All Fields are Required")
    elif s_pass_Entry.get() != s_cpass_Entry.get():
        messagebox.showerror("Error", "Password mismatched")
    elif ch.get() == 0:
        messagebox.showerror("Error", "You did not accept the terms and conditions")
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='Swaroop@696')
            mycursor = con.cursor()
        except:
            messagebox.showerror("Error", "Database connectivity issue")
            return

        try:
             mycursor.execute('create database usernewdata')
             mycursor.execute('use usernewdata')
             mycursor.execute('create table data(id int auto_increment primary key not null, email varchar(50), username varchar(100), password varchar(20))')
        except:
             mycursor.execute('use usernewdata')
# to check for duplicate username write query
        query = 'select * from data where username = %s'
        mycursor.execute(query, (s_user_Entry.get()))

        row = mycursor.fetchone()
        if row != None:
            messagebox.showerror("Error", "Username already exists")
        else:
            query = 'insert into data(email,username,password) values(%s,%s,%s)'
            mycursor.execute(query, (emailEntry.get(), s_user_Entry.get(), s_pass_Entry.get()))
            con.commit()
            con.close()
            messagebox.showinfo("Success", "Registration is successful")
            clear()
            Payment_win.destroy()
            import login

# functions end here

# login_window
Payment_win = Tk()
Payment_win.title("Payment Page")
Payment_win.geometry("990x660+50+50")
Payment_win.resizable(0, 0)
Payment_win.iconbitmap('trainlogo.ico')
Payment_win.config(bg='black')

# photo
photo1 = PhotoImage(file='newTrain.png')

# label image
bgImage1 = Label(Payment_win,
                text="hi",
                image=photo1,
                bg='black',
                bd=0)
bgImage1.place(x=60, y=40)

# label

headname1 = Label(Payment_win,
                 text="PAYMENT FORM",
                 font=('Microsoft Yahei UI Light', 20, 'bold'),
                 fg='#ff3385',
                 bd=2,
                 bg='black')
headname1.place(x=540, y=35)

s_email = Label(Payment_win,
                 text="Transaction_id",
                 font=('Microsoft Yahei UI Light', 15, 'bold'),
                 fg='#ffff66',
                 bd=2,
                 bg='black')
s_email.place(x=550, y=95)

s_user = Label(Payment_win,
                 text="Amount",
                 font=('Microsoft Yahei UI Light', 15, 'bold'),
                 fg='#ffff66',
                 bd=2,
                 bg='black')
s_user.place(x=550, y=190)

s_pass = Label(Payment_win,
                 text="Bank",
                 font=('Microsoft Yahei UI Light', 15, 'bold'),
                 fg='#ffff66',
                 bd=2,
                 bg='black')
s_pass.place(x=550, y=285)

s_cpass = Label(Payment_win,
                 text="Card_no",
                 font=('Microsoft Yahei UI Light', 15, 'bold'),
                 fg='#ffff66',
                 bd=2,
                 bg='black')
s_cpass.place(x=550, y=380)

# entry
emailEntry = Entry(Payment_win,
                  width=28,
                  fg='black',
                  bg='#ff3385',
                  insertbackground='white',
                  font=('Microsoft Yahei UI Light', 14, 'bold'))
emailEntry.place(x=553, y=135)

s_user_Entry = Entry(Payment_win,
                  width=28,
                  fg='black',
                  bg='#ff3385',
                  insertbackground='white',
                  font=('Microsoft Yahei UI Light', 14, 'bold'))
s_user_Entry.place(x=553, y=225)

s_pass_Entry = Entry(Payment_win,
                  width=28,
                  fg='black',
                  bg='#ff3385',
                  insertbackground='white',
                  font=('Microsoft Yahei UI Light', 14, 'bold'))
s_pass_Entry.place(x=553, y=318)

s_cpass_Entry = Entry(Payment_win,
                  width=28,
                  fg='black',
                  bg='#ff3385',
                  insertbackground='white',
                  font=('Microsoft Yahei UI Light', 14, 'bold'))
s_cpass_Entry.place(x=553, y=412)

# checkbutton
ch = IntVar()
check1 = Checkbutton(Payment_win,
                     bg='black',
                     text="I agree to terms and conditions",
                     fg='firebrick1',
                     activeforeground='firebrick1',
                     activebackground='black',
                     font=('Microsoft Yahei UI Light', 14, 'bold'),
                     bd=6,
                     variable=ch,
                     selectcolor='black'
                     )
check1.place(x=540, y=455)

# signup button
signupBut = Button(Payment_win,
             text="Confirm",
             activebackground='#cc0066',
             activeforeground='white',
             bg='#cc0066',
             fg='white',
             cursor='hand2',
             width =20,
             font=('Open Sans', 18, 'bold'),
             command=connect_database,
             bd=0)
signupBut.place(x=560, y=510)

# last label line
sLabel = Label(Payment_win,
                 text="Already have an account?",
                 font=('Open Snas', 13, 'bold'),
                 fg='#ff3385',
                 bg='black')
sLabel.place(x=560, y=580)

# last line button
cBut = Button(Payment_win,
             text="Log In",
             activebackground='black',
             activeforeground='white',
             bg='black',
             fg='white',
             cursor='hand2',
             command=logpage,
             font=('Microsoft Yahei UI Light', 12, 'bold underline'),
             bd=0)
cBut.place(x=770, y=572)


Payment_win.mainloop()