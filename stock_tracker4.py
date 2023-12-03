import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk
import mysql.connector
import style

ctk.set_appearance_mode("dark")  # setting mode for the window
ctk.set_default_color_theme("blue")  # sets the colors for the objects


def generate():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="#naga2020", database="stocks")
    mycursor = mydb.cursor()
    mycursor.execute("select * from stock_info")
    i = 0
    for row in mycursor:
        table.insert("", i, values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        i += 1
    mydb.commit()
    mydb.close()
    messagebox.showinfo("Successful", "All records generated")


# Function Definitions
def insert():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="#naga2020", database='stocks')
    mycursor = mydb.cursor()
    mycursor.execute("insert into stock_info values(%s,%s,%s,%s,%s,%s,%s,%s)", (
        name_entry.get(),
        price_entry.get(),
        quantity_entry.get(),
        total_entry.get(),
        buy_date_entry.get(),
        sell_price_entry.get(),
        sell_date_entry.get(),
        profit_entry.get(),
    ))
    mydb.commit()
    mydb.close()
    messagebox.showinfo("Success", "Record has been inserted")
    generate()


def search():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="#naga2020", database='stocks')
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM stock_info WHERE stock_name = %s", (name_entry.get(),))
    result = mycursor.fetchall()
    for row in result:
        price_entry.insert(0, row[1])
        quantity_entry.insert(0,row[2])
        total_entry.insert(0,row[3])
        buy_date_entry.insert(0,row[4])
        sell_price_entry.insert(0,row[5])
        sell_date_entry.insert(0,row[6])
        profit_entry.insert(0,row[7])

def update():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="#naga2020", database='stocks')
    mycursor = mydb.cursor()
    update_query = """
        UPDATE stock_info
        SET 
            stock_name = %s,
            price = %s,
            quantity = %s,
            total = %s,
            buy_date = %s,
            sell_price = %s,
            sell_date = %s,
            profit = %s
        WHERE stock_name = %s
    """
    mycursor.execute(update_query, (name_entry.get(),
                                    price_entry.get(),
                                    quantity_entry.get(),
                                    total_entry.get(),
                                    buy_date_entry.get(),
                                    sell_price_entry.get(),
                                    sell_date_entry.get(),
                                    profit_entry.get(),
                                    name_entry.get()))
    mydb.commit()
    mydb.close()
    messagebox.showinfo("Success", "Updated successfully")

def clear():
    name_entry.delete(0,tk.END)
    price_entry.delete(0,tk.END)
    quantity_entry.delete(0, tk.END)
    total_entry.delete(0, tk.END)
    buy_date_entry.delete(0, tk.END)
    sell_price_entry.delete(0, tk.END)
    sell_date_entry.delete(0, tk.END)
    profit_entry.delete(0,tk.END)

def delete():
    pass

def calculate_total(*args):
    try:
        quantity = float(quantity_var.get())
        price = float(price_var.get())
        total = quantity * price
        total_var.set(f"{total:.2f}")
    except ValueError:
        total_var.set("")

def calculate_profit(*args):
    try:
        quantity = float(quantity_var.get())
        sell_price=float(sell_var.get())
        price = float(price_var.get())
        profit=(price*quantity)-(sell_price*quantity)
        profit_var.set(f"{profit:.2f}")
    except ValueError:
        profit_var.set("")




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


name_label = ctk.CTkLabel(tab1, text='Stock Name', font=('Ex 2.0', 15, 'bold')).place(x=10, y=10)
name_entry = ctk.CTkEntry(tab1)
name_entry.place(x=150, y=10)

price_label = ctk.CTkLabel(tab1, text='Price', font=('Ex 2.0', 15, 'bold')).place(x=10, y=40)
price_var=tk.StringVar()
price_entry = ctk.CTkEntry(tab1,textvariable= price_var)
price_entry.place(x=150, y=40)

quantity_label = ctk.CTkLabel(tab1, text='Quantity', font=('Ex 2.0', 15, 'bold')).place(x=10, y=70)
quantity_var=tk.StringVar()
quantity_entry = ctk.CTkEntry(tab1,textvariable=quantity_var)
quantity_entry.place(x=150, y=70)

total_label = ctk.CTkLabel(tab1, text='Total Price', font=('Ex 2.0', 15, 'bold')).place(x=10, y=100)
total_var=tk.StringVar()
total_entry = ctk.CTkEntry(tab1,textvariable=total_var)
total_entry.place(x=150, y=100)


buy_date_label = ctk.CTkLabel(tab1, text='Buy date', font=('Ex 2.0', 15, 'bold')).place(x=10, y=130)
buy_date_entry = ctk.CTkEntry(tab1)
buy_date_entry.place(x=150, y=130)

sell_price_label = ctk.CTkLabel(tab1, text='Sell Price', font=('Ex 2.0', 15, 'bold')).place(x=10, y=160)
sell_var=tk.StringVar()
sell_price_entry = ctk.CTkEntry(tab1,textvariable=sell_var)
sell_price_entry.place(x=150, y=160)

sell_date_label = ctk.CTkLabel(tab1, text='Sell date', font=('Ex 2.0', 15, 'bold')).place(x=10, y=190)
sell_date_entry = ctk.CTkEntry(tab1)
sell_date_entry.place(x=150, y=190)

profit_label = ctk.CTkLabel(tab1, text='Profit gained', font=('Ex 2.0', 15, 'bold')).place(x=10, y=220)
profit_var=tk.StringVar()
profit_entry = ctk.CTkEntry(tab1,textvariable=profit_var)
profit_entry.place(x=150, y=220)

quantity_var.trace_add("write", calculate_total)
price_var.trace_add("write", calculate_total)
sell_var.trace_add("write",calculate_profit)


# Buttons
generate_btn = ctk.CTkButton(tab1, text='GENERATE DATA', font=('sans', 15, 'bold'), fg_color='green', width=10,
                             command=generate).place(x=100, y=400)
update_btn = ctk.CTkButton(tab1, text='UPDATE', font=('sans', 15, 'bold'), fg_color='green', width=10,
                             command=update).place(x=250, y=400)
insert_btn = ctk.CTkButton(tab1, text='INSERT', font=('sans', 15, 'bold'), fg_color='green', width=10,
                           command=insert).place(x=0, y=300)
search_btn = ctk.CTkButton(tab1, text='SEARCH', font=('sans', 15, 'bold'), fg_color='green', width=10,
                           command=search).place(x=100, y=300)
delete_btn = ctk.CTkButton(tab1, text='DELETE', font=('sans', 15, 'bold'), fg_color='green', width=10,
                           command=delete).place(x=200, y=300)
clear_btn = ctk.CTkButton(tab1, text='CLEAR', font=('sans', 15, 'bold'), fg_color='green', width=10,
                              command=clear).place(x=300, y=300)

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

table.tag_configure("gray",background="lightgray")

table.pack(fill='both', expand=1)



app.mainloop()
