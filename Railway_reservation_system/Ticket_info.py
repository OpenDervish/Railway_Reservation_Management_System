
from tkinter import *
from tkcalendar import *
from tkinter import messagebox, filedialog
import time
import ttkthemes  # here this module is being used for the button
from tkinter import ttk
import pandas
import pymysql

# Create the main window
tick_ent = ttkthemes.ThemedTk()
tick_ent.get_themes()
tick_ent.set_theme('radiance')
tick_ent.title("BOOKING INFORMATION PAGE")
tick_ent.geometry("1200x660+50+50")
tick_ent.resizable(0, 0)
tick_ent.iconbitmap('trainlogo.ico')
tick_ent.config(bg='black')

#/////////////////////////////////////////////////////////////////////

#////////////////////////////////////////////////////////////////////////




# Create the two frames
frame0 = Frame(tick_ent,background='black')
frame1 = Frame(tick_ent,background='grey')
frame2 = Frame(tick_ent,background='grey')

# Pack the frames onto the window
frame0.pack(pady=10,padx=10,side=TOP,fill=BOTH)
frame1.pack(pady=10,padx=10,side=LEFT,expand=TRUE,fill=BOTH)
frame2.pack(pady=10,padx=10,side=LEFT,expand=TRUE,fill=BOTH)


# Add some widgets to the frames
label0 = Label(frame0, text="TRAIN TICKET INFORMATION",font=('times new roman', 40, 'bold'),bg='black',fg='white')
label0.pack(padx=20,pady=20)

label1 = Label(frame1, text="This is frame 1")
label1.pack(padx=20,pady=20)

label2 = Label(frame2, text="This is frame 2")
label2.pack(padx=20,pady=20)


# Run the main loop
tick_ent.mainloop()
