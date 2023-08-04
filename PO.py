from tkinter import *
from tkinter import messagebox
import customtkinter as ck
import tkinter as tk
import LoginDatabase2
def suc():
    def dbs():

        usname = entry1.get()
        paswd = entry2.get()
        delete()
        LoginDatabase2.db(usname, paswd)

    def delete():
        entry1.delete(0, END)
        entry2.delete(0, END)

    def checkbox_event():
        value = entry2.get()
        print(value)
        print("checkbox toggled, current value:", check_var.get())
        if (check_var.get() == "on" and entry2.get() != ""):

            print("yes")
            entry2.configure(show="")

        elif (check_var.get() == "off"):
            entry2.configure(show="*")
        elif (entry2.get() == ""):
            messagebox.showerror(title="Error", message="Password field is empty")
            check_var.set("off")

    def onSucess():
        dbs()

    root = ck.CTk()

    root.title("Placement Login")
    root.iconbitmap("Files\\icon.ico")
    # p1=PhotoImage(file='H:\\Placement_Management\\Trails\\icon.png')
    # root.iconphoto(False,p1)
    root.geometry("600x400")
    root.maxsize(600, 400)

    ck.CTkLabel(root, text="Placement Login",
                width=120, height=25, fg_color=("white", "gray75")
                , corner_radius=8, font=("Times New Roman", 25)).pack(padx=50, side="top", anchor=CENTER)

    usnames = tk.StringVar()
    passwd = tk.StringVar()
    # USernameLabel
    label1 = ck.CTkLabel(root, text="Username")
    label1.place(relx=.3, rely=.4, anchor=CENTER)
    # UsernameEntry
    entry1 = ck.CTkEntry(root, textvariable=usnames)
    entry1.place(relx=.5, rely=.4, anchor=CENTER)
    # PasswordLabel
    label2 = ck.CTkLabel(root, text="Password")
    label2.place(relx=.3, rely=.5, anchor=CENTER)
    # PasswordEntry
    entry2 = ck.CTkEntry(root, textvariable=passwd, show="*")
    entry2.place(relx=.5, rely=.5, anchor=CENTER)
    check_var = tk.StringVar()

    # frame=ck.CTkFrame(root,width=)
    checkbox = ck.CTkCheckBox(root, text="Show", command=checkbox_event,
                              variable=check_var, onvalue="on", offvalue="off")
    checkbox.place(relx=.48, rely=.6, anchor=CENTER)
    button = ck.CTkButton(root, text="Login", command=onSucess)
    button.place(relx=.5, rely=.7, anchor=CENTER)
    button = ck.CTkButton(root, text="Close", command=root.withdraw)
    button.place(relx=.5, rely=.8, anchor=CENTER)
    ck.CTkButton(root, text="VERSION 1.0", state=DISABLED, border_width=5).pack(side="bottom")

    root.mainloop()


# suc()