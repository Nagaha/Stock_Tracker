import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import mysql.connector


ctk.set_appearance_mode("dark")#setting mode for the window
ctk.set_default_color_theme("blue")#sets the colors for the obejcts

#sql code
mydb=mysql.connector.connect(host="localhost",user="root",passwd="#naga2020")
mycursor=mydb.cursor()
mycursor.execute("use stocks")
mycursor.execute("select * from stock_details")



#App creation
app=ctk.CTk()
app.title("Stock Tracker")
app.geometry("1200x500")
app.resizable()

#frame creation
side_frame=ctk.CTkFrame(app,width=300, 
                        height=500,
                        border_color='gray',
                        border_width=3,
                        corner_radius=10)
side_frame.pack(side='left',expand='false')   

Main_frame=ctk.CTkFrame(app,width=900, 
                        height=500,
                        border_color='gray',
                        border_width=3,
                        corner_radius=10,
                        fg_color='black')
Main_frame.pack(side='right',expand='false') 

#tab view
menu=ctk.CTkTabview(side_frame,
                    width=300,
                    height=500,
                    fg_color='black',
                    segmented_button_fg_color='black',
                    segmented_button_selected_hover_color='green',
                    segmented_button_unselected_color='black')
tab1=menu.add("Search mode")
tab2=menu.add("Edit mode")

menu.pack(side='top',fill='y',expand='true')

#Search mode frame
label=ctk.CTkLabel(tab1,text='Stock Name')
name_entry=ctk.CTkEntry(tab1)

label.pack(side='left')
name_entry.pack(side='right')


label.pack(side='top')

#table
table=ttk.Treeview(Main_frame)
table['columns']=("Stock_Name","Buying_Price","Quantity","Total_spent")
table.column("Stock_Name",width=100,minwidth=50,anchor=tk.CENTER)
table.column("Buying_Price",width=100,minwidth=50,anchor=tk.CENTER)
table.column("Quantity",width=100,minwidth=50,anchor=tk.CENTER)
table.column("Total_spent",width=100,minwidth=50,anchor=tk.CENTER)


table.heading("Stock_Name",text='Stock Name',anchor=tk.CENTER)
table.heading("Buying_Price",text='Buying Price',anchor=tk.CENTER)
table.heading("Quantity",text='Quantity',anchor=tk.CENTER)
table.heading("Total_spent",text='Total Spent',anchor=tk.CENTER)

i=0
for row in mycursor:
    table.insert('',i,text="",values=(row[0],row[1],row[2],row[3]))
    i+=1
table.pack()


#objects
button=ttk.Button(master=app)

app.mainloop()
