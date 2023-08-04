from tkinter import messagebox
from tkinter import *
import customtkinter as ck
from pandas.io import sql

import DBConnect
# import entryForm as frm
import trails as tr
import sys
def login(usname):
    def optionmenu_callback(choice):
        print("optionmenu dropdown clicked:", choice)
        con = DBConnect.connect_db()
        cur = con.cursor()
        text = str(choice)
        # text="2020"
        query = "select * from placed where batch =" + text + " ;"
        print(query)
        cur.execute(query)
        fetchall = cur.fetchall()
        # con.close()
        funct1(fetchall)
    def funct1(fetchall):
        sys.setrecursionlimit(1000000000)

        app = ck.CTk()
        app.title("Student Details")
        app.iconbitmap("Files\\icon.ico")
        # Create A Main Frame
        app.geometry("1080x900")
        app.state("zoomed")
        main_frame = ck.CTkFrame(app)
        main_frame.pack(fill=BOTH, expand=2)

        # Create A Canvas
        my_canvas = ck.CTkCanvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Add A Scrollbar To The Canvas
        my_scrollbar = ck.CTkScrollbar(main_frame, orientation="vertical", command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)
        my_scrollbar1 = ck.CTkScrollbar(app, orientation="horizontal", command=my_canvas.xview)
        my_scrollbar1.pack(side=TOP, fill=X)

        # Configure The Canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
        my_canvas.configure(xscrollcommand=my_scrollbar1.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

        # Create ANOTHER Frame INSIDE the Canvas
        second_frame = ck.CTkFrame(my_canvas)

        # Add that New frame To a Window In The Canvas
        my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

        conb = DBConnect.connect_db()
        curb = conb.cursor()
        # curb.execute("CALL `Total`("''+str(optionmenu_var.get())+"')")
        print(str(optionmenu_var.get()))
        curb.execute("CALL `Total`('"+str(optionmenu_var.get())+"');")
        # "CALL `Total`('2020');"
        procedure=curb.fetchall()
        conb.close()
        print("Procedure",procedure[0][0])
        ck.CTkLabel(app, text="Total " + str(procedure[0][0]) + " Number of Students got placed of "+str(optionmenu_var.get())+" batch", font=("arial", 20, "bold"))\
            .pack(side=BOTTOM,anchor=CENTER)
        label0 = ck.CTkButton(second_frame, border_width=2, text="SLNo", state="disabled", height=5,
                              width=60, corner_radius=20)
        label0.grid(row=1, column=0)
        label1 = ck.CTkButton(second_frame, border_width=2, text="Name", state="disabled", height=5,
                              width=135, corner_radius=20).grid(row=1, column=1)
        label2 = ck.CTkButton(second_frame, border_width=2, text="USN", state="disabled", height=5,
                              width=135, corner_radius=20).grid(row=1, column=2)
        label3 = ck.CTkButton(second_frame, text="Branch", border_width=2, state="disabled", height=5,
                              width=135, corner_radius=20).grid(row=1, column=3)
        label4 = ck.CTkButton(second_frame, text="Batch", border_width=2, state="disabled", height=5,
                              width=135, corner_radius=20).grid(row=1, column=4)
        label5 = ck.CTkButton(second_frame, text="Email", border_width=2, state="disabled", height=5,
                              width=135, corner_radius=20).grid(row=1, column=5)
        label6 = ck.CTkButton(second_frame, text="Mobile", border_width=2, state="disabled", height=5,
                              width=135, corner_radius=20).grid(row=1, column=6)
        label7 = ck.CTkButton(second_frame, text="DOB", border_width=2, state="disabled", height=5,
                              width=135, corner_radius=20).grid(row=1, column=7)
        label8 = ck.CTkButton(second_frame, text="Company", border_width=2, state="disabled", height=5,
                              width=135, corner_radius=20).grid(row=1, column=8)
        # label9 = ck.CTkButton(second_frame, text="Offers", border_width=2, state="disabled", height=5,
        #                       width=135, corner_radius=20).grid(row=1, column=9)
        label10 = ck.CTkButton(second_frame, text="Designation", border_width=2, state="disabled",
                               height=5, width=135, corner_radius=20).grid(row=1, column=9)
        label11 = ck.CTkButton(second_frame, text="Package", border_width=2, state="disabled", height=5,
                               width=135, corner_radius=20).grid(row=1, column=10)
        label12 = ck.CTkButton(second_frame, text="Logs Date", border_width=2, state="disabled", height=5,
                               width=135, corner_radius=20).grid(row=1, column=11)

        i = 3
        slno = 1

        for row in fetchall:
            listOdIf = row[0]
            for j in range(0, len(row)):

                if (j == 0):
                    slNoE = ck.CTkTextbox(second_frame, width=60, height=5)

                    slNoE.grid(row=i, column=j)
                    slNoE.grid(row=i, column=j)
                    slNoE.insert("0.0", str(slno))
                # slNoE.bind("<Key>", lambda a: "break")
                studentIdE = ck.CTkTextbox(second_frame, width=135, height=5)
                # studentIdE.grid(row=i, column=j + 1)
                studentIdE.grid(row=i, column=j + 1)
                studentIdE.insert("0.0", str(row[j]))
            # studentIdE.bind("<Key>", lambda a: "break")
            i += 1
            slno += 1

        print(i)
        # tabview.configure(require_redraw=True)
        # root.mainloop()
        btn1 = ck.CTkButton(second_frame, text="Back", command=app.withdraw)
        btn1.grid(row=i + 2, column=6)

        # tabview.configure(require_redraw=True)
        app.mainloop()
        # del app

    root=ck.CTk()
    root.geometry("600x600")
    # txt=password()
    # root.title("")
    root.iconbitmap("Files\\icon.ico")
    txt = usname
    root.title("LoggedIn As "+txt)


    # txt="mam"
    batch=tr.batch()
    print(batch)
    # branch=tr. branch()
    # company=tr.company()
    ck.CTkLabel(root,text="Welcome "+str(txt),font=("arial",20,"bold")).pack(padx=100,side="top",anchor="center")
    ck.CTkLabel(root,text="Retrive Placed Student Details").place(relx=.3, rely=.4, anchor="center")
    optionmenu_var = ck.StringVar(value="2020")  # set initial value
    combobox = ck.CTkComboBox(root,
                                         values=batch,
                                         command=optionmenu_callback,
                                         variable=optionmenu_var)
    combobox.place(relx=.58, rely=.4, anchor="center")
    btn6 = ck.CTkButton(root, text="Logout", command=root.withdraw)
    btn6.place(relx=.5, rely=.9, anchor="center")
    root.mainloop()


def time():
    from datetime import datetime as dt

    # Getting current date and time
    now = dt.now()
    s = now.strftime(" %I  %M %p ||  %a - %m - %y")
    print('\nExample 1:', s)
# time()
# login("Ashhad")