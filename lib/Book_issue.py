def issue():
    import mysql.connector as Book
    Book=Book.connect(host="localhost",user="root",password="4568",database="12_project")
    Bcursor=Book.cursor( )
    qty="select p_id,sum(qtyissue) from issue group by p_id"
    Bcursor.execute(qty)
    r=Bcursor.fetchall()
    print(r)
    pid=input("enter person id:")
    rec=(pid,)
    for i in r:
        if i[0]==rec[0]:
            if i[1]>1:
                print("first return the book")
        else:
                print("reissue the book")
                print("*"*50)
                b_id=input("enter the book id:")
                b_name=input("enter the book name to be issued:")
                p_id=input("enter person id:")
                qtyissue=int(input("enter the Quantity of the book issued:"))
                print("*"*55)
                E="insert into issue values".format(b_id,b_name,p_id,qtyissue)
                Bcursor.execute(E)
                Book.commit()
                print("********Information Added********")
                print("/n")
    else:
             print("wrong id")

def search():
    import mysql.connector as Book
    Book=Book.connect(host="localhost",user="root",password="4568",database="12_project")
    Bcursor=Book.cursor( )
    p_id=input("enter person id:")
    A="select * from issue where p_id=%s"
    rec=(p_id,)
    Bcursor.execute(A,rec)
    B=Bcursor.fetchall()
    print(B)
    print("\n")

def returnbook():
    import mysql.connector as Book
    Book=Book.connect(host="localhost",user="root",password="4568",database="12_project")
    Bcursor=Book.cursor( )
    b_id=input("enter book id:")
    p_id=input("enter person id:")
    qty=int(input("enter the quantity of book:"))
    rec=(b_id,p_id,qty)
    Bcursor.execute("select * from issue")
    r=Bcursor.fetchall()
    print(r)
    for i in r:
        if i[0]==rec[0] and [2]==rec[1]:
            a="update issue set qtyissue='{}' where b_id='{}' and p_id='{}'".format(i[3]-qty,i[0],i[2])
            Bcursor.execute(a)
            Book.commit()
            print("updated issue file")
            break
        else:
            print("not found id")

def Updatebook():
    import mysql.connector as Book
    Book=Book.connect(host="localhost",user="root",password="4568",database="12_project")
    Bcursor=Book.cursor( )
    def updateissue():
        b_id=input("enter book id:")
        qty=int(input("enter the quantity of book:"))
        rec=(b_id,qty)
        Bcursor.execute("select * from Quest_library")
        r=Bcursor.fetchall()
        for i in r:
            if i[0]==rec[0]:
                a1="update Quest_library set quantity={} where i_d='{}'".format(i[3]+qty,i[0])
                Bcursor.execute(a1)
                Book.commit()
                print("updated book file")
                break
            else:
                print("wrong ID!")
                print("\n")
        def updatereturn():
            b_id=input("enter book id:")
            qty=int(input("enter the quantity of book:"))
            rec=(b_id,qty)
            Bcursor.execute("select * from Quest_library")
            r=Bcursor.fetchall()
            for i in r:
                if i[0]==rec[0]:
                    a1="update Quest_library set quantity={} where i_d='{}'".format(i[3]+qty,i[0])
                    Bcursor.execute(a1)
                    Book.commit()
                    print("updated book file")
                    break
                else:
                    print("wrong ID!")
                    print("\n")
            while True:
                print("1 : update book while issue Book ")
                print("2 : update book while return Book ")
                print("3: exit ")
                ch=int(input("******* Enter Your Choice *******"))
                if ch==1:
                    updateissue()
                elif ch==2:
                    updatereturn()
                elif ch==3:
                    break  
                else:
                    print("***INVALID CHOICE***")



