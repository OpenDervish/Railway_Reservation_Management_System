
from tkinter import *
from tkcalendar import *
from tkinter import messagebox, filedialog
import time
import ttkthemes  # here this module is being used for the button
from tkinter import ttk
import pandas
import pymysql
import random
import traceback




def Pay(seatN,pn,se):

    def upd(b, c, totamt, pn):
        query = 'insert into payment_new(Bank,Card_no,Amount,pn_no) values(%s,%s,%s,%s)'
        mycursor.execute(query, (b, c, totamt, pn))
        con.commit()
        messagebox.showinfo("SUCCESS", "Amount paid successfully and ticket is confirmed")
        Payment_ent.destroy()



    tick_ent.destroy()
    Payment_ent = ttkthemes.ThemedTk()
    Payment_ent.get_themes()
    Payment_ent.set_theme('radiance')
    Payment_ent.title("PAYMENT PAGE")
    Payment_ent.geometry("900x500+50+50")
    Payment_ent.resizable(0, 0)
    Payment_ent.iconbitmap('trainlogo.ico')
    Payment_ent.config(bg='black')

    # Create the two frames
    frame0 = Frame(Payment_ent, background='black')
    frame1 = Frame(Payment_ent, background='grey')

    # Pack the frames onto the window
    frame0.pack(pady=10, padx=10, side=TOP, fill=BOTH)
    frame1.pack(pady=10, padx=10, side=LEFT, expand=TRUE, fill=BOTH)

    # Add some widgets to the frames
    label0 = Label(frame0, text="PAYMENT ENTRIES", font=('times new roman', 30, 'bold'), bg='black',
                   fg='white')
    label0.pack(padx=20, pady=20)

    # *****************************************************************************
    # -------------------------------------------------------------------------------

    amt_label = Label(frame1, bg='grey', text='Amount', font=('times new roman', 25, 'bold'))
    amt_label.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    amt_Entry = Entry(frame1, foreground='black', font=('Consolas', 15, 'bold'), width=24)
    amt_Entry.grid(row=0, column=1, pady=15, padx=10)

    Bank_label = Label(frame1, bg='grey', text='Bank', font=('times new roman', 25, 'bold'))
    Bank_label.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    Bank_Entry = Entry(frame1, foreground='black', font=('Consolas', 15, 'bold'), width=24)
    Bank_Entry.grid(row=1, column=1, pady=15, padx=10)

    # -------------------------------------------------------------------------------
    card_label = Label(frame1, bg='grey', text='Card_No', font=('times new roman', 25, 'bold'))
    card_label.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    card_Entry = Entry(frame1, foreground='black', font=('Consolas', 15, 'bold'), width=24)
    card_Entry.grid(row=2, column=1, pady=15, padx=10)

    # -------------------------------------------------------------------------------
    pnr_label = Label(frame1, bg='grey', text='Pnr_no', font=('times new roman', 25, 'bold'))
    pnr_label.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    pnr_Entry = Entry(frame1, foreground='black', font=('Consolas', 15, 'bold'), width=24)
    pnr_Entry.grid(row=3, column=1, pady=15, padx=10)


    # -------------------------------------------------------------------------------
    pnr_Entry.insert(0, pn)
    pnr_Entry.config(state=DISABLED)


    query= 'select Fare from class where Train_num=%s'
    mycursor.execute(query, se)
    data = mycursor.fetchone()
    amt=data[0]
    totamt = int(amt) *int(seatN)
    amt_Entry.insert(0, totamt)
    amt_Entry.config(state=DISABLED)

    update_but = ttk.Button(frame1, text="CONFIRM", command=lambda:upd(Bank_Entry.get(),card_Entry.get(),totamt,pn))
    update_but.grid(row=4,column=0, padx=10, pady=15)


def jhi(unams, seatnams,sab):

    # cont_win.destroy()
    # update_win.destroy()
    # ad_ent.destroy()
    global pnr_Entry

#//////lobal user_Entry///////////////////////////////////////////////////
    li = range(0, 100)
    # we use this list to get non-repeating elemets
    hi = random.sample(li, 1)
    pnrno = ' '.join(map(str, hi))

    if(int(sab)>0 and (int(seatnams) < int(sab))):
        # query = 'update rail set Seat_available=Seat_available-%s where Train_no=%s'
        # mycursor.execute(query,(int(seatnams),listdata[0]))
        try:
            query = 'CREATE TRIGGER seat_update AFTER INSERT ON ticket FOR EACH ROW update rail r set r.Seat_available = r.Seat_available-%s where Train_no=%s';
            mycursor.execute(query, (int(seatnams), listdata[0]))
            con.commit()
            messagebox.showinfo('Success',"seat reduced")
        except:
            query='drop trigger seat_update'
            mycursor.execute(query)
            con.commit()
            query = 'CREATE TRIGGER seat_update AFTER INSERT ON ticket FOR EACH ROW update rail r set r.Seat_available = r.Seat_available-%s where Train_no=%s';
            mycursor.execute(query, (int(seatnams), listdata[0]))
            con.commit()
            messagebox.showinfo('Success', "seat reduced")

    else:
        messagebox.showerror("Error", "Insufficient seats")
        return

    try:
        query = 'insert into ticket values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        mycursor.execute(query, (str(pnrno), listdata[0],
                                 listdata[1], listdata[2],
                                 listdata[3], listdata[4],
                                 listdata[5], listdata[6],
                                 listdata[7], str(unams)
                                 ))
        con.commit()
        messagebox.showinfo("Success status","Successfully terminated")
    except:
        messagebox.showerror("Error", "Ticket details couldnt be added")
        return


    print(seatnams)
    print(sab)
    sel_train = listdata[0]

    ghi = seatnams

    # Create the main window
    global tick_ent
    tick_ent = ttkthemes.ThemedTk()
    tick_ent.get_themes()
    tick_ent.set_theme('radiance')
    tick_ent.title("BOOKING INFORMATION PAGE")
    tick_ent.geometry("1000x700+50+50")
    tick_ent.resizable(0, 0)
    tick_ent.iconbitmap('trainlogo.ico')
    tick_ent.config(bg='black')



    # Create the two frames
    frame0 = Frame(tick_ent, background='black')
    frame1 = Frame(tick_ent, background='grey')


    # Pack the frames onto the window
    frame0.pack(pady=10, padx=10, side=TOP, fill=BOTH)
    frame1.pack(pady=10, padx=10, side=LEFT, expand=TRUE, fill=BOTH)


    # Add some widgets to the frames
    label0 = Label(frame0, text="TRAIN TICKET INFORMATION", font=('times new roman', 20, 'bold'), bg='black',
                   fg='white')
    label0.pack(padx=20, pady=20)

   # *****************************************************************************
    # -------------------------------------------------------------------------------


    pnr_label = Label(frame1, bg='grey', text='Pnr_no', font=('times new roman', 15, 'bold'))
    pnr_label.grid(row=0, column=0, padx=30, pady=15, sticky=W)

    pnr_Entry = Entry(frame1, foreground='black', font=('Consolas', 15, 'bold'), width=24)
    pnr_Entry.grid(row=0, column=1, pady=15, padx=10)


    No_label = Label(frame1, bg='grey',text='Train_no', font=('times new roman', 15, 'bold'))
    No_label.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    No_Entry = Entry(frame1,foreground='black', font=('Consolas', 15, 'bold'), width=24)
    No_Entry.grid(row=1, column=1, pady=15, padx=10)

    # -------------------------------------------------------------------------------
    Tn_label = Label(frame1, bg='grey', text='Train_name', font=('times new roman', 15, 'bold'))
    Tn_label.grid(row=2 ,column=0, padx=30, pady=15, sticky=W)
    Tn_Entry = Entry(frame1,foreground='black', font=('Consolas', 15, 'bold'), width=24)
    Tn_Entry.grid(row=2, column=1, pady=15, padx=10)

    # -------------------------------------------------------------------------------
    src_label = Label(frame1,bg='grey', text='Source', font=('times new roman', 15, 'bold'))
    src_label.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    src_Entry = Entry(frame1,foreground='black', font=('Consolas', 15, 'bold'), width=24)
    src_Entry.grid(row=3, column=1, pady=15, padx=10)
    # -------------------------------------------------------------------------------
    dest_label = Label(frame1,bg='grey', text='Destination', font=('times new roman', 15, 'bold'))
    dest_label.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    dest_Entry = Entry(frame1,foreground='black', font=('Consolas', 15, 'bold'), width=24)
    dest_Entry.grid(row=4, column=1, pady=15, padx=10)
    # -------------------------------------------------------------------------------
    at_label = Label(frame1,bg='grey', text='Arrival_time', font=('times new roman', 15, 'bold'))
    at_label.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    at_Entry = Entry(frame1,foreground='black', font=('Consolas', 15, 'bold'), width=24)
    at_Entry.grid(row=5, column=1, pady=15, padx=10)
    # -------------------------------------------------------------------------------
    dt_label = Label(frame1,bg='grey', text='Departure_time', font=('times new roman', 15, 'bold'))
    dt_label.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    dt_Entry = Entry(frame1,foreground='black', font=('Consolas', 15, 'bold'), width=24)
    dt_Entry.grid(row=6, column=1, pady=15, padx=10)
    # -------------------------------------------------------------------------------
    dist_label = Label(frame1,bg='grey', text='Date', font=('times new roman', 15, 'bold'))
    dist_label.grid(row=7, column=0, padx=30, pady=15, sticky=W)
    dist_Entry = Entry(frame1,foreground='black', font=('Consolas', 15, 'bold'), width=24)
    dist_Entry.grid(row=7, column=1, pady=15, padx=10)

    seno_label = Label(frame1, bg='grey', text='Seat_no', font=('times new roman', 15, 'bold'))
    seno_label.grid(row=8, column=0, padx=30, pady=15, sticky=W)
    seno_Entry = Entry(frame1, foreground='black', font=('Consolas', 15, 'bold'), width=24)
    seno_Entry.grid(row=8, column=1, pady=15, padx=10)


    usna_label = Label(frame1, bg='grey', text='Username', font=('times new roman', 15, 'bold'))
    usna_label.grid(row=9, column=0, padx=30, pady=15, sticky=W)
    usna_Entry = Entry(frame1, foreground='black', font=('Consolas', 15, 'bold'), width=24)
    usna_Entry.grid(row=9, column=1, pady=15, padx=10)


    contBut = ttk.Button(frame1, text="Continue", command=lambda:Pay(ghi,pnrno,sel_train),width=20)
    contBut.grid(row=2,column=3,pady=15,padx=100)
    cont_win.destroy()
    ad_ent.destroy()
    # bckBut = ttk.Button(frame1, text="Back", command=Pay, width=20)
    # bckBut.grid(row=4, column=3, pady=15, padx=100)
   # *******************************************************************************

    pnr_Entry.insert(0, pnrno)
    No_Entry.insert(0, listdata[0])
    Tn_Entry.insert(0, listdata[1])
    src_Entry.insert(0, listdata[2])
    dest_Entry.insert(0, listdata[3])
    at_Entry.insert(0, listdata[4])
    dt_Entry.insert(0, listdata[5])
    dist_Entry.insert(0, listdata[6])
    seno_Entry.insert(0,listdata[7])
    usna_Entry.insert(0, unams)

    pnr_Entry.config(state=DISABLED)
    No_Entry.config(state=DISABLED)
    Tn_Entry.config(state=DISABLED)
    src_Entry.config(state=DISABLED)
    dest_Entry.config(state=DISABLED)
    at_Entry.config(state=DISABLED)
    dt_Entry.config(state=DISABLED)
    dist_Entry.config(state=DISABLED)
    seno_Entry.config(state=DISABLED)
    usna_Entry.config(state=DISABLED)


    # Run the main loop
    tick_ent.mainloop()



#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



def BookTick():

    def update_data(swa):

        show_train()
        global cont_win
        cont_win = Toplevel()
        cont_win.title("Available Train seats")
        cont_win.resizable(False, False)
        cont_win.geometry('600x550')
        cont_win.grab_set()

        seat_label = Label(cont_win, bg='grey', text='Select number of seats', font=('times new roman', 20, 'bold'))
        seat_label.grid(row=1, column=0, padx=30, pady=15, sticky=W)
        seat_Entry = Entry(cont_win, foreground='black', font=('Consolas', 15, 'bold'), width=24)
        seat_Entry.grid(row=1, column=1, pady=15, padx=10)

        user_label = Label(cont_win, bg='grey', text='Enter Username', font=('times new roman', 20, 'bold'))
        user_label.grid(row=2, column=0, padx=30, pady=15, sticky=W)
        user_Entry = Entry(cont_win, foreground='black', font=('Consolas', 15, 'bold'), width=24)
        user_Entry.grid(row=2, column=1, pady=15, padx=10)

        s=swa
        subm_button = Button(cont_win, text='Generate ticket',command=lambda: jhi(user_Entry.get(), seat_Entry.get(),s))
        subm_button.grid(row=4, column=0)


        # if(int(sea)>0 and (int(sea) < int(swa))):
        #     query = 'update rail set Seat_available=Seat_available-%s'
        #     mycursor.execute(query, int(sea))
        #     con.commit()
        #     subm_button.config(command=lambda: jhi(user_Entry.get(), seat_Entry.get()))
        # else:
        #     messagebox.showerror("Error", "Insufficient seats")
        #     return




    global  update_win
    update_win = Toplevel()
    update_win.title("Train Details")
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

    update_but = ttk.Button(update_win, text="CONTINUE",command=lambda:update_data(sa_Entry.get()))
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


    No_Entry.config(state=DISABLED)
    Tn_Entry.config(state=DISABLED)
    src_Entry.config(state=DISABLED)
    dest_Entry.config(state=DISABLED)
    at_Entry.config(state=DISABLED)
    dt_Entry.config(state=DISABLED)
    dist_Entry.config(state=DISABLED)
    sa_Entry.config(state=DISABLED)





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

# show_train func
def show_train():
    query = 'select * from RAIL'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    trainTable.delete(*trainTable.get_children())
    for data in fetched_data:
        trainTable.insert('', END, values=data)


def Con_data():
    def Connect():
        global mycursor,con
        try:
            con= pymysql.connect(host='localhost', user='root', password='Swaroop@696')
            mycursor = con.cursor()

        except:
            messagebox.showerror("Error", "Invalid Details")
            return

# 'Train_no', 'Train_Name', 'Source', 'Destination', 'Arr_time', 'Dep_time', 'Date', 'Seat_available'
        try:
            mycursor.execute('create database AD_TRAIN')
            mycursor.execute('use AD_TRAIN')
            mycursor.execute('create table RAIL(Train_no int not null primary key,Train_Name varchar(30),Source varchar(30),Destination varchar(30),Arr_time varchar(15),Dep_time varchar(15),Date date,Seat_available int)')
            mycursor.execute('create table TICKET(Pnr_no varchar(10) primary key,Train_no int,Train_name varchar(30),Source varchar(30),Destination varchar(30),Arr_time varchar(15),Dep_time varchar(15),Date date,Seat_no int,Username varchar(20),foreign key(Username) references User(Username));')


        except:
            mycursor.execute('use AD_TRAIN')

        messagebox.showinfo("Success", "Database Connection is successful")
        searchTrain_but.config(state=NORMAL)
        showTrain_but.config(state=NORMAL)
        exportTrain_but.config(state=NORMAL)
        bookTick_but.config(state=NORMAL)



    conButt = ttk.Button(ad_ent, text="Connect", command=Connect)
    conButt.place(x=1000, y=30)


def search_train():
    def search_data():
        # to fetch data from database
        query = 'select * from RAIL,CLASS where (Source=%s or Destination = %s or Date=%s or Class_Type=%s) and RAIL.Train_no=CLASS.Train_num'
        mycursor.execute(query, (
        srcCombo.get(), destCombo.get(),cal.get_date(),claCombo.get()
        ))
        trainTable.delete(*trainTable.get_children())
        fetchdata = mycursor.fetchall()
        for data in fetchdata:
            trainTable.insert('', END, values=data)

    search_win = Toplevel()
    search_win.title("Search Train")
    search_win.resizable(False, False)
    search_win.grab_set()

    # -------------------------------------------------------------------------------
    # No_label = Label(search_win, text='Train_no', font=('times new roman', 20, 'bold'))
    # No_label.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    # No_Entry = Entry(search_win, font=('Consolas', 15, 'bold'), width=24)
    # No_Entry.grid(row=0, column=1, pady=15, padx=10)

    # -------------------------------------------------------------------------------
    # Tn_label = Label(search_win, text='Train_name', font=('times new roman', 20, 'bold'))
    # Tn_label.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    # Tn_Entry = Entry(search_win, font=('Consolas', 15, 'bold'), width=24)
    # Tn_Entry.grid(row=1, column=1, pady=15, padx=10)

    # -------------------------------------------------------------------------------
    src_label = Label(search_win, text='Source', font=('times new roman', 20, 'bold'))
    src_label.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    # src_Entry = Entry(search_win, font=('Consolas', 15, 'bold'), width=24)
    # src_Entry.grid(row=2, column=1, pady=15, padx=10)

    query = 'select distinct source from RAIL'
    mycursor.execute(query)
    fetched_data1 =mycursor.fetchall()
    l=[]
    for i in fetched_data1:
        l.append(i[0])

    srcCombo = ttk.Combobox(search_win,values=l, width=25,height=60,font=('times new roman', 11, 'bold'))

    srcCombo.grid(row=2, column=1, padx=10, pady=15)
    # -------------------------------------------------------------------------------
    dest_label = Label(search_win, text='Destination', font=('times new roman', 20, 'bold'))
    dest_label.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    # dest_Entry = Entry(search_win, font=('Consolas', 15, 'bold'), width=24)
    # dest_Entry.grid(row=3, column=1, pady=15, padx=10)

    cal_label = Label(search_win, text='Date', font=('times new roman', 20, 'bold'))
    cal_label.grid(row=4, column=0, padx=30, pady=15, sticky=W)

    cal = Calendar(search_win,selectmode="day",year=2023,month=1,day=1,date_pattern='yyyy-mm-dd')
    cal.grid(row=4,column=1,padx=20,pady=20)

    def grab_date():
        my_lab.config(text=cal.get_date())

    my_buto = Button(search_win,text="Get Date",font=('times new roman', 15, 'bold'),bd=5, command=grab_date)
    my_buto.grid(row=5,column=0,padx=50)
    my_lab = Label(search_win,text='',font=('times new roman', 20, 'bold'))
    my_lab.grid(row=5,column=1)

    #????????????????????????????????????????????????????????????????????????????/

    query = 'select distinct destination from RAIL'
    mycursor.execute(query)
    fetched_data2 = list(mycursor.fetchall())
    l1 = []
    for i in fetched_data2:
        l1.append(i[0])
    destCombo = ttk.Combobox(search_win, values=l1,font=('times new roman', 15, 'bold'), width=21)

    destCombo.grid(row=3, column=1, padx=10, pady=15)

    clas_label = Label(search_win, text='Class', font=('times new roman', 20, 'bold'))
    clas_label.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    query = 'select distinct Class_type  from CLASS'
    mycursor.execute(query)
    fetched_data1 = list(mycursor.fetchall())
    claCombo = ttk.Combobox(search_win, values=fetched_data1, width=25, height=60, font=('times new roman', 11, 'bold'))

    claCombo.grid(row=6, column=1, padx=10, pady=15)


    # -------------------------------------------------------------------------------
    # at_label = Label(search_win, text='Arrival_time', font=('times new roman', 20, 'bold'))
    # at_label.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    # at_Entry = Entry(search_win, font=('Consolas', 15, 'bold'), width=24)
    # at_Entry.grid(row=4, column=1, pady=15, padx=10)
    # -------------------------------------------------------------------------------
    # dt_label = Label(search_win, text='Departure_time', font=('times new roman', 20, 'bold'))
    # dt_label.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    # dt_Entry = Entry(search_win, font=('Consolas', 15, 'bold'), width=24)
    # dt_Entry.grid(row=5, column=1, pady=15, padx=10)
    # -------------------------------------------------------------------------------
    # dist_label = Label(search_win, text='Date', font=('times new roman', 20, 'bold'))
    # dist_label.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    # dist_Entry = Entry(search_win, font=('Consolas', 15, 'bold'), width=24)
    # dist_Entry.grid(row=6, column=1, pady=15, padx=10)
    # -------------------------------------------------------------------------------
    # sa_label = Label(search_win, text='Seats_available', font=('times new roman', 20, 'bold'))
    # sa_label.grid(row=7, column=0, padx=30, pady=15, sticky=W)
    # sa_Entry = Entry(search_win, font=('Consolas', 15, 'bold'), width=24)
    # sa_Entry.grid(row=7, column=1, pady=15, padx=10)

    searchButt = ttk.Button(search_win, text="Search Train", command=search_data)
    searchButt.grid(row=8, columnspan=2, pady=15)



# # fns
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


# login_window
ad_ent = ttkthemes.ThemedTk()
ad_ent.get_themes()
ad_ent.set_theme('radiance')
ad_ent.title("USER")
ad_ent.geometry("1200x660+50+50")
ad_ent.resizable(0, 0)
ad_ent.iconbitmap('trainlogo.ico')
ad_ent.config(bg='black')
Con_data()
# DATE AND TIME
datetimeLabel = Label(ad_ent,
                      text="hello",
                      fg="white",
                      font=('times new roman', 16, 'bold'),
                      bg="black"
                      )
datetimeLabel.place(x=5, y=5)
clock()

s = "WELCOME TO INDIAN RAILWAYS "
headName = Label(ad_ent,
                 text=s,
                 font=('Consolas', 30, 'bold'),
                 fg='#ff3385',
                 bd=2,
                 bg='black')
headName.place(x=400, y=10)
slider()
# add slider to the text


# frame
leftFrame = Frame(ad_ent, bg="black")
leftFrame.place(x=0, y=80, width=300, height=570)

# add train photo
logo_img = PhotoImage(file="train.png")
logo_lab = Label(leftFrame, image=logo_img, bd=0)
logo_lab.grid(row=0, column=0)

#  Buttons to the left
# addTrain_but = ttk.Button(leftFrame, text="Add Train", width=15, state=DISABLED)
# addTrain_but.grid(row=1, column=0, padx=30, pady=20)

searchTrain_but = ttk.Button(leftFrame, text="Search Train", width=15,state=DISABLED, command=search_train)
searchTrain_but.grid(row=2, column=0, padx=30, pady=5)

# deleteTrain_but = ttk.Button(leftFrame, text="Delete Train", width=15, state=DISABLED)
# deleteTrain_but.grid(row=3, column=0, padx=30, pady=20)

# updateTrain_but = ttk.Button(leftFrame, text="Update Train", width=15, state=DISABLED)
# updateTrain_but.grid(row=4, column=0, padx=30, pady=15)

showTrain_but = ttk.Button(leftFrame, text="Show Train", width=15, state=DISABLED,command=show_train)
showTrain_but.grid(row=5, column=0, padx=30, pady=15)

exportTrain_but = ttk.Button(leftFrame, text="Export Data", width=15, state=DISABLED,command=export_train)
exportTrain_but.grid(row=7, column=0, padx=30, pady=15)

bookTick_but = ttk.Button(leftFrame, text="Book Ticket", width=15, state=DISABLED,command=BookTick)
bookTick_but.grid(row=6, column=0, padx=30, pady=15)

exit_but = ttk.Button(leftFrame, text="Exit", width=15,command=iexit)
exit_but.grid(row=8, column=0, padx=30, pady=15)


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