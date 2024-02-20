def adduser():
    import mysql.connector as Book
    Book=Book.connect(host="localhost",user="root",password="4568",database="12_project")
    Bcursor=Book.cursor( )
    Bcursor.execute('Select * from User')
    R=Bcursor.fetchall()
    Pcode=input('Enter the postal code:')
    Rec=(Pcode)
    for i in R:
        if i[2]==Rec[0]:
            print('id not expired')
            break
    else:
        Name=input('Enter the user name:')
        Pno=int(input('Enter the phone no:'))
        city=input('Enter the city:')
        date=input('Enter the date of birth:')
        A="insert into User values('{}','{}','{}','{}','{}')".format(Name,Pno,Pcode,city,date)
        Bcursor.execute(A)
        Book.commit()
        print("**user details added**")

def display():
    import mysql.connector as Book
    Book=Book.connect(host="localhost",user="root",password="4568",database="12_project")
    Bcursor=Book.cursor( )
    Bcursor.execute('Select * from User')
    print("(Name,Pno,Pcode,city,date)")
    J=Bcursor.fetchall()
    for i in J:
        print(i)

def search():
    import mysql.connector as Book
    Book=Book.connect(host="localhost",user="root",password="4568",database="12_project")
    Bcursor=Book.cursor( )
    p=input('Enter the Pcode of the user to be searched:')
    a="select*from user where Pcode='{}'".format(p)
    Bcursor.execute(a)
    J=Bcursor.fetchall()
    print(J)

def update():
    import mysql.connector as Book
    Book=Book.connect(host="localhost",user="root",password="4568",database="12_project")
    Bcursor=Book.cursor( )
    while True:
        print('*'*50)
        print('\t\t user details')
        print('*'*50)
        print('1.Name')
        print('2.Phone')
        print('3.City')
        print('4.Date of Birth')
        print('5.Exit')
        print('*'*50)
        x=int(input('Enter the choice to be modified:'))
        print('*'*50)
        print('NOTE-****The updation will be done on the basis of Pcode provided by the Database****')
        if x==1:
            p=input('Enter the postal code of the user:')
            name=input('Enter the name to be modified:')
            a="update user set Name='{}'where Pcode='{}'".format(name,p)
            Bcursor.execute(a)
            Book.commit()
            print('data modified!')
        if x==2:
            p=input('Enter the postal code of the user:')
            phno=input('Enter the phone no. to be modified:')
            a="update user set Pno='{}'where Pcode='{}'".format(phno,p)
            Bcursor.execute(a)
            Book.commit()
            print('data modified!')
        if x==3:
            p=input('Enter the postal code:')
            city=input('Enter the city to be modified:')
            a="update user set City='{}'where Pcode='{}'".format(city,p)
            Bcursor.execute(a)
            Book.commit()
            print('data modified!')
        if x==4:
            p=input('Enter the postal code:')
            date=input('Enter the DOB to be modified:')
            a="update user set date='{}'where Pcode='{}'".format(date,p)
            Bcursor.execute(a)
            Book.commit()
            print('data modified!')
        if x==5:
            break

def delete():
    import mysql.connector as Book

    Book=Book.connect(host="localhost",user="root",password="4568",database="12_project")
    Bcursor=Book.cursor( )
    p=input('Enter the Pcode whose detail has to be deleted:')
    a="Delete from user where Pcode='{}'".format(p)
    Bcursor.execute(a)
    Book.commit()
    print('data deleted')

