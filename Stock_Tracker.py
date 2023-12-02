import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import mysql.connector
import style

ctk.set_appearance_mode("dark")  # setting mode for the window
ctk.set_default_color_theme("blue")  # sets the colors for the objects

# sql code
mydb = mysql.connector.connect(host="localhost", user="root", passwd="aishu@1234")
mycursor = mydb.cursor()

mycursor.execute("use stocks")
mycursor.execute("select * from stock_info")


def generate():
    i = 0
    for row in mycursor:
        table.insert("", i, values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        i += 1


# Function Definitions
def insert():
    stock_name = name_entry.get()
    stock_price = price_entry.get()
    stock_quantity = quantity_entry.get()
    total_price = total_entry.get()
    buy_date = buy_date_entry.get()
    sell_price = sell_price_entry.get()
    sell_date = sell_date_entry.get()
    sell_profit = profit_entry.get()

    # inserting the filed attributes to db
    table.insert("", 1, values=(
        stock_name, stock_price, stock_quantity, total_price, buy_date, sell_price, sell_date, sell_profit))

    pass


def update():
    pass


def delete():
    pass


def delete_all():
    pass


# App creation
app = ctk.CTk()
app.title("Stock Tracker")
app.geometry("1200x500")
app.resizable()

# frame creation
side_frame = ctk.CTkFrame(app, width=300,
                          height=500,
                          border_color='gray',
                          border_width=3,
                          corner_radius=10)
side_frame.pack(side='left', expand=0)

# tab view
menu = ctk.CTkTabview(side_frame,
                      width=500,
                      height=500,
                      fg_color='black',
                      segmented_button_fg_color='black',
                      segmented_button_selected_hover_color='green',
                      segmented_button_unselected_color='black')
tab1 = menu.add("View mode")
tab2 = menu.add("Calculate mode")

menu.pack(fill='both', expand=1)

# Search mode frame
# Search mode frame
name_label = ctk.CTkLabel(tab1, text='Stock Name', font=('Ex 2.0', 15, 'bold')).place(x=10, y=10)
name_entry = ctk.CTkEntry(tab1)
name_entry.place(x=150, y=10)

price_label = ctk.CTkLabel(tab1, text='Price', font=('Ex 2.0', 15, 'bold')).place(x=10, y=40)
price_entry = ctk.CTkEntry(tab1)
price_entry.place(x=150, y=40)

quantity_label = ctk.CTkLabel(tab1, text='Quantity', font=('Ex 2.0', 15, 'bold')).place(x=10, y=70)
quantity_entry = ctk.CTkEntry(tab1)
quantity_entry.place(x=150, y=70)

total_label = ctk.CTkLabel(tab1, text='Total Price', font=('Ex 2.0', 15, 'bold')).place(x=10, y=100)
total_entry = ctk.CTkEntry(tab1)
total_entry.place(x=150, y=100)

buy_date_label = ctk.CTkLabel(tab1, text='Buy date', font=('Ex 2.0', 15, 'bold')).place(x=10, y=130)
buy_date_entry = ctk.CTkEntry(tab1)
buy_date_entry.place(x=150, y=130)

sell_price_label = ctk.CTkLabel(tab1, text='Sell Price', font=('Ex 2.0', 15, 'bold')).place(x=10, y=160)
sell_price_entry = ctk.CTkEntry(tab1)
sell_price_entry.place(x=150, y=160)

sell_date_label = ctk.CTkLabel(tab1, text='Sell date', font=('Ex 2.0', 15, 'bold')).place(x=10, y=190)
sell_date_entry = ctk.CTkEntry(tab1)
sell_date_entry.place(x=150, y=190)

profit_label = ctk.CTkLabel(tab1, text='Profit gained', font=('Ex 2.0', 15, 'bold')).place(x=10, y=220)
profit_entry = ctk.CTkEntry(tab1)
profit_entry.place(x=150, y=220)

# Buttons
generate_btn = ctk.CTkButton(tab1, text='Generate Data', font=('sans', 15, 'bold'), fg_color='green', width=10,
                             command=generate).place(x=100, y=400)
insert_btn = ctk.CTkButton(tab1, text='INSERT', font=('sans', 15, 'bold'), fg_color='green', width=10,
                           command=insert).place(x=0, y=300)
update_btn = ctk.CTkButton(tab1, text='UPDATE', font=('sans', 15, 'bold'), fg_color='green', width=10,
                           command=update).place(x=100, y=300)
delete_btn = ctk.CTkButton(tab1, text='DELETE', font=('sans', 15, 'bold'), fg_color='green', width=10,
                           command=delete).place(x=200, y=300)
deleteAll_btn = ctk.CTkButton(tab1, text='DELETE ALL', font=('sans', 15, 'bold'), fg_color='green', width=10,
                              command=delete_all()).place(x=300, y=300)

# table
table = ttk.Treeview(app)
table['columns'] = ("Stock_Name", "Price", "Quantity", "Total_Price", "Buy_Date", "Sell_Price", "Sell_Date", "Profit")
table.column("#0", width=0, stretch='NO')
table.column("Stock_Name", width=100, minwidth=100, anchor=tk.CENTER)
table.column("Price", width=100, minwidth=100, anchor=tk.CENTER)
table.column("Quantity", width=100, minwidth=100, anchor=tk.CENTER)
table.column("Total_Price", width=100, minwidth=100, anchor=tk.CENTER)
table.column("Buy_Date", width=100, minwidth=100, anchor=tk.CENTER)
table.column("Sell_Price", width=100, minwidth=100, anchor=tk.CENTER)
table.column("Sell_Date", width=100, minwidth=100, anchor=tk.CENTER)
table.column("Profit", width=100, minwidth=100, anchor=tk.CENTER)

table.heading("Stock_Name", text='Stock Name', anchor=tk.CENTER)
table.heading("Price", text='Price per stock', anchor=tk.CENTER)
table.heading("Quantity", text='Quantity', anchor=tk.CENTER)
table.heading("Total_Price", text='Total price', anchor=tk.CENTER)
table.heading("Buy_Date", text='Buying date', anchor=tk.CENTER)
table.heading("Sell_Price", text='Selling Price', anchor=tk.CENTER)
table.heading("Sell_Date", text='Selling Date', anchor=tk.CENTER)
table.heading("Profit", text='Profit gained', anchor=tk.CENTER)

table.pack(fill='both', expand=1)

app.mainloop()
