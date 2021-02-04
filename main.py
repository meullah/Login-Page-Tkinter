import tkinter as tk
from tkinter import messagebox  
import re

from login import login


win = tk.Tk()
win.geometry('600x320')
win.resizable(width=0, height=0)
win.title('Bakary Managment System')
main_title = tk.Frame(win,bg='#f0f0f0')
main_title.pack(fill='both', expand = True)

username_var = tk.StringVar()
password_var = tk.StringVar()

label = tk.Label( main_title, 
                    text="Bakery Management System", 
                    font = 'Arial 32 bold', 
                    bg='#59989c', 
                    borderwidth=10, 
                    relief="ridge")
label.pack()

user_info = tk.Frame(main_title,
                    bg='#f0f0f0', 
                    borderwidth=10,
                    relief="ridge")
user_info.pack(fill='both')

tk.Label(user_info, text="Username      ",
                    fg="blue",
                    font = 'Arial 18 bold', padx = 50).grid(row = 0, column  = 0)
tk.Entry(user_info, textvariable  = username_var,
                    borderwidth=10,
                    relief="sunken",
                    font = 'Arial 18 bold',
                    bg="yellow").grid(row = 0, column  = 1)

tk.Label(user_info, text="Password      ",
                    fg="black",
                    font = 'Arial 18 bold', padx = 50).grid(row = 1, column  = 0)
tk.Entry(user_info, textvariable  = password_var,
                    borderwidth=10,
                    relief="sunken",
                    font = 'Arial 18 bold',
                    show='*',
                    bg="#f0f0f0").grid(row = 1, column  = 1)                    


app_button = tk.Frame(main_title,
                    bg='#f0f0f0', 
                    borderwidth=10,
                    relief="ridge")
app_button.pack(fill='both')

app_button.grid_columnconfigure(0, weight=1)
app_button.grid_rowconfigure(0, weight=1)
tk.Button(app_button, font = 'Arial 12 bold' ,text=' Login ',command=lambda: handle_login_button()).grid(row = 0, column  = 0,sticky='nesw')
app_button.grid_columnconfigure(1, weight=1)
app_button.grid_rowconfigure(1, weight=1)
tk.Button(app_button, font = 'Arial 12 bold' ,text=' Reset ',command=lambda: handle_Reset_button()).grid(row = 0, column  = 1,sticky='nesw')
app_button.grid_columnconfigure(2, weight=1)
app_button.grid_rowconfigure(2, weight=1)
tk.Button(app_button, font = 'Arial 12 bold' ,text=' Exit Window ',command=lambda: handle_Exit_button()).grid(row = 0, column  = 2,sticky='nesw')

action_button = tk.Frame(main_title,
                    bg='#f0f0f0', 
                    borderwidth=10,
                    relief="ridge")
action_button.pack(fill='both')

action_button.grid_columnconfigure(0, weight=1)
action_button.grid_rowconfigure(0, weight=1)
btn_stock = tk.Button(action_button, font = 'Arial 12 bold' ,text=' Stock ',state="disabled",command=lambda: handle_Stock_button())
btn_stock.grid(padx = 10, pady=5 ,row = 0, column  = 0,sticky='nesw')
action_button.grid_columnconfigure(1, weight=1)
action_button.grid_rowconfigure(1, weight=1)
btn_sell = tk.Button(action_button, font = 'Arial 12 bold' ,text=' Sell ',state="disabled",command=lambda: handle_Sell_button())
btn_sell.grid(padx = 10, pady=5, row = 0, column  = 1,sticky='nesw')




def handle_login_button():
    if(detect_special_characer(username_var.get())):
        if(password_var != ""):
            if(login(username_var.get(),password_var.get())):
                btn_sell['state'] = 'active'
                messagebox.showinfo("Login", "Sucessfull")
                handle_Reset_button()
            else:
                messagebox.showerror("login", "username or password is incorrect")
    else:
        messagebox.showerror("login", "No Special Character, username incorrect") 
def handle_Stock_button():
    messagebox.showinfo("Stocks", "Stocks button pressed")

def handle_Sell_button():
    messagebox.showinfo("Sell", "Sell button pressed")
          
def handle_Reset_button():
    username_var.set("")
    password_var.set("")

def handle_Exit_button():
    win.destroy()
    

def detect_special_characer(pass_string): 
    regex= re.compile('[@_!#$%^&*()<>?/\|}{~:]') 
    test = regex.search(pass_string)
    print(test)
    if(regex.search(pass_string) == None): 
        res = False
    else: 
        res = True
    return(res)


win.mainloop()