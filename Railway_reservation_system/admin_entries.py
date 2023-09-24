
from tkinter import *
from tkinter import messagebox,filedialog
import time
import ttkthemes  # here this module is being used for the button
from tkinter import ttk
import pandas
import pymysql

# exit func
def iexit():
    res = messagebox.askyesno('Confirm', 'Do u want to exit?')
    if res:
        ad_ent.destroy()
    else:
        pass



# export func
def export_train():
    url = filedialog.asksaveasfilename(defaultextension='.csv')
    index = trainTable.get_children()
    newlist = []
    for i in index:
        cont = trainTable.item(i)
        datalist = cont['values']
        newlist.append(datalist)

    table = pandas.DataFrame(newlist, columns=('Train_no', 'Train_Name', 'Source', 'Destination', 'Arr_time', 'Dep_time', 'Date', 'Seat_available'))
    table.to_csv(url, index=False)
    messagebox.showinfo('Success', 'Data is saved successfully')

# update train func
def update_train():

    def update_data():
        query='update RAIL set Train_Name=%s,Source=%s,Destination = %s,Arr_time = %s,Dep_time=%s,Date=%s,Seat_available=%s where Train_no=%s'
        mycursor.execute(query, (Tn_Entry.get(), src_Entry.get(), dest_Entry.get(), at_Entry.get(), dt_Entry.get(), dist_Entry.get(), sa_Entry.get(), No_Entry.get()))
        con.commit()
        messagebox.showinfo('Success', f'Train no {No_Entry.get()} is modified successfully',parent=update_win)
        update_win.destroy()
        show_train()




    update_win = Toplevel()
    update_win.title("Update Train")
    update_win.resizable(False, False)
    update_win.grab_set()

    # -------------------------------------------------------------------------------
    No_label = Label(update_win, text='Train_no', font=('times new roman', 20, 'bold'))
    No_label.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    No_Entry = Entry(update_win, font=('Consolas', 15, 'bold'), width=24)
    No_Entry.grid(row=0, column=1, pady=15, padx=10)

    # -------------------------------------------------------------------------------
    Tn_label = Label(update_win, text='Train_name', font=('times new roman', 20, 'bold'))
    Tn_label.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    Tn_Entry = Entry(update_win, font=('Consolas', 15, 'bold'), width=24)
    Tn_Entry.grid(row=1, column=1, pady=15, padx=10)

    # -------------------------------------------------------------------------------
    src_label = Label(update_win, text='Source', font=('times new roman', 20, 'bold'))
    src_label.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    src_Entry = Entry(update_win, font=('Consolas', 15, 'bold'), width=24)
    src_Entry.grid(row=2, column=1, pady=15, padx=10)
    # -------------------------------------------------------------------------------
    dest_label = Label(update_win, text='Destination', font=('times new roman', 20, 'bold'))
    dest_label.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    dest_Entry = Entry(update_win, font=('Consolas', 15, 'bold'), width=24)
    dest_Entry.grid(row=3, column=1, pady=15, padx=10)
    # -------------------------------------------------------------------------------
    at_label = Label(update_win, text='Arrival_time', font=('times new roman', 20, 'bold'))
    at_label.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    at_Entry = Entry(update_win, font=('Consolas', 15, 'bold'), width=24)
    at_Entry.grid(row=4, column=1, pady=15, padx=10)
    # -------------------------------------------------------------------------------
    dt_label = Label(update_win, text='Departure_time', font=('times new roman', 20, 'bold'))
    dt_label.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    dt_Entry = Entry(update_win, font=('Consolas', 15, 'bold'), width=24)
    dt_Entry.grid(row=5, column=1, pady=15, padx=10)
    # -------------------------------------------------------------------------------
    dist_label = Label(update_win, text='Date', font=('times new roman', 20, 'bold'))
    dist_label.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    dist_Entry = Entry(update_win, font=('Consolas', 15, 'bold'), width=24)
    dist_Entry.grid(row=6, column=1, pady=15, padx=10)
    # -------------------------------------------------------------------------------
    sa_label = Label(update_win, text='Seats_available', font=('times new roman', 20, 'bold'))
    sa_label.grid(row=7, column=0, padx=30, pady=15, sticky=W)
    sa_Entry = Entry(update_win, font=('Consolas', 15, 'bold'), width=24)
    sa_Entry.grid(row=7, column=1, pady=15, padx=10)

    update_but = ttk.Button(update_win, text="Update Train",command=update_data)
    update_but.grid(row=8, columnspan=2, pady=15)

    global listdata
    indexing = trainTable.focus()
    contents = trainTable.item(indexing)
    listdata = contents['values']
    No_Entry.insert(0, listdata[0])
    Tn_Entry.insert(0, listdata[1])
    src_Entry.insert(0, listdata[2])
    dest_Entry.insert(0, listdata[3])
    at_Entry.insert(0, listdata[4])
    dt_Entry.insert(0, listdata[5])
    dist_Entry.insert(0, listdata[6])
    sa_Entry.insert(0, listdata[7])



# show_train func
def show_train():
    query = 'select * from RAIL'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    trainTable.delete(*trainTable.get_children())
    for data in fetched_data:
        trainTable.insert('', END, values=data)


#delete func
def delete_train():
    index = trainTable.focus()
    print(index)
    train_cont = trainTable.item(index)
    train_cont_id = train_cont['values'][0]
    query = 'delete from RAIL where Train_no=%s'
    mycursor.execute(query, train_cont_id)
    con.commit()
    messagebox.showinfo('Deleted', f'Train_no {train_cont_id} is deleted succesfully')
    query = 'select * from RAIL'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    trainTable.delete(*trainTable.get_children())
    for data in fetched_data:
        trainTable.insert('', END, values=data)


# search func
def search_train():
        def search_data():
            # to fetch data from database
            query = 'select * from RAIL where Train_no=%s or Train_Name=%s or Source=%s or Destination = %s or Arr_time = %s or Dep_time=%s or Date=%s or Seat_available=%s'
            mycursor.execute(query, (No_Entry.get(), Tn_Entry.get(), src_Entry.get(), dest_Entry.get(), at_Entry.get(), dt_Entry.get(), dist_Entry.get(), sa_Entry.get()))
            trainTable.delete(*trainTable.get_children())
            fetchdata = mycursor.fetchall()
            for data in fetchdata:
                trainTable.insert('', END, values=data)

        search_win = Toplevel()
        search_win.title("Search Train")
        search_win.resizable(False, False)
        search_win.grab_set()

        # -------------------------------------------------------------------------------
        No_label = Label(search_win, text='Train_no', font=('times new roman', 20, 'bold'))
        No_label.grid(row=0, column=0, padx=30, pady=15, sticky=W)
        No_Entry = Entry(search_win, font=('Consolas', 15, 'bold'), width=24)
        No_Entry.grid(row=0, column=1, pady=15, padx=10)

        # -------------------------------------------------------------------------------
        Tn_label = Label(search_win, text='Train_name', font=('times new roman', 20, 'bold'))
        Tn_label.grid(row=1, column=0, padx=30, pady=15, sticky=W)
        Tn_Entry = Entry(search_win, font=('Consolas', 15, 'bold'), width=24)
        Tn_Entry.grid(row=1, column=1, pady=15, padx=10)

        # -------------------------------------------------------------------------------
        src_label = Label(search_win, text='Source', font=('times new roman', 20, 'bold'))
        src_label.grid(row=2, column=0, padx=30, pady=15, sticky=W)
        src_Entry = Entry(search_win, font=('Consolas', 15, 'bold'), width=24)
        src_Entry.grid(row=2, column=1, pady=15, padx=10)
        # -------------------------------------------------------------------------------
        dest_label = Label(search_win, text='Destination', font=('times new roman', 20, 'bold'))
        dest_label.grid(row=3, column=0, padx=30, pady=15, sticky=W)
        dest_Entry = Entry(search_win, font=('Consolas', 15, 'bold'), width=24)
        dest_Entry.grid(row=3, column=1, pady=15, padx=10)
        # -------------------------------------------------------------------------------
        at_label = Label(search_win, text='Arrival_time', font=('times new roman', 20, 'bold'))
        at_label.grid(row=4, column=0, padx=30, pady=15, sticky=W)
        at_Entry = Entry(search_win, font=('Consolas', 15, 'bold'), width=24)
        at_Entry.grid(row=4, column=1, pady=15, padx=10)
        # -------------------------------------------------------------------------------
        dt_label = Label(search_win, text='Departure_time', font=('times new roman', 20, 'bold'))
        dt_label.grid(row=5, column=0, padx=30, pady=15, sticky=W)
        dt_Entry = Entry(search_win, font=('Consolas', 15, 'bold'), width=24)
        dt_Entry.grid(row=5, column=1, pady=15, padx=10)
        # -------------------------------------------------------------------------------
        dist_label = Label(search_win, text='Date', font=('times new roman', 20, 'bold'))
        dist_label.grid(row=6, column=0, padx=30, pady=15, sticky=W)
        dist_Entry = Entry(search_win, font=('Consolas', 15, 'bold'), width=24)
        dist_Entry.grid(row=6, column=1, pady=15, padx=10)
        # -------------------------------------------------------------------------------
        sa_label = Label(search_win, text='Seats_available', font=('times new roman', 20, 'bold'))
        sa_label.grid(row=7, column=0, padx=30, pady=15, sticky=W)
        sa_Entry = Entry(search_win, font=('Consolas', 15, 'bold'), width=24)
        sa_Entry.grid(row=7, column=1, pady=15, padx=10)

        searchButt = ttk.Button(search_win, text="Search Train", command=search_data)
        searchButt.grid(row=8, columnspan=2, pady=15)


# button function closed


# add functions
def add_train():
    def add_data():
        if No_Entry.get()=='' or Tn_Entry.get()=='' or src_Entry.get()=='' or\
            dest_Entry.get() == '' or at_Entry.get()=='' or dt_Entry.get()=='' or \
                dist_Entry.get() == '' or sa_Entry.get()=='':
            messagebox.showerror("Error", "All Fields are required", parent=add_win)
        else:
            try:
                query='insert into RAIL values(%s,%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(query, (No_Entry.get(), Tn_Entry.get(),
                                        src_Entry.get(), dest_Entry.get(),
                                        at_Entry.get(), dt_Entry.get(),
                                        dist_Entry.get(), sa_Entry.get()
                                        ))
                con.commit()
                result = messagebox.askyesno("Confirm", "Data added succesfully, Do you want to clean the form?", parent=add_win)
                if result:
                    No_Entry.delete(0, END)
                    Tn_Entry.delete(0, END)
                    src_Entry.delete(0, END)
                    dest_Entry.delete(0, END)
                    at_Entry.delete(0, END)
                    dt_Entry.delete(0, END)
                    dist_Entry.delete(0, END)
                    sa_Entry.delete(0, END)
                else:
                    pass
            except:
                messagebox.showerror("Error", "Train_no cannot be repeated", parent=add_win)
                return

        # to fetch data from database
        mycursor.execute('select * from RAIL')
        fetchdata = mycursor.fetchall()
        trainTable.delete(*trainTable.get_children())
        for data in fetchdata:
            datalist = list(data)
            trainTable.insert('', END, values=datalist)

# ---------------------------------------------------------------------------
    add_win = Toplevel()
    add_win.title("Add Train")
    add_win.resizable(False, False)
    add_win.grab_set()

    # -------------------------------------------------------------------------------
    No_label = Label(add_win, text='Train_no', font=('times new roman', 20, 'bold'))
    No_label.grid(row=0, column=0, padx=30, pady=15,sticky=W)
    No_Entry = Entry(add_win, font=('Consolas', 15, 'bold'), width=24)
    No_Entry.grid(row=0, column=1, pady=15, padx=10)

    # -------------------------------------------------------------------------------
    Tn_label = Label(add_win, text='Train_name', font=('times new roman', 20, 'bold'))
    Tn_label.grid(row=1, column=0, padx=30, pady=15,sticky=W)
    Tn_Entry = Entry(add_win, font=('Consolas', 15, 'bold'), width=24)
    Tn_Entry.grid(row=1, column=1, pady=15, padx=10)

    # -------------------------------------------------------------------------------
    src_label = Label(add_win, text='Source', font=('times new roman', 20, 'bold'))
    src_label.grid(row=2, column=0, padx=30, pady=15,sticky=W)
    src_Entry = Entry(add_win, font=('Consolas', 15, 'bold'), width=24)
    src_Entry.grid(row=2, column=1, pady=15, padx=10)
    # -------------------------------------------------------------------------------
    dest_label = Label(add_win, text='Destination', font=('times new roman', 20, 'bold'))
    dest_label.grid(row=3, column=0, padx=30, pady=15,sticky=W)
    dest_Entry = Entry(add_win, font=('Consolas', 15, 'bold'), width=24)
    dest_Entry.grid(row=3, column=1, pady=15, padx=10)
    # -------------------------------------------------------------------------------
    at_label = Label(add_win, text='Arrival_time', font=('times new roman', 20, 'bold'))
    at_label.grid(row=4, column=0, padx=30, pady=15,sticky=W)
    at_Entry = Entry(add_win, font=('Consolas', 15, 'bold'), width=24)
    at_Entry.grid(row=4, column=1, pady=15, padx=10)
    # -------------------------------------------------------------------------------
    dt_label = Label(add_win, text='Departure_time', font=('times new roman', 20, 'bold'))
    dt_label.grid(row=5, column=0, padx=30, pady=15,sticky=W)
    dt_Entry = Entry(add_win, font=('Consolas', 15, 'bold'), width=24)
    dt_Entry.grid(row=5, column=1, pady=15, padx=10)
    # -------------------------------------------------------------------------------
    dist_label = Label(add_win, text='Date', font=('times new roman', 20, 'bold'))
    dist_label.grid(row=6, column=0, padx=30, pady=15,sticky=W)
    dist_Entry = Entry(add_win, font=('Consolas', 15, 'bold'), width=24)
    dist_Entry.grid(row=6, column=1, pady=15, padx=10)
    # -------------------------------------------------------------------------------
    sa_label = Label(add_win, text='Seats_available', font=('times new roman', 20, 'bold'))
    sa_label.grid(row=7, column=0, padx=30, pady=15,sticky=W)
    sa_Entry = Entry(add_win, font=('Consolas', 15, 'bold'), width=24)
    sa_Entry.grid(row=7, column=1, pady=15, padx=10)

    add1Butt = ttk.Button(add_win, text="Add Train",command=add_data)
    add1Butt.grid(row=8, columnspan=2, pady=15)

# button function closed

# fns
def clock():
    date = time.strftime('%d/%m/%Y')
    curr_time = time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'   Date: {date}\nTime: {curr_time}')
    datetimeLabel.after(1000, clock)  # after 1second clock is called again

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
    headName.after(200, slider)  # after 200 ms it will call the function again

def Con_data():
    def Connect():
        global mycursor,con
        try:
            con= pymysql.connect(host='localhost', user='root', password='Swaroop@696')
            mycursor = con.cursor()

        except:
            messagebox.showerror("Error", "Invalid Details", parent=conWin)
            return

# 'Train_no', 'Train_Name', 'Source', 'Destination', 'Arr_time', 'Dep_time', 'Date', 'Seat_available'
        try:
            mycursor.execute('create database AD_TRAIN')
            mycursor.execute('use AD_TRAIN')
            mycursor.execute('create table RAIL(Train_no int not null primary key,Train_Name varchar(30),Source varchar(30),Destination varchar(30),Arr_time varchar(15),Dep_time varchar(15),Date date,Seat_available int)')
        except:
            mycursor.execute('use AD_TRAIN')

        messagebox.showinfo("Success", "Database Connection is successful", parent=conWin)
        conWin.destroy()
        addTrain_but.config(state=NORMAL)
        searchTrain_but.config(state=NORMAL)
        deleteTrain_but.config(state=NORMAL)
        showTrain_but.config(state=NORMAL)
        updateTrain_but.config(state=NORMAL)
        exportTrain_but.config(state=NORMAL)


    conWin = Toplevel()
    conWin.grab_set()
    conWin.geometry('470x250+730+230')
    conWin.title("Database Connection")
    conWin.resizable(0, 0)

    hostLabel = Label(conWin, text="Host name", font=('arial', 20, 'bold'))
    hostLabel.grid(row=0, column=0, padx=20)

    hostEntry = Entry(conWin, font=('roman', 15, 'bold'), bd=2)
    hostEntry.grid(row=0, column=1, pady=20, padx=40)

    userLabel = Label(conWin, text="User name", font=('arial', 20, 'bold'))
    userLabel.grid(row=1, column=0, padx=20)

    userEntry = Entry(conWin, font=('roman', 15, 'bold'), bd=2)
    userEntry.grid(row=1, column=1, pady=20, padx=40)

    passw = Label(conWin, text="Password", font=('arial', 20, 'bold'))
    passw.grid(row=2, column=0, padx=20)

    passEntry = Entry(conWin, font=('roman', 15, 'bold'), bd=2)
    passEntry.grid(row=2, column=1, pady=20, padx=40)

    conButt = ttk.Button(conWin, text="Connect",command=Connect)
    conButt.grid(row=3, columnspan=2)


# login_window
ad_ent = ttkthemes.ThemedTk()
ad_ent.get_themes()
ad_ent.set_theme('radiance')
ad_ent.title("ADMIN")
ad_ent.geometry("1200x660+50+50")
ad_ent.resizable(0, 0)
ad_ent.iconbitmap('trainlogo.ico')
ad_ent.config(bg='black')

# DATE AND TIME
datetimeLabel = Label(ad_ent,
                      text="hello",
                      fg="white",
                      font=('times new roman', 16, 'bold'),
                      bg="black"
                      )
datetimeLabel.place(x=5, y=5)
clock()

s = "ADMIN ENTRIES ONLY!!"
headName = Label(ad_ent,
                 text=s,
                 font=('Consolas', 30, 'bold'),
                 fg='#ff3385',
                 bd=2,
                 bg='black')
headName.place(x=400, y=10)
slider()
# add slider to the text

con_but = ttk.Button(ad_ent, text="Connect Database", command=Con_data)
con_but.place(x=1000, y=20)

# frame
leftFrame = Frame(ad_ent, bg="black")
leftFrame.place(x=0, y=80, width=300, height=570)

# add train photo
logo_img = PhotoImage(file="train.png")
logo_lab = Label(leftFrame, image=logo_img, bd=0)
logo_lab.grid(row=0, column=0)

#  Buttons to the left
addTrain_but = ttk.Button(leftFrame, text="Add Train", width=15, state=DISABLED, command=add_train)
addTrain_but.grid(row=1, column=0, padx=30, pady=20)

searchTrain_but = ttk.Button(leftFrame, text="Search Train", width=15, state=DISABLED, command=search_train)
searchTrain_but.grid(row=2, column=0, padx=30, pady=5)

deleteTrain_but = ttk.Button(leftFrame, text="Delete Train", width=15, state=DISABLED, command=delete_train)
deleteTrain_but.grid(row=3, column=0, padx=30, pady=20)

updateTrain_but = ttk.Button(leftFrame, text="Update Train", width=15, state=DISABLED,command=update_train)
updateTrain_but.grid(row=4, column=0, padx=30, pady=15)

showTrain_but = ttk.Button(leftFrame, text="Show Train", width=15, state=DISABLED, command=show_train)
showTrain_but.grid(row=5, column=0, padx=30, pady=15)

exportTrain_but = ttk.Button(leftFrame, text="Export Data", width=15, state=DISABLED, command=export_train)
exportTrain_but.grid(row=6, column=0, padx=30, pady=15)

exit_but = ttk.Button(leftFrame, text="Exit", width=15, command=iexit)
exit_but.grid(row=7, column=0, padx=30, pady=15)


# right frame
rightFrame = Frame(ad_ent, bg="white")
rightFrame.place(x=260, y=80, width=850, height=570)

# Scrollbar
scrollBarHorizontal = Scrollbar(rightFrame, orient=HORIZONTAL)
scrollBarVertical = Scrollbar(rightFrame, orient=VERTICAL)

# tree view
trainTable = ttk.Treeview(rightFrame,
             columns=('Train_no', 'Train_Name', 'Source', 'Destination', 'Arr_time', 'Dep_time', 'Date', 'Seat_available'),
                          xscrollcommand=scrollBarHorizontal.set,
                          yscrollcommand=scrollBarVertical.set)
scrollBarHorizontal.config(command=trainTable.xview)
scrollBarVertical.config(command=trainTable.yview)

trainTable.pack(fill=BOTH, expand=1)
scrollBarHorizontal.pack(side=BOTTOM, fill=X)
scrollBarVertical.pack(side=RIGHT, fill=Y)

trainTable.heading('Train_no', text='Train_no')
trainTable.heading('Train_Name', text='Train_Name')
trainTable.heading('Source', text='Source')
trainTable.heading('Destination', text='Destination')
trainTable.heading('Arr_time', text='Arr_time')
trainTable.heading('Dep_time', text='Dep_time')
trainTable.heading('Date', text='Date')
trainTable.heading('Seat_available', text='Seat_available')

trainTable.column('Train_no', width=100, anchor=CENTER)
trainTable.column('Train_Name', width=200, anchor=CENTER)
trainTable.column('Source', width=200, anchor=CENTER)
trainTable.column('Destination', width=200, anchor=CENTER)
trainTable.column('Arr_time', width=100, anchor=CENTER)
trainTable.column('Dep_time', width=100, anchor=CENTER)
trainTable.column('Date', width=100, anchor=CENTER)
trainTable.column('Seat_available', width=200, anchor=CENTER)

style = ttk.Style()
style.configure('Treeview', rowheight=40, font=('arial', 12, 'bold'), foreground='black', background='yellow', feildbackground='yellow')
style.configure('Treeview.Heading', font=('arial', 14, 'bold'))


trainTable.config(show='headings')

ad_ent.mainloop()
