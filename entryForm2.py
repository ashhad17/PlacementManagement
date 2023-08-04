import customtkinter

import customtkinter as ck
from tkinter import messagebox
import DBConnect
import trails as tr
def onsucess(usn_edit):
    # -----------------------------------------------------------------------------------------------------------------------

    root = ck.CTk()

    root.iconbitmap("Files\\icon.ico")
    root.title("Edit Student Registration Form")
    # ck.set_appearance_mode("system")
    # root.geometry("500x300")
    # root.attributes('-fullscreen', True)
    root.state('zoomed')
    # -----------------------------------------------------------------------------------------------------------------------
    def insertion():
        p = package_field.get()
        n = name_field.get()
        u = usn_field.get()
        br = branch_field.get()
        bt = batch_field.get()
        do = dob_field.get()
        de = designation_field.get()
        cm = company_field.get()
        # of = offers_field.get()
        em = email_field.get()
        co = contact_no_field.get()
        print(p, n, u, br, bt, do, de, cm, em, co)
        yes = package_field.get() and name_field.get() and usn_field.get() and batch_field.get() and batch_field.get() and dob_field.get() and designation_field.get() and company_field.get()  and email_field.get() and contact_no_field.get()

        print(yes)
        con1=DBConnect.connect_db()
        cur1=con1.cursor()
        cur1.execute("select usn from placed")
        u_s_n =cur1.fetchall()
        print("--------------------------------",u_s_n)
        con1.close()

        if yes:
            try:
                if usn_field.get() in u_s_n:
                    # print("Exist")
                    messagebox.showerror()
                con = DBConnect.connect_db()
                cur = con.cursor()
                values = str(p) + "', '" + str(n) + "', '" + str(u) + "', '" + str(br) + "', '" + str(
                    bt) + "', '" + str(
                    do) + "','" + str(de) + "','" + str(cm) + "', '" + str(em) + "', '" + str(co)
                print(values)
                # query = "insert into placed(package,name,usn,branch,batch,dob,designation,company,offers,email,mobile) values( '" + values + "');"
                query = "UPDATE `placed` SET `name`='"+str(n)+"',`usn`='"+str(u)+"',`branch`='"+str(br)+"',`batch`='"+str(bt)+"',`email`='"+str(em)+"',`mobile`='"+str(co)+"',`dob`='"+str(do)+"',`company`='"+str(cm)+"',`designation`='"+str(de)+"',`package`='"+str(p)+"' WHERE `usn`='"+str(usn_edit)+"';"
                print(query)
                if (not cur.execute(query)):
                    messagebox.showinfo(title="Data", message="Sucess")
                    con.commit()
                    con.close()
                    root.withdraw()
                else:
                    print(con.rollback())
                    messagebox.showerror(title="Error", message="Query did'nt Executed properly")

            except Exception as e:
                print(e)
                E=str(e)
                print(E[13:42])
                messagebox.showerror(title="Error", message="Something Went Wrong"+E[13:42])

    # -----------------------------------------------------------------------------------------------------------------------
    def edit():
        con=DBConnect.connect_db()
        cur=con.cursor()
        print(usn_edit)
        cur.execute("select * from placed where usn = '"+str(usn_edit)+"'")
        fetch=cur.fetchall()
        print(fetch)
        con.close()
        name_field.insert(0,fetch[0][0])
        usn_field.insert(0,fetch[0][1])

        # Branch = customtkinter.StringVar(value="CSE")  # set initial value
        branch_field.set(fetch[0][2])
        batch_field.set(fetch[0][3])

        contact_no_field.insert(0,fetch[0][5])
        email_field.insert(0,fetch[0][4])
        designation_field.insert(0,fetch[0][9])
        package_field.insert(0,fetch[0][10])
        # Company = customtkinter.StringVar()  # set initial value
        company_field.set(fetch[0][7])
        dob_field.insert(0,fetch[0][6])
        # offers_field.insert(0,fetch[0][8])


    ck.CTkLabel(root, text="Student Details Form",
                width=100, height=25, fg_color=("white", "gray75")
                , corner_radius=8, font=("arial", 50)).grid(row=0, column=5, padx=50)
    name = ck.CTkLabel(root, text="Name")
    usn = ck.CTkLabel(root, text="USN")
    dob = ck.CTkLabel(root, text="Date Of Birth")
    email = ck.CTkLabel(root, text="Email")
    contact_no = ck.CTkLabel(root, text="Contact No.")
    # offers = ck.CTkLabel(root, text="Offers")
    company = ck.CTkLabel(root, text="Company")
    package = ck.CTkLabel(root, text="Package")
    designation = ck.CTkLabel(root, text="Designation")
    branch = ck.CTkLabel(root, text="Branch")
    batch = ck.CTkLabel(root, text="Batch No.")

    # -----------------------------------------------------------------------------------------------------------------------
    Name = customtkinter.StringVar()
    USN = customtkinter.StringVar()
    # Branch = customtkinter.StringVar()
    # Batch = customtkinter.StringVar()
    Contact = customtkinter.StringVar()
    Email = customtkinter.StringVar()
    Designation = customtkinter.StringVar()
    Package = customtkinter.StringVar()
    # Company = customtkinter.StringVar()
    DOB = customtkinter.StringVar()
    # Offers = customtkinter.StringVar()
    # -----------------------------------------------------------------------------------------------------------------------
    batch1 = tr.batch()
    branch1 = tr.branch()
    company1 = tr.company()
    name_field = ck.CTkEntry(root, textvariable=Name)
    usn_field = ck.CTkEntry(root, textvariable=USN)

    Branch = customtkinter.StringVar(value="CSE")  # set initial value
    branch_field = customtkinter.CTkComboBox(root,
                                             values=branch1,
                                             variable=Branch)
    # combobox.pack(padx=20, pady=10)
    Batch = customtkinter.StringVar()  # set initial value
    batch_field = customtkinter.CTkComboBox(root,
                                            values=batch1,
                                            variable=Batch)

    contact_no_field = ck.CTkEntry(root, textvariable=Contact)
    email_field = ck.CTkEntry(root, textvariable=Email)
    designation_field = ck.CTkEntry(root, textvariable=Designation)
    package_field = ck.CTkEntry(root, textvariable=Package)
    Company = customtkinter.StringVar()  # set initial value
    company_field = customtkinter.CTkComboBox(root,
                                              values=company1,
                                              variable=Company)

    dob_field = ck.CTkEntry(root, textvariable=DOB)
    # offers_field = ck.CTkEntry(root, textvariable=Offers)
    # -----------------------------------------------------------------------------------------------------------------------
    name.grid(row=3, column=1)
    usn.grid(row=3, column=4)
    dob.grid(row=3, column=7)
    # email.grid(row=2, column=1)
    contact_no.grid(row=4, column=1)
    # offers.grid(row=4, column=4)
    company.grid(row=4, column=7)
    package.grid(row=5, column=1)
    designation.grid(row=5, column=4)
    branch.grid(row=5, column=7)
    batch.grid(row=6, column=1)
    email.grid(row=4, column=4)
    # -----------------------------------------------------------------------------------------------------------------------
    name_field.grid(row=3, column=2, ipadx="100", pady="20", padx="20")
    usn_field.grid(row=3, column=5, ipadx="100", pady="20", padx="20")
    dob_field.grid(row=3, column=8, ipadx="100", pady="20", padx="20")
    contact_no_field.grid(row=4, column=2, ipadx="100", pady="20", padx="20")
    # offers_field.grid(row=4, column=5, ipadx="100", pady="20", padx="20")
    company_field.grid(row=4, column=8, ipadx="100", pady="20", padx="20")
    package_field.grid(row=5, column=2, ipadx="100", pady="20", padx="20")
    designation_field.grid(row=5, column=5, ipadx="100", pady="20", padx="20")
    branch_field.grid(row=5, column=8, ipadx="100", pady="20", padx="20")
    batch_field.grid(row=6, column=2, ipadx="100", pady="20", padx="20")
    email_field.grid(row=4, column=5, ipadx="100", pady="20", padx="20")
    # -----------------------------------------------------------------------------------------------------------------------
    edit()
    submit = ck.CTkButton(root, text="Submit", command=insertion)
    submit.grid(row=8, column=5)

    root.mainloop()
# onsucess("1cg20cs055")