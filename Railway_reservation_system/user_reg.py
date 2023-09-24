from tkinter import *
from tkinter import messagebox
import pymysql


# functions defined here
def clear():
    userEntry.delete(0, END)
    NameEntry.delete(0, END)
    DOBEntry.delete(0, END)
    AgeEntry.delete(0, END)
    GenderEntry.delete(0, END)
    CityEntry.delete(0, END)
    PincodeEntry.delete(0, END)
    StateEntry.delete(0, END)


def submit_us():
    pass

def hu():
    reg_win.destroy()
    import user_entries

# functions defined here
def on_enter(event):
    if userEntry.get() == 'Username':
        userEntry.delete(0, END)

def on_e(event):
    if NameEntry.get() == 'Name':
        NameEntry.delete(0, END)

def on_en(event):
    if DOBEntry.get() == 'DOB':
        DOBEntry.delete(0, END)

def on_ent(event):
    if AgeEntry.get() == 'Age':
        AgeEntry.delete(0, END)

def on_entr(event):
    if GenderEntry.get() == 'Gender':
        GenderEntry.delete(0, END)

def on_h(event):
    if CityEntry.get() == 'City':
        CityEntry.delete(0, END)

def on_he(event):
    if PincodeEntry.get() == 'Pincode':
        PincodeEntry.delete(0, END)

def on_hey(event):
    if StateEntry.get() == 'State':
        StateEntry.delete(0, END)
#///////////////////////////////////////////////////////////////////
# def login_user():
#     if userEntry.get()=='' :
#         messagebox.showerror("Error", "ALl Fields are Required")
#     else:
#         try:
#             con = pymysql.connect(host='localhost',user='root',password='Swaroop@696')
#             mycursor = con.cursor()
#         except:
#             messagebox.showerror("Error","Connection is not established")
#             return
#         mycursor.execute('use usernewdata')
#         query = 'select * from data where username=%s and password=%s'
#         mycursor.execute(query,(userEntry.get(),passEntry.get()))
#         row = mycursor.fetchone()
#         if row == None:
#             messagebox.showerror("Error", "Invalid Username or Password")
#         else:
#             messagebox.showinfo("Welcome", "Login is successful")



#444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444

def connect_database():
    if userEntry.get() == '' or NameEntry.get() == '' or DOBEntry.get() == '' or AgeEntry.get() == '' or GenderEntry.get() == '' or CityEntry.get() == '' or PincodeEntry.get() == '' or StateEntry.get() == '':
        messagebox.showerror("Error", "All Fields are Required")
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='Swaroop@696')
            mycursor = con.cursor()
        except:
            messagebox.showerror("Error", "Database connectivity issue")
            return

        try:
             mycursor.execute('create database AD_TRAIN')
             mycursor.execute('use AD_TRAIN')
             mycursor.execute('create table User(Name varchar(20),Username varchar(20) primary key,Dob date,Age int,Gender varchar(1),City varchar(20) not null,Pincode int not null,State varchar(20) not null ;')
        except:
             mycursor.execute('use ad_train')
# to check for duplicate username write query
        query = 'select * from User where username = %s'
        mycursor.execute(query, (userEntry.get()))

        row = mycursor.fetchone()
        if row != None:
            messagebox.showerror("Error", "Username already. exists")
        else:
            query = 'insert into User(Username,Name,DOB,Age,Gender,City,Pincode,State) values(%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query, (userEntry.get(), NameEntry.get(), DOBEntry.get(),AgeEntry.get(),GenderEntry.get(),CityEntry.get(),PincodeEntry.get(),StateEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo("Success", "Registration is successful")
            clear()
            reg_win .destroy()
            import user_entries



def forget():
    reg_win.destroy()
    import forgetpass



# end of functions

# reg_window
reg_win = Tk()
reg_win.title("User Registration page")
reg_win.geometry("990x750+50+50")
reg_win.resizable(0, 0)
reg_win.iconbitmap('trainlogo.ico')
reg_win.config(bg='black')

# photo
photo = PhotoImage(file='train3d.png')

# labels
bgImage = Label(reg_win,
                text="hi",
                image=photo,
                bg='black',
                bd=0)
bgImage.place(x=60, y=0)
headName = Label(reg_win,
                 text="User Registration",
                 font=('Microsoft Yahei UI Light', 27, 'bold'),
                 fg='#ff3385',
                 bd=2,
                 bg='black')
headName.place(x=620, y=20)

# entry for username
userEntry = Entry(reg_win,
                  width=13,
                  bd=0,
                  fg='#ffff66',
                  bg='black',
                  insertbackground='white',
                  font=('Microsoft Yahei UI Light', 21, 'bold'))
userEntry.place(x=610, y=100)
userEntry.insert(0, 'Username')
userEntry.bind('<FocusIn>', on_enter)

#////////////////////////////////////////////////////////////////////////////////

# entry for Name
NameEntry = Entry(reg_win,
                  width=13,
                  bd=0,
                  fg='#ffff66',
                  bg='black',
                  insertbackground='white',
                  font=('Microsoft Yahei UI Light', 21, 'bold'))
NameEntry.place(x=610, y=160)
NameEntry.insert(0, 'Name')
NameEntry.bind('<FocusIn>', on_e)


# entry for DOB
DOBEntry = Entry(reg_win,
                  width=13,
                  bd=0,
                  fg='#ffff66',
                  bg='black',
                  insertbackground='white',
                  font=('Microsoft Yahei UI Light', 21, 'bold'))
DOBEntry.place(x=610, y=225)
DOBEntry.insert(0, 'DOB')
DOBEntry.bind('<FocusIn>', on_en)

# entry for Age
AgeEntry = Entry(reg_win,
                  width=13,
                  bd=0,
                  fg='#ffff66',
                  bg='black',
                  insertbackground='white',
                  font=('Microsoft Yahei UI Light', 21, 'bold'))
AgeEntry.place(x=610, y=290)
AgeEntry.insert(0, 'Age')
AgeEntry.bind('<FocusIn>', on_ent)

# entry for Gender
GenderEntry = Entry(reg_win,
                  width=13,
                  bd=0,
                  fg='#ffff66',
                  bg='black',
                  insertbackground='white',
                  font=('Microsoft Yahei UI Light', 21, 'bold'))
GenderEntry.place(x=610, y=345)
GenderEntry.insert(0, 'Gender')
GenderEntry.bind('<FocusIn>', on_entr)

# entry for City
CityEntry = Entry(reg_win,
                  width=13,
                  bd=0,
                  fg='#ffff66',
                  bg='black',
                  insertbackground='white',
                  font=('Microsoft Yahei UI Light', 21, 'bold'))
CityEntry.place(x=610, y=400)
CityEntry.insert(0, 'City')
CityEntry.bind('<FocusIn>', on_h)

# entry for Pincode
PincodeEntry = Entry(reg_win,
                  width=13,
                  bd=0,
                  fg='#ffff66',
                  bg='black',
                  insertbackground='white',
                  font=('Microsoft Yahei UI Light', 21, 'bold'))
PincodeEntry.place(x=610, y=465)
PincodeEntry.insert(0, 'Pincode')
PincodeEntry.bind('<FocusIn>', on_he)

# entry for State
StateEntry = Entry(reg_win,
                  width=13,
                  bd=0,
                  fg='#ffff66',
                  bg='black',
                  insertbackground='white',
                  font=('Microsoft Yahei UI Light', 21, 'bold'))
StateEntry.place(x=610, y=530)
StateEntry.insert(0, 'State')
StateEntry.bind('<FocusIn>', on_hey)



#////////////////////////////////////////////////////////////////////////////////
# frame  for username
userFrame = Frame(reg_win, width=264, height=2, bg='#ff3385')
userFrame.place(x=613, y=145)

nameFrame = Frame(reg_win, width=264, height=2, bg='#ff3385')
nameFrame.place(x=613, y=200)

dobFrame = Frame(reg_win, width=264, height=2, bg='#ff3385')
dobFrame.place(x=613, y=260)

AgeFrame = Frame(reg_win, width=264, height=2, bg='#ff3385')
AgeFrame.place(x=613, y=330)

GenderFrame = Frame(reg_win, width=264, height=2, bg='#ff3385')
GenderFrame.place(x=613, y=390)

CityFrame = Frame(reg_win, width=264, height=2, bg='#ff3385')
CityFrame.place(x=613, y=445)

PincodeFrame = Frame(reg_win, width=264, height=2, bg='#ff3385')
PincodeFrame.place(x=613, y=500)

StateFrame = Frame(reg_win, width=264, height=2, bg='#ff3385')
StateFrame.place(x=613, y=565)

# login button
Sub_but = Button(reg_win,
             text="Submit",
             activebackground='#cc0066',
             activeforeground='white',
             bg='#cc0066',
             fg='white',
             cursor='hand2',
             width =19,
             command=connect_database,
             font=('Microsoft Yahei UI Light', 15, 'bold'),
             bd=0)
Sub_but.place(x=620, y=580)

reg_but = Button(reg_win,
             text="Already reg",
             activebackground='#cc0066',
             activeforeground='white',
             bg='#cc0066',
             fg='white',
             cursor='hand2',
             width =19,
             command=hu,
             font=('Microsoft Yahei UI Light', 15, 'bold'),
             bd=0)
reg_but.place(x=620, y=640)


#  last line button
# createBut = Button(reg_win,
#              text="Create new account!",
#              activebackground='black',
#              activeforeground='white',
#              bg='black',
#              fg='white',
#              command=signupPage,
#              cursor='hand2',
#              font=('Microsoft Yahei UI Light', 12, 'bold underline'),
#              bd=0)
# createBut.place(x=770, y=560)

reg_win.mainloop()