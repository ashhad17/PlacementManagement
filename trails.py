import DBConnect

def batch():
    con = DBConnect.connect_db()
    cur=con.cursor()
    query="select batch_year from batch"
    cur.execute(query)
    s=cur.fetchall()
    lst=[]
    for i in range(len(s)):
        # print(s[i][0])
        lst.append(str(s[i][0]))
    con.close()
    # print(lst)
    return lst
def company():
    con = DBConnect.connect_db()
    cur = con.cursor()
    query = "select company_name from company"
    cur.execute(query)
    s = cur.fetchall()
    lst = []
    for i in range(len(s)):
        # print(s[i][0])
        lst.append(str(s[i][0]))
    con.close()
    # print(lst)
    return lst
def branch():
    con = DBConnect.connect_db()
    cur = con.cursor()
    query = "select branch_name from branch"
    cur.execute(query)
    s = cur.fetchall()
    lst = []
    for i in range(len(s)):
        # print(s[i][0])
        lst.append(str(s[i][0]))
    con.close()
    # print(lst)
    return lst
# batch()
# company()
# blst=branch()
# blst
# print(blst)
