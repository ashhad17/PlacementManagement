import DBConnect
# from Trails.CustomTkinter.FirstGui import onLogin
import Login1,Login2
from tkinter import messagebox
# import opener
from datetime import datetime as dt

def db(usnames,passwd):
    if usnames == "" and passwd=="":
        messagebox.showwarning(
            title="Warning",
            message="Login Required"
        )
    elif(usnames == ""):
        messagebox.showwarning(
            title="Warning",
            message="Username Required"
        )
    elif(passwd==""):
        messagebox.showwarning(
            title="Warning",
            message="Password Required"
        )
    else:
        con = DBConnect.connect_db()
        # creating cur in db
        cur = con.cursor()
        usname = "select username from login"
        cur.execute(usname)
        new_name = cur.fetchall()

        con.close()
        con1 = DBConnect.connect_db()
        # creating cur in db
        cur1 = con1.cursor()
        usname = "select password from login"
        cur1.execute(usname)
        new_pass = cur1.fetchall()
        # print("new",new_pass)
        con1.close()
        con2=DBConnect.connect_db()
        cur2=con2.cursor()
        cur2.execute("select name from login")
        name=cur2.fetchall()
        con2.close()
        print("new",name)
        print(new_name)
        l = len(new_name)
        con3 = DBConnect.connect_db()
        cur3 = con3.cursor()
        usname3 = "select username from pincharge;"
        cur3.execute(usname3)
        usn3 = cur3.fetchone()
        con3.close()
        con4 = DBConnect.connect_db()
        cur4 = con4.cursor()
        pass4 = "select password from pincharge;"
        cur4.execute(pass4)
        usn4 = cur4.fetchone()
        # print(usn3[0])
        # print(usn4[0])
        cur4.close()
        con5 = DBConnect.connect_db()
        cur5 = con4.cursor()
        cur5.execute("select name from pincharge;")
        name1 = cur5.fetchone()
        cur4.close()
        print(new_name)
        print(new_pass)
        print(usn3)
        print(usn4)
        print(name1)
        print(len(usn4))
        u=""
        p=""
        n=""
        u1=""
        p1=""
        n1=""
        for i in range(l, 0, -1):
            print(i)
            print(new_name[i - 1][0], "  ", new_pass[i - 1][0])
            if (usnames == new_name[i - 1][0] and passwd == new_pass[i - 1][0]):
                u=new_name[i - 1][0]
                p=new_pass[i - 1][0]
                n=name[i - 1][0]
        for i in range(len(usn4),0,-1):
            print(i)
            print(usn3[i - 1], "  ", usn4[i - 1])
            if (usnames == usn3[i - 1] and passwd == usn4[i - 1]):
                u1=usn3[i - 1]
                # u=usn3[i - 1]
                p1=usn4[i - 1]
                n1=name1[i - 1]
        print("final:",u,p,n)
        print("final1:",u1,p1,n1)
        if (usnames == u1 and passwd == p1):
            time(usnames)
            Login2.login(n1)
        else:
            messagebox.showwarning(title="warning",message="Incorrect username or password")



def time(usnames):
    # Getting current date and time
    now = dt.now()
    s = now.strftime(" %I  %M %p ||  %a %d - %m - %y")
    d = now.strftime("%a %d - %m - %y")
    print(d)
    conl = DBConnect.connect_db()
    curl = conl.cursor()
    curl.execute("INSERT INTO `login_activity` (`login_logs`,`date`) VALUES('" + str(usnames) + " is LoggedIn on " + str(s) + "','"+str(d)+"');")
    conl.commit()
    conl.close()
    # return d
