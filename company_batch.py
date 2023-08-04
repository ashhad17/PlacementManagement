import sys
from tkinter import messagebox

from pandas.io import sql

import DBConnect
import customtkinter as ck
from tkinter import *


def onsucess(compp,batt):
    print("HEy",batt.get(),compp.get())
    bat=batt.get()
    comp=compp.get()
    def generatexcel():
        # cur.execute(query)
        # tabview.tab("StudentDetails").quit()
        try:
            con = DBConnect.connect_db()
            cur = con.cursor()
            # text = str(choice)
            text = "2020"
            query = sql.read_sql(
                "select * from placed where batch ='" + str(bat) + "' and company='" + str(comp) + "'  ;", con)
            # print(query)
            query.to_excel(str(bat)+"_"+str(comp)+".xls")
            messagebox.showinfo(title="Sucess", message="ExcelFile Generated")

        except:
            messagebox.showerror(title="error", message="error")

    def optionmenu_callback():
        # print("optionmenu dropdown clicked:", choice)
        con = DBConnect.connect_db()
        cur = con.cursor()
        # text = str(choice)
        # text="2020"
        query = "select * from placed where batch ='"+ str(bat) +"' and company='"+str(comp)+"' ;"
        print(query)
        cur.execute(query)
        global fetchall
        fetchall = cur.fetchall()
        # con.close()
        funct1(fetchall)
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
        second_frame = ck.CTkFrame(my_canvas)

        # Add that New frame To a Window In The Canvas
        my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

        conb = DBConnect.connect_db()
        curb = conb.cursor()
        curb.execute("select count(usn) from placed where batch='"+str(bat)+"' and company='"+str(comp)+"';")
        # "CALL `Total`('2020');"
        procedure=curb.fetchall()
        conb.close()
        print("Procedure",procedure[0][0])
        ck.CTkLabel(app, text="A total of " + str(procedure[0][0]) + " Students got placed in " + str(
            comp) + " in the " + str(bat) + " batch ", font=("arial", 20, "bold")) \
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

        app.mainloop()
    optionmenu_callback()

# onsucess()
