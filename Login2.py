import customtkinter
from tkinter import messagebox
from tkinter import *
import sys
from datetime import datetime as dt
import customtkinter as ck
from pandas.io import sql
import entryForm2
import DBConnect
import entryForm as frm
import trails as tr
import company_batch
def login(usname):
    def getBC():
        print(comp)
        print(bat)
        company_batch.onsucess(comboboxc,comboboxb)
    def form():
        frm.onsucess()
    def insertyr(data):
            print("Hey",data)
            if data == "":
                messagebox.showwarning(message="Empty Field")
                return
            con = DBConnect.connect_db()
            cur1 = con.cursor()
            query = "insert into batch(batch_year) values('" + str(data) + "');"
            # if data in lst:
            #     messagebox.showwarning(message="already exist")
            try:
                if (not cur1.execute(query)):
                    messagebox.showinfo(title="Information",message="success")
                    con.commit()
                    con.close()
                else:
                    messagebox.showwarning(title="Warning",message="Query Didn't Executed Properly")
            except Exception as e:
                E=str(e)
                messagebox.showerror(title="Error",message=E[13:36])
    def insertcom(data1,data2,data3):
            print(data1)
            if data1 == "" or data2=="" or data3=="":
                messagebox.showwarning(message="Empty Field")
                return
            try:
                con = DBConnect.connect_db()
                cur1 = con.cursor()
                # cur1.execute("select * from company;")

                query = "insert into company values('" + str(data1) + "','" + str(data2) + "','" + str(data3) + "');"
                # if data in lst:
                #     messagebox.showwarning(message="already exist")
                if (not cur1.execute(query)):
                    con.commit()
                    con.close()
                    messagebox.showinfo(title="Information", message="success")

                else:
                    messagebox.showerror(title="Error",message="Something Went Wrong")
            except Exception as e:
                E=str(e)
                messagebox.showerror(title="Error",message=E[13:36])
    def getyear():
        print("Yes")
        window = ck.CTkToplevel(root)
        window.geometry("400x200")
        window.title("Placement Management")
        window.iconbitmap("Files\\icon.ico")
        # create label on CTkToplevel window
        label1 = ck.CTkLabel(window, text="Enter Batch Year")
        label1.pack()
        entry1 = ck.CTkEntry(window)
        entry1.pack()
        data = entry1.get()
        btn = ck.CTkButton(window, text="Add",command=lambda :insertyr(entry1.get()))
        btn.pack()
        window.mainloop()



        # insertyr(data)
    def getcompany():
        print("Yes")
        window = ck.CTkToplevel(root)
        window.geometry("400x200")

        window.title("Placement Management")
        window.iconbitmap("Files\\icon.ico")

        # create label on CTkToplevel window
        label1 = ck.CTkLabel(window, text="Enter Company Name")
        label1.pack()
        entry1 = ck.CTkEntry(window)
        entry1.pack()
        label2 = ck.CTkLabel(window, text="Enter Company Location")
        label2.pack()
        entry2 = ck.CTkEntry(window)
        entry2.pack()
        label3 = ck.CTkLabel(window, text="Enter Contact Number")
        label3.pack()
        entry3 = ck.CTkEntry(window)
        entry3.pack()

        btn = ck.CTkButton(window, text="Add",command=lambda : insertcom(entry1.get(),entry2.get(),entry3.get()))
        btn.pack()
        window.mainloop()




    # insertcom(data)
    def insertuser():
        def insert():
            conn = DBConnect.connect_db()
            curr = conn.cursor()
            queryy = "insert into login(username,password,name) values('" + str(entry1.get()) + "','" + str(
                entry2.get()) + "','"+str(entry.get())+"');"
            # query1 = "select password from admin"
            if (not curr.execute(queryy)):
                print("Sucess")
                conn.commit()
                # messagebox.showinfo(title="Information",message="Success")
            else:
                messagebox.showerror(title="Error",message="Something Went Wrong")
            # print(s)

            conn.close()

        def successuseradd():

            print(entry2.get(),entry3)
            if entry1.get()=="" or entry2.get()=="" or  entry3.get()=="" or entry.get()=="":
                messagebox.showwarning(title="Warning",message="Field is empty")
            elif entry1.get()!="" and entry2.get()==entry3.get():
                insert()
                messagebox.showinfo(title="Success",message=entry1.get()+" User Added Successfully ")
                window.withdraw()
            elif entry1.get()!="" and entry2.get()!=entry3.get():
                messagebox.showwarning(title="Warning",message="Password is not same as first password")
            else:
                messagebox.showerror(title="Error",message="Something Went Wrong")
                window.withdraw()
        # app=ck.CTk()
        window = ck.CTkToplevel(root)
        window.geometry("300x200")

        window.title("Placement Management")
        window.iconbitmap("Files\\icon.ico")

        # create label on CTkToplevel window

        label = ck.CTkLabel(window, text="Enter Name")
        label.grid(column=3,row=1)
        entry=ck.CTkEntry(window)
        entry.grid(column=4,row=1)
        label1 = ck.CTkLabel(window, text="Enter Username")
        label1.grid(column=3,row=2)
        entry1=ck.CTkEntry(window)
        entry1.grid(column=4,row=2)
        label2 = ck.CTkLabel(window, text="Enter Password")
        label2.grid(column=3,row=3)
        entry2=ck.CTkEntry(window)
        entry2.grid(column=4,row=3)
        label3 = ck.CTkLabel(window, text="Renter Password")
        label3.grid(column=3,row=4)
        entry3 = ck.CTkEntry(window)
        entry3.grid(column=4,row=4)
        btn=ck.CTkButton(window,text="Add",command=successuseradd)
        btn.grid(column=4,row=5)

        # app.mainloop()
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
    def viewLogs():
        # tabview.set("StudentDetails")
        # global studentIdE, slNoE
        sys.setrecursionlimit(1000000000)
        print("optionmenu dropdown clicked:",)
        con = DBConnect.connect_db()
        cur = con.cursor()
        d=time()
        # text = str(choice)
        # text="2020"
        query = "select login_logs from login_activity where date='"+str(d)+"';"
        print(query)
        cur.execute(query)
        fetchall = cur.fetchall()

        app = ck.CTk()
        app.title("Logs")
        app.iconbitmap("Files\\icon.ico")
        app.geometry("500x400")
        # Create A Main Frame
        main_frame = ck.CTkFrame(app)
        main_frame.pack(fill=BOTH, expand=2)

        # Create A Canvas
        my_canvas = ck.CTkCanvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Add A Scrollbar To The Canvas
        my_scrollbar = ck.CTkScrollbar(main_frame, orientation="vertical", command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)
        # my_scrollbar1 = ck.CTkScrollbar(app, orientation="horizontal", command=my_canvas.xview)
        # my_scrollbar1.pack(side=TOP, fill=X)

        # Configure The Canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
        # my_canvas.configure(xscrollcommand=my_scrollbar1.set)
        # my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

        # Create ANOTHER Frame INSIDE the Canvas
        second_frame = ck.CTkFrame(my_canvas)

        # Add that New frame To a Window In The Canvas
        my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
        label0 = ck.CTkButton(second_frame, border_width=2, text="SLNo", state="disabled", height=5,
                              width=60, corner_radius=20)
        label0.grid(row=1, column=0)
        label1 = ck.CTkButton(second_frame, border_width=2, text="Logs", state="disabled", height=5,
                              width=500, corner_radius=20).grid(row=1, column=1)
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
                studentIdE = ck.CTkTextbox(second_frame, width=500, height=5)
                # studentIdE.grid(row=i, column=j + 1)
                studentIdE.grid(row=i, column=j + 1)
                studentIdE.insert("0.0", str(row[j]))
            # studentIdE.bind("<Key>", lambda a: "break")
            i += 1
            slno += 1

        print(i)
        # tabview.configure(require_redraw=True)
        # root.mainloop()
        btn = ck.CTkButton(second_frame, text="Generate Excel Sheet", command=generatexcel_logs)
        btn.grid(row=i + 2, column=1)
        btn1 = ck.CTkButton(second_frame, text="Back", command=app.withdraw)
        btn1.grid(row=i + 3, column=1)

        app.mainloop()

    def funct1(fetchall):
        # tabview.set("StudentDetails")
        # global studentIdE, slNoE
        sys.setrecursionlimit(1000000000)

        app = ck.CTk()
        app.title("Student Details")
        app.iconbitmap("Files\\icon.ico")
        app.geometry("1080x900")
        app.state("zoomed")
        # Create A Main Frame
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
        ck.CTkLabel(app, text="A total of " + str(procedure[0][0]) + " Students got placed in the "+str(optionmenu_var.get())+" batch ", font=("arial", 20, "bold"))\
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
        btn = ck.CTkButton(second_frame, text="Generate Excel Sheet", command=generatexcel)
        btn.grid(row=i + 2, column=5)
        btn1 = ck.CTkButton(second_frame, text="Back", command=app.withdraw)
        btn1.grid(row=i + 2, column=6)

        # tabview.configure(require_redraw=True)
        app.mainloop()
    def delete():
        con=DBConnect.connect_db()
        cur=con.cursor()
        # print(ent1.get())
        query="DELETE FROM `placed` WHERE `placed`.`usn` = '"+ent1.get()+"';"
        execu=cur.execute(query)
        if(not execu):
            print(execu)
            con.commit()
            messagebox.showinfo(title="Information",message=str(ent1.get())+"deleted Sucessfully")
            # con.commit()
        else:
            messagebox.showerror(title="Error",message="Error While deleting "+str(ent1.get())+" Check if the existance of USN")

        con.close()
    def generatexcel_logs():
        # cur.execute(query)
        # tabview.tab("StudentDetails").quit()
        try:
            d=time()
            con = DBConnect.connect_db()
            cur = con.cursor()
            query = sql.read_sql("select login_logs from login_activity where date='"+str(d)+"';", con)

            query.to_excel(str(d)+"_Logs.xls")
            messagebox.showinfo(title="Sucess", message="ExcelFile Generated")

        except:
            messagebox.showerror(title="error", message="error")

    # def edit_form():
    #     # print(usn.get())
    #     # a=usn.get()
    #     entryForm2.onsucess(str(usn.get()))
    def generatexcel():
        # cur.execute(query)
        # tabview.tab("StudentDetails").quit()
        try:
            con = DBConnect.connect_db()
            cur = con.cursor()
            # text = str(choice)
            text = "2020"
            query = sql.read_sql("select * from placed where batch =" + str(text) + " ;", con)
            # print(query)
            query.to_excel("2020.xls")
            messagebox.showinfo(title="Sucess", message="ExcelFile Generated")

        except:
            messagebox.showerror(title="error", message="error")

    root=ck.CTk()
    root.geometry("600x600")
    # txt=password()
    # root.title("")
    root.iconbitmap("Files\\icon.ico")
    txt=usname
    root.title("LoggedIn As "+txt)
    # txt="mam"
    batch=tr.batch()
    com=tr.company()
    print(batch)
    # branch=tr. branch()
    # company=tr.company()
    ck.CTkLabel(root,text="Welcome "+str(txt),font=("arial",20,"bold")).pack(padx=100,side="top",anchor="center")
    ck.CTkLabel(root,text="Retrive Placed Student Details").place(relx=.4, rely=.1, anchor="center")
    optionmenu_var = ck.StringVar(value="2020")  # set initial value
    combobox = ck.CTkComboBox(root,
                                         values=batch,
                                         command=optionmenu_callback,
                                         variable=optionmenu_var)
    combobox.place(relx=.68, rely=.1, anchor="center")
    ck.CTkLabel(root,text="Add Newly Placed Student Details").place(relx=.3, rely=.2, anchor="center")
    btn1 = ck.CTkButton(root, text="Add New Student", command=form)
    btn1.place(relx=.7, rely=.2, anchor="center")
    ck.CTkLabel(root, text="Add Newly Placed Student Batch").place(relx=.3, rely=.3, anchor="center")
    btn2 = ck.CTkButton(root, text="Add", command=getyear)
    btn2.place(relx=.7, rely=.3, anchor="center")
    ck.CTkLabel(root, text="Add Newly Recruited Company").place(relx=.3, rely=.4, anchor="center")
    btn3 = ck.CTkButton(root, text="Add", command=getcompany)
    btn3.place(relx=.7, rely=.4, anchor="center")
    ck.CTkLabel(root, text="Add New User").place(relx=.3, rely=.5, anchor="center")
    btn4 = ck.CTkButton(root, text="Add", command=insertuser)
    btn4.place(relx=.7, rely=.5, anchor="center")
    ck.CTkLabel(root, text="View Logs").place(relx=.3, rely=.6, anchor="center")
    btn5 = ck.CTkButton(root, text="View", command=viewLogs)
    btn5.place(relx=.7, rely=.6, anchor="center")
    usn=customtkinter.StringVar()
    ent=ck.CTkEntry(root,textvariable=usn,placeholder_text="Enter USN")
    ent.place(relx=.3, rely=.7, anchor="center")
    btn5 = ck.CTkButton(root, text="Edit", command=lambda :entryForm2.onsucess(str(ent.get())))
    btn5.place(relx=.7, rely=.7, anchor="center")
    usn1 = customtkinter.StringVar()
    ent1 = ck.CTkEntry(root, textvariable=usn1,placeholder_text="Enter USN")
    ent1.place(relx=.3, rely=.8, anchor="center")
    btn5 = ck.CTkButton(root, text="Delete", command=delete)
    btn5.place(relx=.7, rely=.8, anchor="center")
    bat = ck.StringVar()  # set initial value
    comboboxb = ck.CTkComboBox(root,
                              values=batch,
                              variable=bat)
    comboboxb.place(relx=.2, rely=.9, anchor="center")
    comp = ck.StringVar()  # set initial value
    comboboxc = ck.CTkComboBox(root,
                              values=com,
                              variable=comp)
    comboboxc.place(relx=.45, rely=.9, anchor="center")
    btn5 = ck.CTkButton(root, text="View", command=getBC)
    btn5.place(relx=.7, rely=.9, anchor="center")
    btn6 = ck.CTkButton(root, text="Logout", command=root.withdraw)
    btn6.place(relx=.5, rely=.95, anchor="center")

    root.mainloop()
def time():
    # Getting current date and time
    now = dt.now()
    # s = now.strftime(" %I  %M %p ||  %a %d - %m - %y")
    d = now.strftime("%a %d - %m - %y")
    # print(d)
    return d
# print(time("ashhad"))